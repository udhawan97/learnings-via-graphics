"""Dependency-free retrieval/abstention teaching demo. NOT an LLM or production RAG system.

Run: python3 offline_rag_lab.py
Test: python3 -m unittest -v test_offline_rag_lab.py
"""

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Document:
    doc_id: str
    title: str
    text: str


DOCUMENTS = (
    Document("POL-001", "Refund eligibility", "A customer may request a refund within 30 days of purchase. A receipt is required."),
    Document("POL-002", "Payment processing", "Approved refunds return to the original payment method within five to ten business days."),
    Document("ACC-003", "Account access", "To reset a password, request a reset link from the sign-in page."),
)

STOPWORDS = {"a", "an", "and", "are", "can", "do", "for", "from", "how", "i", "in", "is", "of", "on", "or", "our", "the", "to", "we", "what", "when", "within", "your"}
CLARIFY = "NEEDS CLARIFICATION — add a specific action or constraint to the question."


def tokens(text: str) -> set[str]:
    """Toy exact-word matching; real search engines need broader ranking."""
    return set(re.findall(r"[a-z0-9]+", text.lower())) - STOPWORDS


def retrieve(question: str, allowed_ids: set[str], *, min_overlap: int = 2):
    """Filter before scoring; abstain on weak or ambiguous top matches."""
    terms = tokens(question)
    eligible = [doc for doc in DOCUMENTS if doc.doc_id in allowed_ids]
    ranked = sorted(
        ((len(terms & tokens(doc.text + " " + doc.title)), doc) for doc in eligible),
        key=lambda item: (-item[0], item[1].doc_id),
    )
    if not ranked or ranked[0][0] < min_overlap:
        return None
    if len(ranked) > 1 and ranked[0][0] == ranked[1][0]:
        return None
    return ranked[0][1]


def answer(question: str, allowed_ids: set[str]) -> str:
    """Return evidence, request specificity, or abstain safely."""
    if len(tokens(question)) < 2:
        return CLARIFY
    match = retrieve(question, allowed_ids)
    if not match:
        return "NOT ENOUGH EVIDENCE — ask a human or search an authorized source."
    return f"EVIDENCE [{match.doc_id}] {match.text}"


if __name__ == "__main__":
    permitted = {doc.doc_id for doc in DOCUMENTS}
    for question in (
        "What is the refund request window?",
        "refund",
        "What is the enterprise contract cancellation penalty?",
    ):
        print(f"Q: {question}\nA: {answer(question, permitted)}\n")
