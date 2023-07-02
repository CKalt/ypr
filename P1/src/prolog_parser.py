from constants import Constants
from operators import Operators

class Parser:
    def __init__(self):
        self.constants = Constants().values
        self.operators = Operators()

    def parse(self, expression):
        parsed_expression = []
        index = 0
        while index < len(expression):
            char = expression[index]
            if char in self.constants:
                parsed_expression.append(self.constants[char])
                index += 1
            elif char in self.operators.keys():
                operator = char
                operands = []
                index += 2  # Skip the "(" following the operator
                while expression[index] != ")":
                    if expression[index] in self.constants:
                        operands.append(self.constants[expression[index]])
                    index += 2  # Skip the comma and whitespace after each operand
                index += 1  # Skip the ")" at the end of the tuple
                parsed_expression.append((operator, *operands))
            else:
                index += 1  # Skip over characters that are not constants or operators
        return parsed_expression
