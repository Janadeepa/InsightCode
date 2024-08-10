rules = [
    # Define custom rules for code analysis here
    {
        "name": "Function Naming Rule",
        "description": "Functions should be named using snake_case",
        "check": lambda func_name: func_name.islower() and "_" in func_name
    },
    {
        "name": "No Debug Statements",
        "description": "Code should not contain debug print statements",
        "check": lambda code: "print(" not in code
    }
]

def get_rule_by_name(name):
    for rule in rules:
        if rule['name'] == name:
            return rule
    return None

# Example usage:
# rule = get_rule_by_name("Function Naming Rule")
# print(rule)
