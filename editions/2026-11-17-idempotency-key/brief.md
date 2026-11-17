# Why can retrying one request create two orders?

[Front page](../../README.md) · [Resource index](../../archive.md)

**Engineering / The Builder's Workbench · APIs · Edition 2026-11-17 · Foundation with current draft context**

Visual brief: 4 minutes · Optional practice: 15 minutes

> **The takeaway:** A timeout says only that no response arrived—not whether the server committed the order. Retrying a create request with a new identity can duplicate the effect. Reuse one scoped idempotency key for the same intent; the server must bind that key, request fingerprint and result atomically, then return the recorded outcome.

## Separate the reply from the effect

A server creates order `O-42`, but its reply is lost. “No reply” fits two stories: nothing happened, or the order exists. A blind retry can create `O-43`.

![A five-step timeline shows a client sending one order intent with key K7, the server committing order O-42 and recording the result, the reply being lost, and a retry with K7 returning O-42 instead of creating another order. Side notes show that a new key can duplicate the effect and a reused key with a changed payload must be rejected.](assets/retry-window.svg)

[Open the full-size timeline](assets/retry-window.svg). **Text equivalent:** The server records key `K7`, its request fingerprint and order `O-42`; the reply is lost. A retry with `K7` returns `O-42`. A new key can create another effect; changed content under `K7` is an error.

## Walk one example

An invented request contains two notebooks and standard shipping. The service commits `O-42` and records its response under `K7`; the connection drops. Reusing `K7` returns `O-42`. Inventing `K8` can authorize another order.

This is an application-level guarantee. HTTP defines idempotent methods, but `POST` is not automatically safe to retry. The API must document and enforce the key contract.

## Keep this retry-contract card

1. **Scope:** bind the key to the authenticated caller and operation.
2. **Sameness:** define which request fields form the fingerprint.
3. **Atomicity:** record key and effect in one transaction or equivalent protocol.
4. **Lifecycle:** state retention, concurrent-request behavior and the stored response.
5. **Mismatch:** reject changed content; never treat the key as authentication.

**Limit:** Keys expire, downstream effects may escape the transaction, and concurrent duplicates need a documented policy. The cited IETF document is an active Internet-Draft, not an RFC or standard.

## Try and check

**Quick check:** A request timed out, the user still wants the same order, and the API supports idempotency keys. Should the retry generate a fresh key?

<details>
<summary>Reveal the answer</summary>

No. Reuse the original key for the same intent. If the intent changed, reconcile the earlier attempt before using a new key.

</details>

## Keep exploring

Compare [RFC 9110’s method semantics](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) with the proposed [IETF Idempotency-Key contract](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/).

[Full illustrated guide and retry-contract worksheet](index.html) · [Evidence and limitations](sources.md)
