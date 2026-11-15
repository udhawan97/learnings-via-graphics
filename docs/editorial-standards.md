# Write a visual brief, keep the depth

[Front page](../README.md) · [Contribution checklist](../CONTRIBUTING.md) · [Templates](../editions/_template/)

**Our promise:** Explain one useful question through a visual, a worked example, and something the reader can use. Be comprehensive about that question, not encyclopedic about the subject.

## Three reading layers

| Layer | Target | Required content |
| --- | --- | --- |
| Takeaway | 30 seconds; 40–60 words | What matters, the answer, and the most important boundary |
| Visual brief | 3–5 minutes; 250–450 prose words | 1–2 explanatory visuals, one worked example, one visible limitation, one reusable artifact or direct link, one quick check |
| Optional depth | Full guide; practice separately estimated at 15–30 minutes | Prerequisites, terms, alternatives, failure modes, three questions with answers, dated sources, and observable practice outcomes |

Put the mechanism before extended background. Count prose, captions, and checklists toward the brief budget; exclude code and source tables. Estimate time for diagram inspection too. Keep essential safety and uncertainty in the brief; only optional depth belongs behind links or disclosures. Do not shrink type to fit more text.

## Choose one home

Use **one primary category + one topic** consistently in the brief, full guide, ledger, and archive. Keep these four reader-facing names paired with the established track names:

| Category / track | Reader's main job | Example topics |
| --- | --- | --- |
| Engineering / The Builder's Workbench | Build, debug, secure, or operate a system | AI & retrieval; files & reliability; APIs; cloud; testing |
| Frontier technology / The Horizon | Understand a capability and judge its maturity | Chips; quantum; robotics; energy; infrastructure |
| Everyday life / Dad's Field Notes | Practice a useful everyday skill or decision | Home; communication; habits; nature; safety |
| Work & money / Career & Independence | Improve work, business, or financial judgment | Careers; portfolios; negotiation; business economics; financial literacy |

Classify by the **lesson's outcome**, not every noun it mentions. Implementing GPU inference belongs in Engineering; assessing chip capability belongs in Frontier technology; comparing a chip business model belongs in Work & money. A life analogy in a RAG guide does not make it an Everyday life edition.

Use an existing topic when it fits. Add a topic only for a completed edition; leave empty categories explicitly empty. Cross-link related lessons rather than duplicating archive entries. Keep dates and paths stable. Within each topic, list newest editions first.

## Choose the next newsletter story

Before committing editorial work, read the latest [newsletter issues and section index](../archive.md), open PRs and the last four changes to published lessons on the default branch. In the archive, give each edition one bold title linked to its brief beneath its section and topic headings. Count that title once. A lab repair, a reprint and a link from a second desk add zero editions to that count.

For an ordinary shift, pick a reader question in one of the sections with the fewest editions. Within those sections prefer a topic outside the last four lesson changes. State the new thing a beginner can do after reading. If the proposed work revisits a recent topic or follows two successive maintenance changes, give the next slot to a fresh story. A newly formatted diagram or a new folder name alone adds no reader outcome.

A specific unfinished edition already claimed by a contributor, a demonstrated error that misleads readers, a broken exercise or accessibility barrier can take priority. Identify the draft or show the reader’s failing step and expected result. If the least-covered section has no adequately sourced story ready, explain the evidence gap and the worthwhile alternative. Record the reason with the PR. Leave the shift without a commit when there is no useful, verifiable work.

**Run the coverage check from the repository root.** After fetching the current default branch, stage the complete proposal, including new files, and run `python3 scripts/check_coverage.py --base origin/main`. For a committed PR use `python3 scripts/check_coverage.py --base BASE_SHA --head HEAD_SHA` with its actual commits. The output gives section counts, recent topics and newly indexed editions. Use `--exception "specific reason and evidence"` for the editorial cases above. Verify the reason in review. If the base advances, reconcile the candidate and repeat on the new base.

**With GitHub access only,** read the archive and the files changed in the last four lesson deliveries on the first-parent history of the default branch. List sections with the lowest counts, the recent topics, and whether each delivery added an edition or maintained one. Compare those with the PR’s actual files, real new reader outcome and section. Apply the same exception rule and put the evidence in the PR template.

**Assemble a newsletter issue from completed stories.** Keep one home per lesson. Use `issues/YYYY-MM-DD.md` for a dated issue. Give at least two sections their own `## Section · Headline` heading, and link that section’s featured brief first beneath it. A labelled archive pick can follow. Feature at least one story outside the previous four issues, or explain the new teaching activity that makes a retrospective worthwhile. Give each story a plain-language question, a prediction or choice with an explained answer usable on GitHub, and a direct beginner resource with a reason to open it. Offer a written or local alternative when recommending video. Define the first unfamiliar term and keep equipment, accounts and downloads optional for the brief. Link the issue from the front page and archive. Reprints belong to their original edition date.

## Make the visual do the teaching

| Need to explain | Prefer |
| --- | --- |
| Sequence or causality | Labeled flow with inputs, outputs, and failure branches |
| A choice | Comparison or decision tree with concrete criteria |
| Change or maturity | Before/after states or a research → pilot → production ladder |
| Evidence | Chart with units, source, date, and uncertainty |
| A practical action | Annotated artifact, checklist, worksheet, or runnable lab |

Use original SVGs with accessible titles/descriptions and meaningful adjacent text. Save GitHub-readable versions in the edition's `assets/`; keep exports synchronized with inline originals. Label conceptual diagrams, invented examples, and measured results distinctly. Never invent chart values or imply measurements with decorative axes.

Use semantic HTML, legible type, descriptive links, visible keyboard focus, and responsive layouts. Test narrow screens and zoom; offer full-size diagrams and text equivalents. No remote scripts, tracking pixels, external fonts, or copied illustrations. Inspect actual rendering when available and report any gap.

## Evidence and scope

Keep a `sources.md` per edition: precise claim, evidence status, exact primary-source URL, publication/update date if known, access date, and limitations. Link claims from both reading layers to this ledger. Separate confirmed facts, prototypes, estimates/inferences, hypotheses, and evergreen foundations. Marketing is not independent verification.

For AI/cloud, use reproducible examples with explicit limits. For frontier technology, distinguish research from deployment. For money topics, explain mechanisms, alternatives, uncertainty, and falsifiable signals; do not manufacture prices or recommend transactions. For health/life topics, avoid universal promises and therapy claims; refer hazardous tasks to qualified professionals. Financial and health content is educational, not personalized advice.

## Review before drafting and before merging

Apply all five perspectives to the proposed outline, then again to the **exact final artifacts**:

- **Facts:** claim mapping, dates, numbers, and uncertainty.
- **Domain:** correct mechanism, terminology, boundaries, and counterexamples.
- **Teaching:** useful example, understandable visuals, and checkable practice.
- **Accessibility/design:** reading order, labels, contrast, keyboard, and narrow layout.
- **Safety/minimalism:** visible risks, privacy, no filler, and no unsupported claims.

Sequential review is acceptable; never claim independent reviewers participated unless they did. Hold publication when key claims or safety cannot be verified. Keep executed tests and browser checks separate from editorial judgments.

## Publication and delivery

Use the [contribution checklist](../CONTRIBUTING.md) and [delivery guide](default-branch-delivery.md). Merge the archive entry with the completed, reviewed edition; a draft or commit object is not a landed publication. Preserve checks, protections, and the verified no-deployment boundary. Pages, Actions, releases, tags, and deployments remain outside routine editorial work.

Once this repository is selected, Elf and Mobster follow the [story selection rule](#choose-the-next-newsletter-story) before committing. The 9 PM GitHub Delivery Supervisor may recover safe unfinished GitHub work and make evidence-backed prompt-only corrections for later runs, preserving schedules, timezone, enabled state, mission, and every safety/review/deployment boundary. Operational detail stays in the delivery guide.
