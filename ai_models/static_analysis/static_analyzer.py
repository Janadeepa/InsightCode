import ast

class StaticAnalyzer:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def analyze_code(self, code):
        tree = ast.parse(code)
        errors = []
        for rule in self.rules:
            errors.extend(rule.check(tree))
        return errors

class Rule:
    def check(self, tree):
        # Example rule that finds all function definitions
        return [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

# Example usage:
# analyzer = StaticAnalyzer()
# analyzer.add_rule(Rule())
# code = '''
# def example_function():
#     pass
# '''
# print(analyzer.analyze_code(code))
