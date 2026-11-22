# Sources and claim ledger — Test isolation

- Primary category / established track: `Engineering / The Builder's Workbench`
- Topic: `Testing`
- Reading layers: [Visual brief](brief.md) · [Full guide](index.html)
- Edition title: `Why can a test pass alone but fail in the full suite?`
- Reporting as of (America/Chicago): `2026-11-21`
- Last fact checked: `2026-11-21`

| Claim or section | Status | Primary source URL | Source publication/update date | Access date | Notes, competing evidence and uncertainty |
| --- | --- | --- | --- | --- | --- |
| A flaky or order-dependent test often relies on uncontrolled system state; a previous test may fail to clean up, a later test may rely on that residue, and global state usually conflicts with parallel execution | Confirmed framework guidance | [pytest — Flaky tests](https://docs.pytest.org/en/stable/explanation/flaky.html) | Undated stable documentation | 2026-11-21 | Pytest describes several other causes, including strict timing or numeric assertions and thread-safety problems. The edition therefore treats order dependence as a hypothesis supported by a reproducible sequence, not a universal diagnosis. |
| Yield fixtures and finalizers provide explicit teardown; fixture scope determines how long a shared instance lives | Confirmed framework guidance | [pytest — How to use fixtures: teardown and scope](https://docs.pytest.org/en/stable/how-to/fixtures.html#teardown-cleanup-aka-fixture-finalization) | Undated stable documentation | 2026-11-21 | Exact cleanup guarantees and failure behavior depend on the chosen fixture pattern. Readers must verify their framework's control flow. |
| `setUp()` and `tearDown()` run for each `unittest.TestCase` method when setup succeeds; class/module shared fixtures can break isolation and require care | Confirmed standard-library documentation | [Python 3.15 — `unittest`](https://docs.python.org/3/library/unittest.html) | Python 3.15.2 documentation; page undated | 2026-11-21 | This is Python-specific evidence for per-test fixture ownership. Other frameworks use different names but expose analogous lifecycle boundaries. |
| Reproducing a test independently and checking initialization, cleanup and order assumptions are useful triage steps; arbitrary delays and retries can hide rather than repair the cause | Confirmed practitioner guidance | [Google Testing Blog — Test Flakiness, Part II](https://testing.googleblog.com/2021/03/test-flakiness-one-of-main-challenges.html) | 2021-03-24 | This is engineering guidance from Google, not a language standard. It covers additional environment, application and infrastructure causes beyond shared state. |

## Worked-example status

`test_enable_beta`, `test_discount_banner` and the shared feature flag are invented teaching examples. They illustrate the cited order-dependence mechanism; they are not measurements from a real codebase.

## Artifacts and validation

- Visual: `assets/test-order.svg`; original conceptual comparison of a clean run, leaked-state run and isolated run. It has a title, description, labeled states and adjacent text that does not rely on color.
- Practice: `worksheet.md`; a 20-minute isolation card with a smallest-sequence record, shared-boundary inventory, cleanup owner and verification matrix.
- Review: sequential pre-draft and exact-final review from facts, domain, teaching, accessibility/design, and safety/minimalism perspectives.
- Checks actually run: recorded in the delivery PR. Static parsing does not establish screen-reader behavior or appearance in every browser.

**Limit:** A suite-only failure can also arise from time, concurrency, resource contention, external services, random data, platform differences or an assertion that is too strict. The worksheet asks the reader to widen the hypothesis when a two-test sequence is not reproducible.
