from document_loader import load_documents
from search import search_documents


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


def evaluate_search():
    """Evaluate search quality using predefined questions."""
    documents = load_documents()
    passed_cases = 0

    for case_number, case in enumerate(EVALUATION_CASES, start=1):
        results = search_documents(case["query"], documents)

        if results:
            actual_filename = results[0]["filename"]
        else:
            actual_filename = None

        is_correct = actual_filename == case["expected_filename"]

        if is_correct:
            passed_cases += 1

        status = "PASS" if is_correct else "FAIL"

        print(f"\nCase {case_number}: {status}")
        print(f"Question: {case['query']}")
        print(f"Expected: {case['expected_filename']}")
        print(f"Actual: {actual_filename or 'No document found'}")

        if results:
            print(f"Score: {results[0]['score']}")
            print(f"Matching words: {', '.join(results[0]['matching_terms'])}")

    total_cases = len(EVALUATION_CASES)
    accuracy = passed_cases / total_cases * 100

    print("\nEvaluation summary:")
    print(f"Passed: {passed_cases}/{total_cases}")
    print(f"Accuracy: {accuracy:.1f}%")


if __name__ == "__main__":
    evaluate_search()
