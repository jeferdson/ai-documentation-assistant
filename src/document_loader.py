from pathlib import Path


DOCUMENTS_DIR = Path(__file__).resolve().parent.parent / "data" / "documents"


def load_documents(directory: Path = DOCUMENTS_DIR) -> dict[str, str]:
    """Load all text documents from a directory."""
    if not directory.exists():
        raise FileNotFoundError(f"Document directory not found: {directory}")

    documents = {}

    for file_path in sorted(directory.glob("*.txt")):
        documents[file_path.name] = file_path.read_text(encoding="utf-8")

    return documents
