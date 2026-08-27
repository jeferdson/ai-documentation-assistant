import re


STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "be",
    "can",
    "could",
    "do",
    "does",
    "for",
    "from",
    "has",
    "have",
    "how",
    "i",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "should",
    "that",
    "the",
    "this",
    "to",
    "was",
    "were",
    "what",
    "when",
    "where",
    "will",
    "with",
    "would",
    "you",
    "your",
}


def tokenize(text: str) -> set[str]:
    """Convert text into a set of meaningful lowercase words."""
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {word for word in words if word not in STOP_WORDS}


def search_documents(query: str, documents: dict[str, str]) -> list[dict]:
    """Rank documents by the number of words matching the query."""
    query_terms = tokenize(query)
    results = []

    for filename, content in documents.items():
        document_terms = tokenize(content)
        matching_terms = query_terms.intersection(document_terms)

        if matching_terms:
            results.append(
                {
                    "filename": filename,
                    "content": content,
                    "score": len(matching_terms),
                    "matching_terms": sorted(matching_terms),
                }
            )

#Разобрать лямбду!!!

    return sorted(results, key=lambda result: result["score"], reverse=True)
