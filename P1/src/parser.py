# src/parser.py

class Parser:
    def parse(self, expr):
        # Remove whitespace and outermost parentheses.
        expr = expr.replace(' ', '')[1:-1]

        # Split into operator and rest.
        operator, rest = expr[0], expr[1:]

        # Parse the rest based on the operator.
        if operator == ',' or operator == ';':
            # Find the comma that separates the operands.
            comma = rest.find(',', 1)
            operand1 = self.parse(rest[:comma])
            operand2 = self.parse(rest[comma+1:])
            return (operator, operand1, operand2)
        elif operator == '\\':
            # Find the plus sign that follows the backslash.
            plus = rest.find('+')
            operand = self.parse(rest[plus+1:])
            return ('\\+', operand)
        else:
            # Operand is a constant.
            return expr
