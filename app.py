from fastapi import FastAPI
from rule_engine import create_rule, evaluate_rule
from database import RULES_DB

app = FastAPI()

@app.post("/create-rule/")
def create_rule_endpoint(rule_string: str):
    rule_ast = create_rule(rule_string)
    rule_id = len(RULES_DB) + 1
    RULES_DB[rule_id] = rule_ast
    return {"rule_id": rule_id, "rule_ast": str(rule_ast)}

@app.post("/evaluate-rule/")
def evaluate_rule_endpoint(rule_id: int, user_data: dict):
    rule_ast = RULES_DB.get(rule_id)
    if not rule_ast:
        return {"error": "Rule not found"}

    result = evaluate_rule(rule_ast, user_data)
    return {"result": result}
