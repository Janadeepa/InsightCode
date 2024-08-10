import unittest
from app.models import CodeAnalysis

class TestCodeAnalysis(unittest.TestCase):
    def test_code_analysis(self):
        code = "def hello_world():\n    print('Hello, World!')"
        analysis = CodeAnalysis(code)
        result = analysis.run()
        self.assertEqual(len(result), 0)

if __name__ == "__main__":
    unittest.main()
