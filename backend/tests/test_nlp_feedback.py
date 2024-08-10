import unittest
from app.models.nlp_feedback import generate_feedback

class TestNLPFeedback(unittest.TestCase):
    
    def test_generate_feedback(self):
        code = "def foo():\n    return 1"
        feedback = generate_feedback(code)
        self.assertIn("Good code quality", feedback)

if __name__ == '__main__':
    unittest.main()
