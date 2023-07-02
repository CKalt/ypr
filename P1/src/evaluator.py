# evaluator.py
from prolog_parser import Parser
from operators import Operators

class Evaluator:
    def __init__(self):
        self.parser = Parser()
        self.operators = Operators()

    def evaluate(self, expression):
        parsed_expression = self.parser.parse(expression)
        for i in range(len(parsed_expression)):
            element = parsed_expression[i]
            if isinstance(element, tuple):
                operator, *operands = element
                if operator == self.parser.constants['and_symbol']['value']:
                    result = self.operators.and_operator(*operands)
                elif operator == self.parser.constants['or_symbol']['value']:
                    result = self.operators.or_operator(*operands)
                elif operator == self.parser.constants['not_symbol']['value']:
                    result = self.operators.not_operator(*operands)
                parsed_expression[i] = result
        return parsed_expression[-1]['value']
