from parser import *

class CodeGenerator:
    def __init__(self):
        self.output = []
    
    def generate(self, program):
        self.output.append('section .text')
        for f in program.functions:
            self.generate_function(f)
        return '\n'.join(self.output)
    
    def generate_function(self, f):
        self.output.append(f'{f.name}:')
        self.generate_statement(f.body)
        self.output.append('\tret')
    
    def generate_statement(self, s):
        if isinstance(s, Expression):
            self.generate_expression(s.value)

    def generate_expression(self, e):
        if isinstance(e, Constant):
            self.output.append(f'\tmovl ${e.value}, %eax')