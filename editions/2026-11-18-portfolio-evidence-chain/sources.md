# Sources and claim ledger — Portfolio evidence chain

- Primary category / established track: `Work & money / Career & Independence`
- Topic: `Portfolios`
- Reading layers: [Visual brief](brief.md) · [Full guide](index.html)
- Edition title: `What makes a portfolio case study believable?`
- Reporting as of (America/Chicago): `2026-11-18`
- Last fact checked: `2026-11-18`

| Claim or section | Status (confirmed/prototype/inference/foundation) | Primary source URL | Source publication/update date | Access date | Notes, competing evidence and uncertainty |
| --- | --- | --- | --- | --- | --- |
| Structured interview questions can elicit situation/task, action and result and should connect to job-related competencies. | Foundation | [U.S. Office of Personnel Management: creating structured interview questions](https://www.opm.gov/frequently-asked-questions/assessment-policy-faq/structured-interviews/how-do-i-create-structured-interview-questions) | Undated page; underlying OPM guide dated September 2008 | 2026-11-18 | The evidence-chain framework adapts this response structure; it is not an OPM portfolio standard. |
| GitHub profiles can highlight selected repositories, and project READMEs can expose features, setup, examples and tests. | Confirmed product behavior and product guidance | [GitHub Docs: Using your GitHub profile to enhance your resume](https://docs.github.com/en/account-and-profile/tutorials/using-your-github-profile-to-enhance-your-resume) | Undated, living documentation | 2026-11-18 | GitHub controls its product behavior. The page offers guidance, not evidence that a particular presentation causes hiring outcomes. |
| GitHub permits up to six combined pinned repositories and gists. | Confirmed product behavior | [GitHub Docs: Pinning items to your profile](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/pinning-items-to-your-profile) | Undated, living documentation | 2026-11-18 | Product limits may change; the lesson does not depend on the number. |
| Meaningful images need an appropriate text alternative; complex diagrams need their information conveyed elsewhere on the page. | Foundation | [W3C Web Accessibility Initiative: Images Tutorial](https://www.w3.org/WAI/tutorials/images/) | Undated, living tutorial | 2026-11-18 | The brief and guide provide adjacent text equivalents; visual inspection and screen-reader acceptance remain separate checks. |
| Context → decision → artifact → check, with scope and limit attached, is a useful way to draft a portfolio case study. | Editorial synthesis | [This edition’s diagram](assets/evidence-chain.svg) | 2026-11-18 | Original framework synthesized from the sources above. It has not been validated as a hiring rubric and should not be presented as one. |
| The checkout example and its 8/20 and 18/20 values | Invented example | [Worked example](index.html#example) | 2026-11-18 | Deliberately fictional. It demonstrates structure and must not be read as measured product evidence. |

## Artifacts and validation

- Visuals: `assets/evidence-chain.svg`; original conceptual diagram. Its title, description, alt text and adjacent prose cover context, decision, artifact, check, scope and limit.
- Practice: the five-field evidence card in `index.html#try`; no account or download is required to copy it. Success means a reader can locate the decision, inspectable evidence and limitation.
- Review: sequential pre-draft and exact-final review from facts, domain, teaching, accessibility/design and safety/minimalism perspectives.
- Checks actually run: `python3 scripts/check_coverage.py --base origin/main` passed and selected the previously tied least-covered Work & money section on a fresh Portfolios topic. Both repository Python lab suites passed. Python parsing confirmed unique HTML IDs, resolving local links and fragments, valid SVG XML, and a 411-word brief under the editorial counting method. `git diff --cached --check` passed. Chromium rendering was attempted twice, but the execution environment denied its singleton socket (`Operation not permitted`); browser appearance, keyboard, zoom and screen-reader acceptance remain unverified.

**Boundary:** This is educational career guidance, not an employer’s rubric, a hiring guarantee or personalized career advice. Do not disclose secrets, personal data or confidential work to make a portfolio claim inspectable.
