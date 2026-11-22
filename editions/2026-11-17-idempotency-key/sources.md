# Sources and claim ledger — safe API retries

- Primary category / established track: Engineering / The Builder's Workbench
- Topic: APIs
- Reading layers: [Visual brief](brief.md) · [Full guide](index.html)
- Edition title: Why can retrying one request create two orders?
- Reporting as of (America/Chicago): 2026-11-17
- Last fact checked: 2026-11-17

| Claim or section | Status | Primary source URL | Source publication/update date | Access date | Notes, competing evidence and uncertainty |
| --- | --- | --- | --- | --- | --- |
| HTTP method idempotency concerns the intended server effect of multiple identical requests; safe methods, PUT and DELETE are idempotent; a client should not automatically retry a non-idempotent request unless it knows the semantics are idempotent or the first request was not applied | Confirmed Internet Standard | [RFC 9110 §9.2.2 — Idempotent Methods](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) | Published 2022-06 | 2026-11-17 | This is the HTTP method-level rule. It does not by itself give every POST request application-level idempotency. |
| An idempotency key identifies retries; clients should not reuse one key with a different payload; servers define expiry, fingerprinting and lifecycle; a completed duplicate returns a consistent result while a concurrent duplicate needs explicit handling | Active standards work, not an RFC | [IETF HTTPAPI Working Group — The Idempotency-Key HTTP Header Field, draft-08](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/) | Updated 2026-10-22; expires 2027-04-25 | 2026-11-17 | Internet-Drafts are works in progress. Clients cannot assume a server honors this header. The draft describes 409 for a concurrent duplicate and 422 for a mismatched payload; an API must publish its actual contract. |
| Caller-provided request identifiers can make ambiguous retries safer; the identifier and mutating operation need an atomic or equivalent recovery boundary; changed parameters under one identifier should be rejected; retention is finite | Confirmed industry implementation guidance | [AWS Builders’ Library — Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) | Undated article | 2026-11-17 | This is AWS design guidance, not a standard. Other systems can use different storage, conflict and retention policies while preserving the same invariant. |

## Worked-example status

Order `O-42`, keys `K7` and `K8`, and the two-notebook request are invented teaching examples. They illustrate the cited ambiguity and identity rules; they are not an API contract or evidence about a real transaction.

## Artifacts and validation

- Visual: `assets/retry-window.svg`; original conceptual timeline. It includes a title, description, adjacent text equivalent and labels that do not rely on color alone.
- Practice: `index.html#try`; a 15-minute retry-contract worksheet covering scope, fingerprint, atomicity, response, retention, concurrency and mismatch handling.
- Review: sequential pre-draft and final review from facts, domain, teaching, accessibility/design and safety/minimalism perspectives.
- Checks actually run: recorded in the delivery PR. Static validation does not establish screen-reader behavior; browser, narrow-layout, keyboard and zoom checks are reported separately.

**Limit:** Idempotency keys do not replace authentication, authorization, reconciliation, transaction design or downstream deduplication. Expired keys, partial side effects and undocumented server behavior remain failure boundaries.
