from lexer import Lexer
from parser import Parser
import sys

Lexer = Lexer()
code : str = sys.stdin.read()
tokens = Lexer.tokenize(code)
parser = Parser(tokens)
ast = parser.parse_program()
print(ast)