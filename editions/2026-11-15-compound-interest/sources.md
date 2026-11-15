# Sources and claim ledger — interest on interest

- Primary category / established track: Work & money / Career & Independence
- Topic: Financial literacy
- Reading layers: [Visual brief](brief.md) · [Full guide](index.html)
- Edition title: Where does interest on interest come from?
- Reporting as of (America/Chicago): 2026-11-15
- Last fact checked: 2026-11-15

| Claim or section | Status | Primary source URL | Source publication/update date | Access date | Notes, competing evidence and uncertainty |
| --- | --- | --- | --- | --- | --- |
| Compound interest earns interest on principal and previously earned interest; principal, rate and compounding frequency drive the example | Confirmed consumer explanation | [Consumer Financial Protection Bureau — How does compound interest work?](https://www.consumerfinance.gov/ask-cfpb/how-does-compound-interest-work-en-1683/) | Last reviewed 2023-10-19 | 2026-11-15 | CFPB’s first two years use the same invented $1,000 and 5% annual example. The third year in this edition is arithmetic derived from those stated inputs. |
| A calculator needs initial amount, contributions, time, estimated annual rate and compounding frequency | Confirmed tool behavior | [Investor.gov — Compound Interest Calculator](https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator) | Undated interactive tool | 2026-11-15 | Investor.gov labels the rate as estimated. Calculator output is a scenario, not a promised return. |
| For deposit disclosures, an interest rate does not reflect compounding; APY is an annualized relationship between interest earned and principal under stated assumptions | Confirmed regulation | [CFPB — Regulation DD, Appendix A: Annual Percentage Yield Calculation](https://www.consumerfinance.gov/rules-policy/regulations/1030/a/) | Regulation most recently amended 2023-04-19 | 2026-11-15 | The regulation contains special rules for tiered, stepped and time accounts. The brief does not reproduce those product-specific cases. |
| Interest is added to principal before a later interest calculation | Confirmed beginner explanation | [FDIC — Chapter 5: Compound Interest](https://www.fdic.gov/consumer-resource-center/chapter-5-compound-interest) | Last updated 2023-10-25 | 2026-11-15 | FDIC’s youth example compounds monthly; this edition instead uses annual compounding so the comparison remains inspectable by hand. |

## Worked-example arithmetic

The example is invented and assumes a fixed 5% rate compounded once per year, no deposits, no withdrawals, no fees, no taxes and no inflation adjustment.

- Simple balance after three years: $1,000 + (3 × $1,000 × 0.05) = $1,150.
- Compound balance before display rounding: $1,000 × 1.05³ = $1,157.625.
- Displayed compound balance: $1,157.63.
- Displayed difference: $7.63.

## Artifacts and validation

- Visual: assets/growth-paths.svg; original conceptual comparison with invented values. It labels every year and supplies a title, description and adjacent text equivalent.
- Practice: index.html#try; a 20-minute hand calculation and one-input-at-a-time calculator comparison. Expected result: a reproducible rate card with explicit exclusions.
- Review: sequential pre-draft and final review from facts, domain, teaching, accessibility/design and safety/minimalism perspectives.
- Checks actually run: recorded in the delivery PR. Static validation does not establish screen-reader behavior. Browser, viewport, keyboard and zoom checks are reported separately rather than inferred.

**Limit:** This edition teaches arithmetic and disclosure vocabulary. It does not compare current products, predict investment returns, account for individual taxes or fees, or recommend a transaction.
