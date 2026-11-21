# Test-isolation worksheet

[Visual brief](brief.md) · [Full guide](index.html) · [Evidence](sources.md)

Use this card for one test that passes alone but fails in a suite. Write short notes on each blank; do not add retries while diagnosing.

## 1. Name the smallest sequence

- Observer test: ________________________________________________
- Suspected predecessor: ________________________________________
- Alone result and command: _____________________________________
- Predecessor → observer result and command: _____________________
- Observer → predecessor result and command: _____________________

## 2. Inventory shared boundaries

| Boundary | Starting state B expects | Who changes it? | Who restores it? |
| --- | --- | --- | --- |
| Process globals / singleton / feature flags |  |  |  |
| Environment / locale / timezone / clock |  |  |  |
| Files / temp paths / database / cache |  |  |  |
| Network ports / servers / queues / background work |  |  |  |
| Randomness / test doubles / framework hooks |  |  |  |

## 3. Make ownership explicit

- Setup creates: _________________________________________________
- Cleanup runs through: __________________________________________
- Cleanup still runs after failure because: _______________________
- Broader-scoped state that remains, and why it is safe: __________

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
