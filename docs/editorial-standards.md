# Visual Field Guide Editorial Standard

## Promise

Every piece must answer five questions: **Why does it matter? How does it actually work? What can I do with it? Where can it fail? What should I learn next?**

## Source hygiene

- Anchor time-sensitive news in official documentation, release notes, primary research, trustworthy standards and source-dated reporting.
- Identify precisely what is **confirmed**, **experimental/prototype**, **estimated**, **hypothesized**, or **evergreen background**. Vendor marketing is not independent verification.
- For investing trends, teach mechanisms, bull/bear cases, uncertainty and falsifiable signals. Do not manufacture price movements or recommend transactions.
- For resilient living and mental performance, prefer grounded practices over universal promises. Distinguish nature metaphors from scientific evidence; refer hazardous/high-stakes tasks to qualified professionals.
- Keep a `sources.md` alongside every issue. For each important claim record the exact URL, original publication or update date when available, and accessed date.

## Teaching progression

1. One central question, clearly scoped, and a one-paragraph answer.
2. Prerequisites and glossary: assume curiosity, not expertise.
3. An accurate annotated visual model of the mechanism, including constraints and failure paths.
4. Real-life application or a worked example.
5. Explicit tradeoffs, failure modes, costs, safety and competing approaches.
6. A 15–30-minute exercise with observable success criteria.
7. Three quick questions with answers, a concise heuristic, and further reading.

For AI/cloud lessons, include a reproducible `Build / Test / Ship Safely` lab when feasible; never claim commands, tests or deployments happened unless observed. For chips/quantum, include a maturity ladder between lab demonstration, limited pilot and production deployment. For life skills, provide a practical checklist or decision tree instead of therapy claims.

## Visual and accessibility standards

- Semantic HTML, responsive layout, legible default typography, original inline SVG, accessible SVG title and description, and meaningful text explanation independent of color.
- No remote scripts, tracking pixels, external font dependencies, copied illustrations, fake quantitative axes or unsupported charts.
- Verify valid HTML/SVG and local paths; inspect actual rendered layout when a renderer is available. Note explicitly if visual inspection could not be done.

## Five-perspective council, both pre-draft and exact final artifact

- **Fact-checker:** source-to-claim mapping, dates, numerical accuracy, uncertainty.
- **Domain specialist:** mechanisms, terminology, counterexamples and trade-offs.
- **Educator:** scaffolded explanation, useful worked example, verifiable practice.
- **Graphic/accessibility reviewer:** hierarchy, layout, responsive behavior, labels.
- **Safety/minimalism:** risks, privacy, clarity, no misinformation, filler or dangerous instructions.

Do not claim independent specialists participated unless actually available; labeled sequential review is acceptable. Hold publication when key claims or safety cannot be verified.

## Merge and release boundary

A source commit or PR may be merged after checks/reviews and a verified no-deployment trigger map. GitHub Pages, published releases, or other public deployments require separately confirmed owner approval. Never enable deployment during routine editorial maintenance.

## Default-branch delivery is the success gate

Elf and Mobster must follow the [default-branch delivery and failed-write recovery guide](default-branch-delivery.md) before describing work as landed. Preparing a Git commit object without confirming its branch ref is **not** delivery. Recover independently useful stranded work before starting duplicate editions, require non-forced ref updates against verified heads, classify failures instead of bypassing safety denials, and read back `main` after an authorized PR merge. The 9 PM GitHub Delivery Supervisor may recover safe unfinished GitHub work and make evidence-backed prompt-only corrections to Elf or Mobster for later runs, while preserving their schedule, timezone, enabled state, mission, and every safety, review, and deployment boundary.
