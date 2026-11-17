"""Exercise the coverage gate against real commits and the Git index."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

CHECK = Path(__file__).resolve().parents[1] / "scripts" / "check_coverage.py"


class CoverageCheck(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.name", "Newsletter fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.write("archive.md", "# Archive\n")
        self.add_edition("original", "Engineering", "Files")
        self.commit("First edition")
        for revision in ("first repair", "second repair"):
            self.write("editions/original/lab.txt", revision)
            self.commit(revision)

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, text=True).strip()

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def commit(self, title):
        self.git("add", ".")
        self.git("commit", "-qm", title)

    def add_edition(self, slug, desk, topic):
        for filename in ("brief.md", "index.html", "sources.md"):
            self.write(f"editions/{slug}/{filename}", "fixture\n")
        with (self.root / "archive.md").open("a", encoding="utf-8") as index:
            index.write(f"\n## {desk}\n\n### {topic}\n\n**[Brief](editions/{slug}/brief.md)**\n")

    def check(self, *args, expected=0):
        result = subprocess.run([sys.executable, str(CHECK), "--base", "HEAD", *args],
                                cwd=self.root, text=True, capture_output=True)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result.stdout + result.stderr

    def test_repeated_lab_repair_is_held_unless_reader_impact_is_recorded(self):
        self.write("editions/original/lab.txt", "repair broken instructions")
        self.git("add", ".")
        self.assertIn("recent coverage", self.check(expected=1))
        self.assertIn("Editorial exception for review", self.check("--exception", "The published exercise now fails at step one."))

    def test_staged_mixed_issue_and_exact_commit_match(self):
        base = self.git("rev-parse", "HEAD")
        self.add_edition("hills", "Everyday life", "Map reading")
        self.add_edition("heat", "Frontier technology", "Heat pumps")
        self.write("issues/2026-11-15.md", "## Everyday life · Hill\n[Map](../editions/hills/brief.md)\n## Frontier technology · Heat\n[Heat](../editions/heat/brief.md)")
        self.git("add", ".")
        self.write("issues/2026-11-15.md", "unstaged change")
        staged = self.check()
        self.assertIn("heat, hills", staged)
        self.git("commit", "-qm", "Mixed issue")
        self.assertEqual(staged, self.check("--base", base, "--head", "HEAD"))

    def test_one_desk_issue_cannot_use_an_exception_to_skip_the_mix(self):
        self.write("issues/2026-11-15.md", "## Engineering · Files\n[Files](../editions/original/brief.md)")
        self.git("add", ".")
        self.assertIn("at least two sections", self.check("--exception", "Documented correction", expected=1))

    def test_date_only_reprint_and_cross_desk_footer(self):
        self.add_edition("hills", "Everyday life", "Map reading")
        issue = ("## Everyday life · Hills\n[Map](../editions/hills/brief.md)\n"
                 "## Engineering · Files\n[Files](../editions/original/brief.md)\n")
        self.write("issues/2026-11-15.md", issue)
        self.commit("Two featured stories")
        self.write("issues/2026-11-22.md", issue)
        self.git("add", ".")
        self.assertIn("previous four issues", self.check(expected=1))
        self.write("issues/2026-11-22.md", "## Engineering · Files\n[Files](../editions/original/brief.md)\n"
                   "From the archives: [Map](../editions/hills/brief.md)\n")
        self.git("add", ".")
        self.assertIn("at least two sections", self.check(expected=1))

    def test_existing_brief_cannot_silently_disappear_from_counts(self):
        path = self.root / "archive.md"
        path.write_text(path.read_text().replace("**[Brief]", "[Brief]"))
        self.git("add", ".")
        self.assertIn("lost its archive entry", self.check(expected=1))

    def test_same_edition_cannot_be_indexed_twice_under_one_topic(self):
        with (self.root / "archive.md").open("a", encoding="utf-8") as index:
            index.write("\n**[Duplicate](editions/original/brief.md)**\n")
        self.git("add", ".")
        self.assertIn("indexed more than once", self.check(expected=1))

    def test_renaming_the_question_under_the_same_recent_topic_does_not_rotate_it(self):
        self.add_edition("same", "Engineering", "Files")
        self.git("add", ".")
        self.assertIn("least-covered", self.check(expected=1))


    def test_archive_cross_references_and_template_links_are_not_editions(self):
        self.add_edition("hills", "Everyday life", "Map reading")
        with (self.root / "archive.md").open("a", encoding="utf-8") as index:
            index.write("[Back issue](editions/original/brief.md) · [Template](editions/_template/brief.md)\n")
        self.git("add", ".")
        self.assertIn("Newly indexed editions | hills", self.check())

    def test_navigation_maintenance_does_not_add_an_edition_or_reset_history(self):
        self.write("README.md", "[A reprint](editions/original/brief.md)")
        self.commit("Feature an older story")
        self.assertIn("Newly indexed editions | none", self.check())
        self.write("editions/original/lab.txt", "routine maintenance again")
        self.git("add", ".")
        self.assertIn("recent coverage", self.check(expected=1))


if __name__ == "__main__":
    unittest.main()
