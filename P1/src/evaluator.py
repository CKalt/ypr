# src/evaluator.py

class Evaluator:
    def evaluate(self, expr):
        print(f"Evaluating: {expr}")
        if isinstance(expr, tuple):
            operator, *operands = expr
            print(f"Operator: {operator}, Operands: {operands}")
            if operator == ',':
                return self.evaluate(operands[0]) and self.evaluate(operands[1])
            elif operator == ';':
                return self.evaluate(operands[0]) or self.evaluate(operands[1])
            elif operator == '\\+':
                return not self.evaluate(operands[0])
        else:
            # Operand is a constant.
            if expr == 'true':
                return True
            elif expr == 'false':
                return False
            else:
                raise ValueError(f"Invalid constant: {expr}")
