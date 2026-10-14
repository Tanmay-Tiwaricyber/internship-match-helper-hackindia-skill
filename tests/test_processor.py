import unittest
from processor import build_matches, clean_text


class ProcessorTests(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text("  PyThOn   "), "python")

    def test_matches_are_ranked(self):
        payload = {
            "students": [{"id": "S1", "name": "Test", "skills": ["Python", "SQL"]}],
            "internships": [
                {"id": "I1", "title": "Partial", "required_skills": ["Python", "Git"]},
                {"id": "I2", "title": "Perfect", "required_skills": ["Python", "SQL"]},
            ],
        }
        result = build_matches(payload)
        matches = result["students"][0]["matches"]
        self.assertEqual(matches[0]["title"], "Perfect")
        self.assertEqual(matches[0]["match_score"], 100)
        self.assertEqual(matches[1]["match_score"], 50)


if __name__ == "__main__":
    unittest.main()
