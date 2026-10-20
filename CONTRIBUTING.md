# Make one useful visual edition

[Front page](README.md) · [Editorial standards](docs/editorial-standards.md) · [Starter files](editions/_template/)

**Scheduled ChatGPT runs:** start with the [run guardrails](docs/scheduled-run-guardrails.md); use current GitHub files and the capabilities available in that run.

## The short version

1. **Check existing work.** Read the [resource index](archive.md) and open PRs. Improve or finish a relevant existing edition before duplicating it.
2. **Choose one question and one home.** Assign a primary category and topic by the reader's intended outcome. Use the [category rules](docs/editorial-standards.md#choose-one-home).
3. **Sketch the explanation first.** Choose a process diagram, comparison, decision tree, annotated artifact, or evidence chart. Draft the takeaway and main limitation before prose.
4. **Build from the template.** Copy `editions/_template/` to `editions/YYYY-MM-DD-topic/`. Complete `brief.md`, `index.html`, and `sources.md`; add original SVGs in `assets/` and a useful lab, checklist, worksheet, or worked example. Remove every placeholder.
5. **Review twice.** Apply the handbook's five perspectives before drafting and to the exact finished files. Sequential review is acceptable; report it honestly.
6. **Verify and index.** Check local links, SVG labels, rendering, keyboard access, narrow layout, source claims, and runnable examples. Keep any copied inline/exported SVGs identical. Add one category entry in `archive.md` with every artifact; update the README's front page and counts when needed.
7. **Deliver through a scoped PR.** Follow the [delivery and recovery checklist](docs/default-branch-delivery.md). Honor required checks and reviews, verify the deployment trigger map, and read back `main` after merging.

## Done means

- [ ] The brief explains the idea without opening the full guide.
- [ ] The visual teaches a mechanism, comparison, decision, or evidence; adjacent text conveys the same information.
- [ ] One worked example, one useful artifact, one visible limitation, and a checkable next action are present.
- [ ] All edition resources are reachable from its single category entry.
- [ ] Evidence, test results, review method, and any unverified rendering are stated accurately in the PR.

**Publication boundary:** Reviewed repository files only. Keep Pages and Actions disabled. Tags, releases, hosted websites, and deployments need separate owner authorization; never bypass a gate to finish an edition.
