from sentence_transformers import SentenceTransformer


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

MODEL = SentenceTransformer(MODEL_NAME)


def search_documents_semantically(
    query: str,
    documents: dict[str, str],
) -> list[dict]:
    """Rank documents by semantic similarity to the query."""
    if not documents:
        return []

    filenames = list(documents.keys())
    contents = list(documents.values())

    query_embedding = MODEL.encode([query])
    document_embeddings = MODEL.encode(contents)

    similarity_scores = MODEL.similarity(
        query_embedding,
        document_embeddings,
    )[0]

    results = []

    for filename, content, score in zip(
        filenames,
        contents,
        similarity_scores,
    ):
        results.append(
            {
                "filename": filename,
                "content": content,
                "score": score.item(),
            }
        )

    return sorted(
        results,
        key=lambda result: result["score"],
        reverse=True,
    )
