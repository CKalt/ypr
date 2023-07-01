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
        print("Prolog Lite - P1 Shell")
        while True:
            command = input("> ")
            if command == 'halt.':
                break
            self.handle_command(command)

    def handle_command(self, command):
        if command.startswith('consult('):
            filename = command[len('consult('):-2]
            self.consult(filename)
        else:
            self.evaluate_expression(command)

    def evaluate_expression(self, expr):
        try:
            parsed_expr = self.parser.parse(expr)
            result = self.evaluator.evaluate(parsed_expr)
            print(result)
        except Exception as e:
            print(f"Failed to evaluate expression. Error: {str(e)}")

    def consult(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    self.evaluate_expression(line.strip())
        except Exception as e:
            print(f"Failed to consult file. Error: {str(e)}")

if __name__ == "__main__":
    verbose = "-v" in sys.argv
    shell = Interactive(verbose)
    shell.start_shell()
