from rule_engine import create_rule, evaluate_rule

def test_create_rule():
    rule_string = "age > 30 AND salary > 50000"
    rule_ast = create_rule(rule_string)
    assert rule_ast is not None
    print("Rule AST:", rule_ast)

def test_evaluate_rule():
    rule_string = "age > 30 AND salary > 50000"
    rule_ast = create_rule(rule_string)

    user_data = {"age": 35, "salary": 60000}
    result = evaluate_rule(rule_ast, user_data)
    assert result == True  # Expecting True

    user_data = {"age": 25, "salary": 40000}
    result = evaluate_rule(rule_ast, user_data)
    assert result == False  # Expecting False

    user_data = {"age": 31, "salary": 51000}
    result = evaluate_rule(rule_ast, user_data)
    assert result == True  # Expecting True

    print("All evaluations completed successfully.")

if __name__ == "__main__":
    test_create_rule()
    test_evaluate_rule()
