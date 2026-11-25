# Database-index decision card

[Visual brief](brief.md) · [Full guide](index.html) · [Evidence](sources.md)

Use this 20-minute worksheet before adding an index. Work from a representative query and data shape; do not change a production database just to complete the exercise.

## 1. Name the reader-visible problem

- Query or operation: ____________________________________________
- Slow or expensive symptom: ____________________________________
- Representative environment and data size: _____________________
- Success threshold: ____________________________________________

## 2. Describe the access pattern

| Question | Observation |
| --- | --- |
| Which columns filter or join rows? |  |
| Which columns order the result? |  |
| Which columns are returned? |  |
| Roughly what fraction of rows match? |  |
| How often does this table change? |  |

## 3. Predict, then inspect

- Predicted plan without the candidate index: ____________________
- Candidate key order and reason: ________________________________
- Existing index that may already cover this prefix: _____________
- Actual before-plan evidence: ___________________________________
- Actual after-plan evidence in a safe test environment: __________

## 4. Count both sides

| Evidence | Before | After |
| --- | --- | --- |
| Representative read work or latency |  |  |
| Representative insert/update work or latency |  |  |
| Index storage |  |  |
| Build/lock impact |  |  |

**Decision:** keep, revise or remove the candidate index because ________________.

**Stop:** If you cannot obtain a representative plan or safely reproduce the workload, record the evidence gap instead of declaring the index successful.
