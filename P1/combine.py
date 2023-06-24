# evaluator.py ---------------------------------------------
# src/evaluator.py

class Evaluator:
    def evaluate(self, expr):
        if isinstance(expr, tuple):
            operator, *operands = expr
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
# parser.py ---------------------------------------------
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
# shell.py ---------------------------------------------
# src/shell.py

from parser import Parser
from evaluator import Evaluator

class Interactive:
    def __init__(self):
        self.parser = Parser()
        self.evaluator = Evaluator()

    def start_shell(self):
        print("Prolog Lite - P1 Shell\nEnter your Prolog queries or use built-in commands:")
        while True:
            command = input("Command: ")
            self.handle_command(command)

    def handle_command(self, command):
        command_parts = command.split(' ', 1)
        if command_parts[0] == 'load_file':
            if len(command_parts) > 1:
                self.load_file(command_parts[1])
            else:
                print("You must provide a filename.")
        else:
            self.evaluate_expression(command)

    def evaluate_expression(self, expr):
        try:
            parsed_expr = self.parser.parse(expr)
            result = self.evaluator.evaluate(parsed_expr)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Failed to evaluate expression. Error: {str(e)}")

    def load_file(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    self.evaluate_expression(line.strip())
        except Exception as e:
            print(f"Failed to load file. Error: {str(e)}")

if __name__ == "__main__":
    shell = Interactive()
    shell.start_shell()
