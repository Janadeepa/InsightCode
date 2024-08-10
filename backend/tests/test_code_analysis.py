import unittest
from app.models.code_analysis import analyze_code

class TestCodeAnalysis(unittest.TestCase):
    
    def test_analyze_code(self):
        code = "def foo():\n    return 1"
        result = analyze_code(code)
        self.assertEqual(result['quality_score'], 95)

if __name__ == '__main__':
    unittest.main()
