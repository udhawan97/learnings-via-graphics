#!/usr/bin/env python3
"""Review staged or committed newsletter coverage against the default branch."""
import argparse
from collections import Counter
from datetime import date
from pathlib import PurePosixPath
import re
import subprocess
import sys

DESKS = ("Engineering", "Frontier technology", "Everyday life", "Work & money")
BRIEF = re.compile(r"\]\((?:\.\./)?editions/([^/)]+)/brief\.md(?:#[^)]*)?\)")
ISSUE = re.compile(r"issues/(\d{4}-\d{2}-\d{2})\.md")
WINDOW = 4


def git(*args):
    return subprocess.run(["git", *args], check=True, stdout=subprocess.PIPE,
                          text=True).stdout


def read_file(ref, path):
    # An empty ref addresses the index, including files staged for the first time.
    return git("show", f"{ref}:{path}")


def archive(ref):
    records = {}
    desk = topic = None
    for line in read_file(ref, "archive.md").splitlines():
        if line.startswith("## "):
            desk = line[3:].strip()
            topic = None
        elif line.startswith("### "):
            topic = line[4:].strip()
        elif desk in DESKS and topic and line.startswith("**["):
            for slug in BRIEF.findall(line):
                home = (desk, topic)
                if slug in records and records[slug] != home:
                    raise ValueError(f"{slug} is indexed under two topics")
                if slug in records:
                    raise ValueError(f"{slug} is indexed more than once")
                records[slug] = home
    return records


def edition(path):
    parts = PurePosixPath(path).parts
    if len(parts) >= 3 and parts[0] == "editions" and parts[1] != "_template":
        return parts[1]
    return None


def recent_deliveries(base, before):
    history = []
    for sha in git("rev-list", "--first-parent", base).splitlines():
        paths = git("diff-tree", "--root", "--diff-merges=first-parent", "-r",
                    "--no-commit-id", "--name-only", "--no-renames", sha).splitlines()
        slugs = {edition(path) for path in paths} & before.keys()
        if not slugs:
            continue
        new = set()
        if "archive.md" in paths:
            parent = git("show", "-s", "--format=%P", sha).split()
            previous = archive(parent[0]) if parent and git("ls-tree", parent[0], "archive.md") else {}
            new = set(archive(sha)) - previous.keys() if git("ls-tree", sha, "archive.md") else set()
        history.append((sha, {before[slug] for slug in slugs}, bool(slugs & new)))
        if len(history) == WINDOW:
            break
    return history


def featured_stories(ref, path, records=None):
    features = {}
    section = None
    for line in read_file(ref, path).splitlines():
        if line.startswith("## "):
            if section and section not in features:
                raise ValueError(f"{path}: {section} needs its own linked brief")
            heading = line[3:]
            parts = heading.split(" · ", 1)
            desk = parts[0]
            if desk in DESKS and (len(parts) == 1 or not parts[1].strip()):
                raise ValueError(f"{path}: {desk} section needs a headline")
            if desk in DESKS and heading in features:
                raise ValueError(f"{path} duplicates section heading {heading}")
            section = heading if desk in DESKS else None
        elif section and section not in features:
            match = BRIEF.search(line)
            if match:
                slug = match.group(1)
                if records is not None and records.get(slug, (None,))[0] != section.split(" · ", 1)[0]:
                    raise ValueError(f"{path}: first brief in {section} must be indexed in that section")
                features[section] = slug
    if section and section not in features:
        raise ValueError(f"{path}: {section} needs its own linked brief")
    return features


def check_issues(base, head, compare, records):
    previous = set(git("ls-tree", "-r", "--name-only", base, "--", "issues").splitlines())
    changed = git("diff", "--diff-filter=ACMT", "--name-only", *compare, "--", "issues").splitlines()
    issues = {path for path in previous.union(changed) if path.endswith(".md")}
    reprints = []
    for path in sorted(set(changed) & issues):
        match = ISSUE.fullmatch(path)
        try:
            date.fromisoformat(match.group(1))
        except (AttributeError, ValueError):
            raise ValueError(f"{path} must use a valid YYYY-MM-DD date") from None
        features = featured_stories(head, path, records)
        if len({records[slug][0] for slug in features.values()}) < 2:
            raise ValueError(f"{path} needs featured briefs from at least two sections")
        if path in previous:
            continue
        earlier = sorted((name for name in issues if name < path), reverse=True)[:WINDOW]
        recent = {slug for name in earlier
                  for slug in featured_stories(base if name in previous else head, name).values()}
        if earlier and set(features.values()) <= recent:
            reprints.append(path)
    if reprints:
        return ", ".join(reprints) + " only features stories from the previous four issues."
    return ""


def check(base, head, reason):
    before, after = archive(base), archive(head)
    counts = Counter(desk for desk, _ in before.values())
    fewest = min(counts[desk] for desk in DESKS)
    light = {desk for desk in DESKS if counts[desk] == fewest}
    history = recent_deliveries(base, before)
    print("Indexed editions at base | " + " · ".join(f"{d} {counts[d]}" for d in DESKS))
    print("Least-covered sections | " + ", ".join(sorted(light)))
    for sha, homes, fresh in history:
        print(sha[:9], "edition added" if fresh else "maintenance",
              ", ".join(" / ".join(home) for home in sorted(homes)))

    compare = [base, head] if head else ["--cached", base]
    paths = git("diff", "--no-renames", "--name-only", *compare, "--").splitlines()
    touched = {edition(path) for path in paths} - {None}
    added = {slug for slug in after.keys() - before.keys() if slug in touched}
    for slug in sorted(added):
        for name in ("brief.md", "index.html", "sources.md"):
            read_file(head, f"editions/{slug}/{name}")

    hold = check_issues(base, head, compare, after)
    for slug in before.keys() - after.keys():
        probe = subprocess.run(["git", "cat-file", "-e", f"{head}:editions/{slug}/brief.md"],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if probe.returncode == 0:
            hold = f"The existing brief {slug} lost its archive entry."
    if after.keys() - before.keys() - added:
        raise ValueError("New archive entries must include the edition files in this change")
    print("Newly indexed editions | " + (", ".join(sorted(added)) or "none"))

    old_topics = {before[s] for s in touched if s in before}
    recent_topics = set().union(*(homes for _, homes, _ in history))
    fresh_topics = {after[s] for s in added} - recent_topics
    if not hold and added and not any(desk in light for desk, _ in fresh_topics):
        hold = "The proposal adds no edition on a different recent topic in a least-covered section."
    elif not hold and touched and not added and (old_topics & recent_topics or
                        (len(history) >= 2 and not any(item[2] for item in history[:2]))):
        hold = "This repeats recent coverage or follows two maintenance deliveries."
    elif not hold and not added and touched - before.keys():
        hold = "The new folder has no completed archive entry."
    if hold:
        print(hold)
        if not reason.strip():
            print("Choose a fresh reader question or document the editorial exception in the PR.")
            return 1
        print("Editorial exception for review | " + reason.strip())
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="origin/main", help="base commit for history and comparison")
    parser.add_argument("--head", default="", help="exact proposed commit (default: staged index)")
    parser.add_argument("--exception", default="", help="specific reader harm, claimed draft, or sourcing constraint")
    args = parser.parse_args()
    try:
        base_sha = git("rev-parse", "--verify", "--end-of-options", args.base + "^{commit}").strip()
        head_sha = git("rev-parse", "--verify", "--end-of-options", args.head + "^{commit}").strip() if args.head else ""
        subprocess.run(["git", "merge-base", "--is-ancestor", base_sha, head_sha or "HEAD"], check=True)
        sys.exit(check(base_sha, head_sha, args.exception))
    except (subprocess.CalledProcessError, ValueError) as error:
        sys.exit(f"Coverage check could not validate the proposal: {error}")
