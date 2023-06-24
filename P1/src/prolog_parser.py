# src/prolog_parser.py

# src/prolog_parser.py
class Parser:
    def parse(self, expr):
        print(f"Parsing: {expr}")
        expr = expr.strip().replace(' ', '')

        if expr.endswith('.'):
            expr = expr[:-1]

        if expr[0] == '(' and expr[-1] == ')':
            expr = expr[1:-1]

        operator, rest = expr.split('(', 1)
        operator = operator.replace("'", "")  # Remove quotes from the operator
        rest = rest[:-1]
        print(f"Operator: {operator}, Rest: {rest}")

        operands = rest.split(',')
        if operator == '\\+':
            operands = [operands[0]]

        parsed_operands = []
        for operand in operands:
            if operand in ('true', 'false'):
                parsed_operands.append(operand)
            else:
                parsed_operands.append(self.parse(operand))

        return (operator, *parsed_operands)

