# Sources and claim ledger — Database index trade-offs

- Primary category / established track: `Engineering / The Builder's Workbench`
- Topic: `Databases`
- Reading layers: [Visual brief](brief.md) · [Full guide](index.html)
- Edition title: `Why can a database index speed up reads but slow down writes?`
- Reporting as of (America/Chicago): `2026-11-25`
- Last fact checked: `2026-11-25`

| Claim or section | Status | Primary source URL | Source publication/update date | Access date | Notes, competing evidence and uncertainty |
| --- | --- | --- | --- | --- | --- |
| A database can use an index to avoid scanning a whole table for a selective lookup; the planner may instead choose a sequential scan when it estimates that route is cheaper | Confirmed engine documentation | [PostgreSQL 18 — Indexes introduction](https://www.postgresql.org/docs/18/indexes-intro.html) | PostgreSQL 18 documentation; page undated, copyright 2026 | 2026-11-25 | Exact plan depends on statistics, operators, data distribution and engine cost settings. The edition makes no latency guarantee. |
| An index must be kept synchronized with table changes, adding overhead to data-manipulation operations; rarely used indexes can be counterproductive | Confirmed engine documentation | [PostgreSQL 18 — Indexes introduction](https://www.postgresql.org/docs/18/indexes-intro.html) | PostgreSQL 18 documentation; page undated, copyright 2026 | 2026-11-25 | Write overhead varies by index type, key width, workload and storage. |
| SQLite indexes hold ordered search columns plus row identifiers; statistics help its planner choose among indexes, and a longer multi-column index can make a prefix index redundant | Confirmed engine documentation | [SQLite — Query Planning](https://www.sqlite.org/queryplanner.html) | Page undated | 2026-11-25 | SQLite-specific representation and rules must not be assumed to describe every engine. |
| A covering or index-only scan can avoid fetching the base row only when the engine and query meet additional conditions; extra payload columns increase index size | Confirmed engine documentation | [PostgreSQL 19 — Index-only scans and covering indexes](https://www.postgresql.org/docs/current/indexes-index-only-scans.html) | PostgreSQL 19 released 2026-11-19; page undated | 2026-11-25 | PostgreSQL visibility rules mean a physically possible index-only scan is not always a win, especially for frequently changing data. |

## Worked-example status

The million-order table, email address, query, plan choices and timing worksheet are invented teaching examples. They contain no measured benchmark and no personal data.

## Artifacts and validation

- Visual: `assets/index-tradeoff.svg`; original conceptual comparison of a table scan, indexed lookup and write-maintenance path. It has a title, description, labels and adjacent text that does not rely on color.
- Practice: `index-decision-card.md`; a 20-minute worksheet covering query shape, selectivity, before/after plan evidence, writes, storage and build impact.
- Review: sequential pre-draft and exact-final review from facts, domain, teaching, accessibility/design, and safety/minimalism perspectives.
- Checks actually run: recorded in the delivery PR. Static parsing does not establish screen-reader behavior or appearance in every browser.

**Limit:** The lesson explains a trade-off, not a production prescription. Readers must use their engine's plan tools, representative data and safe index-build procedure.
