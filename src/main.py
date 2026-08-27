from document_loader import load_documents
from search import search_documents


def main():
    """Run the application."""
    documents = load_documents()
    print(f"Loaded {len(documents)} documents.")

    query = input("\nAsk a question: ").strip()

    if not query:
        print("Question cannot be empty.")
        return

    results = search_documents(query, documents)

    if not results:
        print("\nNo relevant documents found.")
        return

    best_result = results[0]

    print("\nBest matching document:")
    print(f"File: {best_result['filename']}")
    print(f"Score: {best_result['score']}")
    print(f"Matching words: {', '.join(best_result['matching_terms'])}")
    print("\nDocument content:")
    print(best_result["content"])



if __name__ == "__main__":
    main()
    