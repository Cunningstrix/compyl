from lexer import Lexer
from parser import Parser
from generator import CodeGenerator
import sys

Lexer = Lexer()
code : str = sys.stdin.read()
tokens = Lexer.tokenize(code)
parser = Parser(tokens)
program = parser.parse_program()

Generator = CodeGenerator()
asm = Generator.generate(program)
print(asm)