# Learnings via Graphics

**Field manuals for modern engineering, future technology, money skills, and capable living.**

A visual, practical knowledge library designed to teach *how things work*, *how to use them*, and *how to improve your judgment over time*. Original accessible diagrams, real examples, documented sources, and short exercises replace vague inspiration and recycled headlines.

## Start with the first field guide

**[RAG that knows when to say “I don't know”](editions/2026-10-12-rag-that-can-abstain/index.html)** — October 12, 2026 · The Builder's Workbench

Learn how to retrieve authorized evidence, combine keyword and vector search, cite sources, and abstain when an answer is unsupported. The guide includes two original diagrams, a worked ranking example, an 18-minute offline Python exercise, and three questions with answer guidance.

- [Read the source ledger](editions/2026-10-12-rag-that-can-abstain/sources.md) for dated references and limitations.
- [Inspect the teaching lab](editions/2026-10-12-rag-that-can-abstain/offline_rag_lab.py) and its [five tests](editions/2026-10-12-rag-that-can-abstain/test_offline_rag_lab.py).
- [Browse all completed editions](archive.md).

**[Safe Saves: atomic replacement vs durability](editions/2026-10-13-safe-saves/index.html)** — October 13, 2026 · The Builder's Workbench

Understand why an atomic rename is not a durability guarantee, with original diagrams, a 20-minute no-dependency Python lab and five failure-focused tests. [Read the source ledger](editions/2026-10-13-safe-saves/sources.md) or [inspect the lab](editions/2026-10-13-safe-saves/save_lab.py).

## Open the illustrated layout

GitHub displays the lesson's HTML source. To read the diagrams and full layout of either field guide:

1. [Download the repository ZIP](https://github.com/udhawan97/learnings-via-graphics/archive/refs/heads/main.zip), or select **Code → Download ZIP** on this repository.
2. Extract the ZIP and open `editions/2026-10-12-rag-that-can-abstain/index.html` in your browser.
3. Open the HTML file in either edition directory and follow its exercise and knowledge-check answers.

The lesson renders locally without a server, account, API key, or paid service. Its source references open external documentation when clicked. GitHub Pages is disabled; there is no hosted lesson website.

### Run the offline lab

Requires **Python 3.10+** and Git for the clone command. Alternatively, download and extract the ZIP, then open a terminal in the edition's folder.

```sh
git clone https://github.com/udhawan97/learnings-via-graphics.git
cd learnings-via-graphics/editions/2026-10-12-rag-that-can-abstain
python3 offline_rag_lab.py
python3 -m unittest -v test_offline_rag_lab.py
```

Expected result: the refund-window question cites `POL-001`, the unsupported contract question abstains, and all five tests pass. This standard-library example demonstrates lexical retrieval and permission filtering; it does not call an LLM or implement production RAG. The small test suite does not establish general prompt-injection protection.

## Four tracks

| Track | What you'll learn | What you'll do |
| --- | --- | --- |
| **The Builder's Workbench** | AI engineering, agents/RAG, evaluations, system design, cloud platforms, APIs, debugging, CI/CD | Build, test, secure, and ship a small real product |
| **The Horizon** | Quantum computing, chips, GPUs, semiconductor manufacturing, robotics, energy, infrastructure and market structure | Distinguish experiments from real deployments and evaluate evidence |
| **Dad's Field Notes** | Practical home/life judgment, resilience, communication, nature, mental focus, safety, habits | Practice a concrete checklist or decision-making skill |
| **Career & Independence** | Work-ready skills, portfolios, freelancing, product economics, negotiation and long-term financial literacy | Make one verifiable, useful improvement to your capabilities |

## Reading an edition

Browse [the archive](archive.md). Each edition teaches one central question from fundamentals to real-world application, with sourced claims, diagrams, failure modes, a practical exercise, three knowledge-check questions and next-step reading.

## Editorial standards

Read [the editorial handbook](docs/editorial-standards.md). Current releases and developments must be distinguished from prototypes, speculation and evergreen foundations. Financial and health content is educational, not personalized professional advice.

## Repository conventions

- `editions/YYYY-MM-DD-<topic>/index.html`: self-contained responsive article with semantic HTML, local CSS and original accessible SVG illustrations.
- `editions/YYYY-MM-DD-<topic>/sources.md`: sources linked to specific time-sensitive claims, including publication dates and access dates.
- `editions/_template/`: reusable starter for each new edition.
- `archive.md`: one entry per completed, reviewed edition; never include unmerged drafts as published.

## Contribution workflow

**Operational reliability:** Elf and Mobster use the [default-branch delivery and failed-write recovery checklist](docs/default-branch-delivery.md) to finish stranded work, distinguish commit objects from landed changes, and verify the actual default-branch SHA. The 9 PM GitHub Delivery Supervisor may recover safe unfinished GitHub work and make evidence-backed prompt-only corrections to Elf or Mobster for later runs. It must preserve their schedule, timezone, enabled state, mission, and every safety, review, and deployment boundary.


1. Check the current archive and active PRs to prevent duplicates.
2. Research primary sources and design one independently useful lesson.
3. Review across facts, domain knowledge, pedagogy, accessibility/design, and safety.
4. Verify internal links, markup and (when available) browser rendering and practical examples.
5. Open one scoped PR, wait for required checks, then merge only when no public deployment or release is triggered without the owner's authorization.

Elf and Mobster maintain this library using the editorial handbook, existing templates, and a shared archive. They should resume an existing edition before creating a competing PR, and add an archive entry only for completed, reviewed work that lands on `main`.

**Repository publication means committing reviewed source to GitHub. GitHub Pages and Actions remain disabled; releases, release tags, hosted websites, and automated deployments are not part of this workflow.** Do not enable Actions to obtain checks for an edition; honor any configured checks and protections, and hold the PR when a required gate cannot be satisfied.
