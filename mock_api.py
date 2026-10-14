"""Local mock API data source; no network calls or API key required."""


def get_internships(payload):
    """Return internships from the local mock payload."""
    internships = payload.get("internships", [])
    if not isinstance(internships, list):
        raise ValueError("'internships' must be a JSON list.")
    return internships
