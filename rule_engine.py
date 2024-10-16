class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # "operator" or "operand"
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value}, left={self.left}, right={self.right})"


def create_rule(rule_string):
    # Tokenization: handling parentheses and basic operators
    tokens = rule_string.replace("(", " ( ").replace(")", " ) ").split()
    stack = []
    
    def parse(tokens):
        if not tokens:
            return None

        token = tokens.pop(0)

        if token == '(':
            node = parse(tokens)
            if tokens and tokens[0] == ')':
                tokens.pop(0)  # pop the closing parenthesis
            return node
        elif token in {'AND', 'OR'}:
            left = stack.pop() if stack else None
            right = parse(tokens)
            return Node("operator", value=token, left=left, right=right)
        else:
            # Capture a complete condition (like "age > 30")
            if len(tokens) >= 2 and tokens[0] in {'>', '<', '='}:
                operator = tokens.pop(0)
                value = tokens.pop(0)
                condition = f"{token} {operator} {value}"
                stack.append(Node("operand", value=condition))
            else:
                stack.append(Node("operand", value=token))
            return None

    while tokens:
        parse(tokens)

    return stack[0] if stack else None


def evaluate_rule(ast, data):
    if ast.type == "operand":
        # Evaluate conditions like "age > 30"
        try:
            # Splitting conditions like "age > 30"
            condition_parts = ast.value.split()
            attribute = condition_parts[0]
            operator = condition_parts[1]
            value = int(condition_parts[2])
            user_value = data.get(attribute, 0)

            if operator == ">":
                return user_value > value
            elif operator == "<":
                return user_value < value
            elif operator == "=":
                return user_value == value
        except (IndexError, ValueError):
            return False
    elif ast.type == "operator":
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)
        if ast.value == "AND":
            return left_result and right_result
        elif ast.value == "OR":
            return left_result or right_result

    return False
