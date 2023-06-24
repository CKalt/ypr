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
