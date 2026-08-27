from document_loader import load_documents
from search import search_documents
from semantic_search import search_documents_semantically


EVALUATION_CASES = [
    {
        "query": "Can I delete an active project?",
        "expected_filename": "project_statuses.txt",
    },
    {
        "query": "How do I return equipment?",
        "expected_filename": "equipment_returns.txt",
    },
    {
        "query": "When does a crew member receive a notification?",
        "expected_filename": "crew_scheduling.txt",
    },
    {
        "query": "What should workers do with broken gear?",
        "expected_filename": "equipment_returns.txt",
    },
]


def evaluate_search(search_name, search_function):
    """Evaluate search quality using predefined questions."""
    documents = load_documents()
    passed_cases = 0

    print(f"\n=== {search_name} ===")

    for case_number, case in enumerate(EVALUATION_CASES, start=1):
        results = search_function(case["query"], documents)

        actual_filename = (
           results[0]["filename"] if results else None
       )

        is_correct = actual_filename == case["expected_filename"]

        if is_correct:
            passed_cases += 1

        status = "PASS" if is_correct else "FAIL"

        print(f"\nCase {case_number}: {status}")
        print(f"Question: {case['query']}")
        print(f"Expected: {case['expected_filename']}")
        print(f"Actual: {actual_filename or 'No document found'}")

    total_cases = len(EVALUATION_CASES)
    accuracy = passed_cases / total_cases * 100

    print(f"\n{search_name} summary:")
    print(f"Passed: {passed_cases}/{total_cases}")
    print(f"Accuracy: {accuracy:.1f}%")

    return accuracy


def main():
    """Compare keyword and semantic search quality."""
    keyword_accuracy = evaluate_search(
        "Keyword search",
        search_documents,
    )

    semantic_accuracy = evaluate_search(
        "Semantic search",
        search_documents_semantically
    )

    print("\n=== Comparison ===")
    print(f"Keyword search: {keyword_accuracy:.1f}%")
    print(f"Semantic search: {semantic_accuracy:.1f}%")


if __name__ == "__main__":
    main()
