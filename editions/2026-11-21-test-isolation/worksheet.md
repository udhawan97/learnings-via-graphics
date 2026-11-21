# Test-isolation worksheet

[Visual brief](brief.md) · [Full guide](index.html) · [Evidence](sources.md)

Use this card for one test that passes alone but fails in a suite. Replace the bracketed prompts; do not add retries while diagnosing.

## 1. Name the smallest sequence

- Observer test: `[test that fails]`
- Suspected predecessor: `[test that runs before it]`
- Alone result: `[pass/fail and command]`
- Predecessor → observer: `[pass/fail and command]`
- Observer → predecessor: `[pass/fail and command]`

## 2. Inventory shared boundaries

| Boundary | Starting state B expects | Who changes it? | Who restores it? |
| --- | --- | --- | --- |
| Process globals / singleton / feature flags |  |  |  |
| Environment / locale / timezone / clock |  |  |  |
| Files / temp paths / database / cache |  |  |  |
| Network ports / servers / queues / background work |  |  |  |
| Randomness / test doubles / framework hooks |  |  |  |

## 3. Make ownership explicit

- Setup creates: `[the exact state this test needs]`
- Cleanup runs through: `[fixture/finalizer/tearDown/defer mechanism]`
- Cleanup still runs after failure because: `[framework guarantee or verified control flow]`
- Broader-scoped state that remains: `[why sharing is safe, or how it is reset]`

## 4. Verification matrix

| Run | Expected after repair | Actual |
| --- | --- | --- |
| Observer alone | Pass |  |
| Predecessor alone | Pass |  |
| Predecessor → observer | Pass |  |
| Observer → predecessor | Pass |  |
| Full suite, no retry | Pass |  |

**Success:** every row passes from an intentionally prepared start, and the repair removes the shared-state dependency rather than fixing one test order.

**Stop and widen the hypothesis** if the smallest sequence is not repeatable. Record timing, parallelism, resource pressure and external-service evidence before changing production code.
