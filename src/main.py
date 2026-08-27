from document_loader import load_documents
from semantic_search import search_documents_semantically


def main():
    """Run the application."""
    documents = load_documents()
    print(f"Loaded {len(documents)} documents.")

    query = input("\nAsk a question: ").strip()

    if not query:
        print("Question cannot be empty.")
        return

    results = search_documents_semantically(query, documents)

    if not results:
        print("\nNo relevant documents found.")
        return

    best_result = results[0]

    print("\nBest matching document:")
    print(f"File: {best_result['filename']}")
    print(f"Similarity score: {best_result['score']:.3f}")
    print("\nDocument content:")
    print(best_result["content"])



if __name__ == "__main__":
    main()
    