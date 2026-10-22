
def extract_policy_number(document: dict) -> str:
    """Extract a policy number from structured document data."""
    return document.get("policy_number", "")


def test_extract_policy_number():
    document = {"policy_number": "POL-12345"}
    result = extract_policy_number(document)

    assert result == "POL-12345"


def test_missing_policy_number():
    document = {}
    result = extract_policy_number(document)

    assert result == ""
