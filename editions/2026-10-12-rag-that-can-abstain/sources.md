# Evidence and source ledger — RAG that knows when to say “I don't know”

- Edition date in America/Chicago: **2026-10-12**
- Source access/check date: **2026-10-12**
- Editorial classification: **foundation with 2026 product-documentation context**; not a breaking-news announcement.
- Example customer policies, SKUs, corpus, ranks, scores and outputs are **invented teaching examples**, not empirical benchmarks or representations of any real company.

| Claim / article reference | Status | Dated primary source | Publication/update date | Access date | What it does / does not establish |
| --- | --- | --- | --- | --- | --- |
| [1] Azure AI Search hybrid requests combine full-text and vector queries and use reciprocal rank fusion; exact identifiers often benefit from text search. | **Documented service behavior** | [Microsoft Learn: Hybrid search overview](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview) | **2026-08-31** (last-updated label) | 2026-10-12 | Confirms Azure service mechanism, not performance on this hypothetical corpus. |
| [2] RRF sums reciprocal rank contributions `1/(rank + k)`; documentation gives illustrative constant 60. | **Documented scoring formula** | [Microsoft Learn: Hybrid search ranking](https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking) | No verified publication date in retrieved page; **undated/updated online** | 2026-10-12 | Scores in our table are exact arithmetic for **invented ranks**, not observed Azure scores. |
| [3] Search result retrieval quality should be evaluated using measures such as precision@k, recall@k and MRR, with positive and negative queries; reranking adds time. | **Engineering guidance** | [Azure Architecture Center: RAG information retrieval](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-information-retrieval) | Page updated online; exact date not independently verified | 2026-10-12 | Guidance for designing an evaluation, not evidence that the included three-document toy demo is production-ready. |
| [4] Retrieved external content can induce indirect prompt injection; RAG is not a complete mitigation. | **Documented security risk** | [OWASP Top 10 for LLM Applications v2025, LLM01 Prompt Injection](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf) | **2025 edition** | 2026-10-12 | Motivates treating retrieved text as data and enforcing privileged actions in code. |
| [5] Azure documentation distinguishes classic RAG from agentic retrieval with planning, knowledge sources and structured source references. | **Vendor-documented capability** | [Microsoft Learn: RAG in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview) | Current online documentation; precise updated date not independently verified | 2026-10-12 | Product availability, regional rollout, cost and model access can vary; check before relying on deployment. |
| [6] NIST's Generative AI Profile identifies risks and practices for generative-AI lifecycle risk management. | **Published risk framework** | [NIST AI 600-1, Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | **2024-07-26**, NIST page subsequently updated 2026-04-08 | 2026-10-12 | Framework guidance, not proof of the security of any individual application. |

## Technical assertions validated locally

- `offline_rag_lab.py` uses **Python standard library only** and performs lexical token-overlap retrieval, not embeddings, vector search, semantic ranking, Azure AI Search or LLM generation.
- `test_offline_rag_lab.py` checks supported evidence, unanswerable questions, permission-filtered corpus, empty corpus and a suspicious query. Passing the tests establishes only those sample invariants, **not general prompt-injection defense**.
- The formula/example `1/62 + 1/61 ≈ 0.0325` can be recalculated without network access.
- No API keys, uploaded data, paid services, telemetry, external fonts, scripts or cloud deployment are required by this edition.

## Editor's uncertainty notes

- Microsoft documentation is updated continuously. This article's classification and citation ledger reflect what was observed on 2026-10-12, not a guarantee of future feature naming, billing or regional support.
- A production system needs tenant isolation, doc versioning, safe chunk preprocessing, stronger retrieval, empirical thresholds, adversarial evaluation, privacy controls, monitoring and rollback beyond this lab.
- OWASP identifies a security class; this educational toy's suspicious-query unit test is not a certification against the wider class.