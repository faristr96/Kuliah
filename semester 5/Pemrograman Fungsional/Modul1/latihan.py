def minus (x, y):
    return x - y
result = minus(3, 5)
print(result)

def mult (x, y):
    return x * y
result = mult(3,3)
print(result)

def mult (x, y):
    return x / y
result = mult(12,3)
print(result)

def evaluate_expression_tree(expression_tree):
    if isinstance(expression_tree, tuple):
        left_operand = expression_tree[0]
        operator = expression_tree[1]
        right_operand = expression_tree[2]

        if operator == '+':
            return evaluate_expression_tree(left_operand) + evaluate_expression_tree(right_operand)
        elif operator == '-':
            return evaluate_expression_tree(left_operand) - evaluate_expression_tree(right_operand)
        elif operator == '*':
            return evaluate_expression_tree(left_operand) * evaluate_expression_tree(right_operand)
        elif operator == '/':
            return evaluate_expression_tree(left_operand) / evaluate_expression_tree(right_operand)
    else:
        return expression_tree  # Return numeric operands as is

expression_tree = ((2, '+', 3), '*', (5, '-', 1))
result = evaluate_expression_tree(expression_tree)
print("Hasil evaluasi pohon ekspresi:", result)