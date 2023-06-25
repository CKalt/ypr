# src/evaluator.py ---------------------------------------------
# src/evaluator.py

class Evaluator:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def evaluate(self, expr):
        if self.verbose:
            print(f"Evaluating: {expr}")

        if isinstance(expr, tuple):
            operator, *operands = expr
            if self.verbose:
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
# src/prolog_parser.py ---------------------------------------------
# src/prolog_parser.py

# src/prolog_parser.py
class Parser:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def parse(self, expr):
        if self.verbose:
            print(f"Parsing: {expr}")
            
        expr = expr.strip().replace(' ', '')

        if expr.endswith('.'):
            expr = expr[:-1]

        if expr[0] == '(' and expr[-1] == ')':
            expr = expr[1:-1]

        operator, rest = expr.split('(', 1)
        operator = operator.replace("'", "")  # Remove quotes from the operator
        rest = rest[:-1]
        if self.verbose:
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

# src/shell.py ---------------------------------------------
# src/shell.py   
from prolog_parser import Parser
from evaluator import Evaluator
import sys

class Interactive:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.parser = Parser(verbose)
        self.evaluator = Evaluator(verbose)

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
    verbose = "-v" in sys.argv
    shell = Interactive(verbose)
    shell.start_shell()
