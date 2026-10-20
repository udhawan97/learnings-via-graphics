# Guardrails for scheduled ChatGPT runs

For Elf, Mobster, and the Delivery Supervisor working on this repository. Read this from the **current default branch** alongside [contributing](../CONTRIBUTING.md), [editorial standards](editorial-standards.md), [the resource index](../archive.md), and [delivery/recovery](default-branch-delivery.md). These rules reduce avoidable errors; they do not guarantee service availability or waive any required gate.

## 1. Start with the tools actually available

- Confirm repository identity, default-branch SHA, permissions, open work, and the current America/Chicago date. Use supported GitHub tools; do not assume the scheduled chat has the local Mac checkout, previous downloads, terminal, browser, installed skills, or another chat's private output.
- Read current tool schemas before calling them. A local `gh` command or Safari success does not prove the cloud connector supports that operation. Use branch search and commit comparison tools for branch names containing `/`; follow the delivery guide's supported-read routes.
- If a discovery or read endpoint is unsupported, record that once and use an available supported equivalent. If none exists, report the specific missing capability. Do not repeatedly call the same rejected endpoint, invent API names, install tooling, or enable Actions to manufacture a check.
- Preserve useful work on an authorized GitHub branch/PR when possible. A temporary file or attachment from an earlier run is not a dependable shared handoff.

## 2. Keep the edition small and visual

Use **one primary category + one topic**, chosen by the reader's outcome. Categories are Engineering / The Builder's Workbench; Frontier technology / The Horizon; Everyday life / Dad's Field Notes; Work & money / Career & Independence. Keep empty categories explicitly empty; never duplicate an edition to populate them.

A new edition uses `editions/_template/brief.md`, `index.html`, and `sources.md`: a 40–60-word takeaway, a 250–450-word visual brief with 1–2 explanatory graphics, a worked example, a usable artifact/checklist, a visible limitation, and one answered quick check. Full explanations and 15–30-minute practice are optional reading depth. Keep source evidence and important safety limits accessible from the brief. Estimate reading time separately from lab time.

Store original standalone SVGs in the edition's `assets/` and keep any inline/exported copies synchronized. Index every artifact through **Read / See / Try / Check** under one topic in `archive.md`. Update README links/counts when editions change. Prefer a real correction to existing work over an unnecessary new edition or recurring process rewrite.

## 3. Validate the exact proposed files

| Check | Required evidence |
| --- | --- |
| Navigation | Relative paths exist; fragments resolve; no duplicate IDs; archive and brief reach every artifact |
| Visual assets | SVG parses; meaningful title/description and adjacent text; exported copies match inline originals |
| Editorial | Brief fits the word budget; category/topic agree; examples, evidence dates, and limits are honest; no draft placeholders |
| Runnable examples | Run relevant existing tests in an available execution environment; report command, outcome, and scope |
| Rendering | Inspect available rendering for visual changes; separately report browser, width, keyboard/zoom checks actually performed |
| Final change | Inspect all new and changed files, not only tracked-file diffs; preserve unrelated work |

When a checkout and Python are available, run the relevant suite from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s editions/2026-10-12-rag-that-can-abstain -p 'test_*.py' -v
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s editions/2026-10-13-safe-saves -p 'test_*.py' -v
```

Do not hard-code historical test counts as acceptance criteria. With Git available, inspect `git status --short`, stage only scoped files, then check `git diff --cached --check` and the complete staged diff. New untracked files are absent from an ordinary `git diff`. Use blank paragraphs instead of trailing-space Markdown breaks. Quote shell arguments containing `?`, spaces, or other metacharacters; pass multiline PR bodies as structured text or a body file.

No terminal means **tests not run**, not tests passed. Static parsing does not prove browser appearance, keyboard access, or screen-reader behavior. A browser connection check does not prove page rendering. Bound browser calls using supported timeouts; after a stall, check state once if possible, release control, and stop that browser attempt. Do not bypass an administrator restriction. State missing visual checks; hold when a required gate or material correctness/safety concern depends on them. A nonvisual documentation correction does not require invented browser acceptance.

Use Graphify when available and required by the execution environment's instructions. Refresh an existing graph before publishing from that environment; report failures and follow its release gate. Cloud runs must not pretend a Mac-local ignored graph exists or create one merely to imitate local tooling. Graph output is navigation evidence, not correctness proof.

## 4. Finish, or leave a precise handoff

Apply the five editorial perspectives before drafting and to the final artifact; sequential review is allowed. Reserve the final part of the run for validation and delivery. Before any merge, re-read the exact head/base, diff, required reviews/checks, and deployment triggers. Merge only the reviewed head through supported, non-forced operations. Read back default-branch ancestry and final file contents.

On stale state or a transient failure, inspect current state before at most one justified retry. An ambiguous write needs read-back before retrying, to avoid duplicate commits/PRs. Auth failures, required reviews, and platform safety denials remain distinct blockers; never change API, branch, or repository to evade a denied action.

Report **verified default-branch landing**, **branch only**, **PR pending**, or **not persisted**, with the SHA/PR, actual checks, missing checks, exact failure if any, and one next action. Preserve Pages/Actions disabled and all deployment, review, and safety boundaries. Scheduled workers must not change schedules or task settings; the supervisor retains only its explicitly authorized prompt-correction scope.
