# Sources and claim ledger — Reading a pay stub

- Primary category / established track: `Work & money / Career & Independence`
- Topic: `Pay & benefits`
- Reading layers: [Visual brief](brief.md) · [Full guide](index.html)
- Edition title: `Where did the rest of my paycheck go?`
- Reporting as of (America/Chicago): `2026-11-23`
- Last fact checked: `2026-11-23`

| Claim or section | Status (confirmed/prototype/inference/foundation) | Primary source URL | Source publication/update date | Access date | Notes, competing evidence and uncertainty |
| --- | --- | --- | --- | --- | --- |
| Gross income is money earned before deductions; net income or take-home pay is what remains after deductions. A pay stub reports earnings, pay period and subtractions. | Foundation | [Consumer Financial Protection Bureau: Understanding taxes and your paycheck](https://www.consumerfinance.gov/consumer-tools/educator-tools/youth-financial-education/teach/activities/understanding-taxes-paycheck/) | Updated 2022-11-17 | 2026-11-23 | The page is a U.S. classroom activity. Employers may use different labels and statement layouts. |
| Federal income-tax withholding is money an employer withholds from pay; the amount depends on earnings and Form W-4 information. Withholding can differ from final tax liability. | Confirmed federal guidance | [Internal Revenue Service: Tax withholding](https://www.irs.gov/payments/tax-withholding) | Undated living guidance | 2026-11-23 | The IRS estimator covers federal income-tax withholding, not every payroll tax, state or local tax, benefit or deduction. |
| Covered employers’ required records include wage basis, earnings, additions or deductions, total wages, payment date and pay period. | Confirmed federal recordkeeping guidance | [U.S. Department of Labor: Fact Sheet #21](https://www.dol.gov/agencies/whd/fact-sheets/21-flsa-recordkeeping) | Revised July 2008 | 2026-11-23 | The FLSA does not require a particular record form. This lesson does not claim that federal law requires every worker to receive a pay stub; state rules may add requirements. |
| A current amount covers one pay period while a year-to-date amount accumulates across the year. | Foundation | [IRS: Tax Withholding Estimator FAQs](https://www.irs.gov/individuals/tax-withholding-estimator-faqs) | Undated living guidance | 2026-11-23 | The FAQ distinguishes federal tax withheld for one pay period from total withholding so far. Pay-stub labels vary. |
| The $2,000 → $1,450 flow and all intermediate values | Invented example | [Pay-stub flow](assets/pay-stub-flow.svg) | 2026-11-23 | Deliberately fictional. It demonstrates reconciliation, not tax rates or the order used by a payroll system. The middle subtotal is not presented as a universal tax base. |

## Artifacts and validation

- Visuals: `assets/pay-stub-flow.svg`; original invented example. Title, description, alt text and adjacent prose identify gross pay, three subtractions, net pay and the model’s boundary.
- Practice: `pay-stub-review-card.md`; a private 20-minute worksheet. Success means current gross plus current additions minus current deductions reconciles with current net pay and every current addition or subtraction has an understood label or a payroll question.
- Review: sequential pre-draft and exact-final review from facts, domain, teaching, accessibility/design and safety/minimalism perspectives.
- Checks actually run: `python3 scripts/check_coverage.py --base origin/main` passed and selected a fresh `Pay & benefits` topic in the tied least-covered Work & money section. Both repository Python lab suites passed. Python parsing confirmed resolving local links and fragments, unique HTML IDs, valid SVG XML with a title and description, and no template placeholders. The 59-word takeaway and 373-word brief fit their editorial budgets. `git diff --cached --check` passed. The SVG was rendered through Inkscape and visually inspected after a label-fit correction. Local Chromium could not create its singleton socket (`Operation not permitted`), and the cloud browser’s URL policy rejected the local `file:` page; HTML browser appearance, keyboard, zoom and screen-reader acceptance remain unverified.

**Boundary:** This U.S.-focused educational lesson does not decide whether a deduction is lawful, calculate personalized tax or replace payroll, tax or legal advice. Keep account numbers, tax IDs, addresses and full statements private.
