from parser import Parser
from evaluator import Evaluator

class Interactive:
    def __init__(self):
        self.parser = Parser()
        self.evaluator = Evaluator()
        self.prompt = "Prolog Lite - P1 Shell > "

    def start_shell(self):
        while True:
            user_input = input(self.prompt)
            if user_input == 'halt.':
                self.exit()
            elif user_input.startswith('consult('):
                filename = user_input.replace('consult(', '').replace(').', '')
                self.load_file(filename)
            elif len(user_input) > 0:
                self.process_expression(user_input)
            else:
                print("Invalid input. Please enter a boolean expression or a command.")

    def load_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file.readlines():
                    self.process_expression(line.strip())
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    def process_expression(self, expression):
        parsed_expression = self.parser.parse(expression)
        evaluated_result = self.evaluator.evaluate(parsed_expression)
        print(evaluated_result)

    def exit(self):
        print("Terminating the shell.")
        exit(0)


def start_shell():
    shell = Interactive()
    shell.start_shell()


def load_file(filename):
    shell = Interactive()
    shell.load_file(filename)
