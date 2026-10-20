# Read, explore, or practice

[Front page](../README.md) · [All resources by topic](../archive.md)

## Choose your depth

| Time available | Open | Leave with |
| --- | --- | --- |
| 30 seconds | The takeaway at the top of a brief | One useful idea and its main caveat |
| 3–5 minutes | Brief, diagrams, worked example | A mental model and reusable checklist |
| More time | Full illustrated guide | Foundations, alternatives, failure modes, and source context |
| 15–30 minutes | Optional lab or practice artifact | An observable result you can check |

Times are editorial estimates, including diagram inspection; lab time is separate. The two original full guides are longer than their new briefs.

## Open the illustrations

**On GitHub:** open a visual brief from the [resource index](../archive.md). Markdown displays the text and SVG diagrams together. Each brief also links a full-size diagram; its text explains the same mechanism without relying on color.

**Offline:** [download the ZIP](https://github.com/udhawan97/learnings-via-graphics/archive/refs/heads/main.zip), extract it, then open either file in your browser:

- `editions/2026-10-13-safe-saves/index.html`
- `editions/2026-10-12-rag-that-can-abstain/index.html`

The full HTML guides include their own styles and diagrams. Reading requires no server, Python, account, API key, or paid service. Source links lead to external sites. GitHub displays HTML as source, not as a hosted article.

## Run a lab

Requires **Python 3.10+**. Download and extract the ZIP, then open a terminal in the extracted repository folder. The labs use only the Python standard library.

### Files & reliability: Safe Saves

```sh
cd editions/2026-10-13-safe-saves
python3 save_lab.py
python3 -m unittest -v test_save_lab.py
```

Expected: an injected failure preserves Version A, a successful replacement writes Version B, and the tests pass. The directory-sync result can vary by platform. This is not a hardware power-loss test.

### AI & retrieval: RAG that can abstain

From a **new terminal at the repository root**:

```sh
cd editions/2026-10-12-rag-that-can-abstain
python3 offline_rag_lab.py
python3 -m unittest -v test_offline_rag_lab.py
```

Expected: the refund-window question cites `POL-001`, “refund” requests clarification, the unsupported contract question abstains, and the tests pass. The corpus is fictional; the lab does not call an LLM or implement vector search.

## Read the evidence

Every edition's `sources.md` maps claims to references and records dates and limitations. “Foundation” means a mechanism lesson, not today's news. Follow the source ledger before relying on time-sensitive product details.
