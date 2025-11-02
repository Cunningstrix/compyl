from parser import *

class CodeGenerator:
    def __init__(self):
        self.output = []
    
    def generate(self, program):
        self.output.append('\t.section .text')
        self.output.append('\t.globl main')
        for f in program.functions:
            self.generate_function(f)
        self.output.append('\t.section .note.GNU-stack,"",@progbits')
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
            #Mov(src, dst) :  movl src, dst
            self.output.append(f'\tmovl ${e.value}, %eax')