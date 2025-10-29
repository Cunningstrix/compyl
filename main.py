from lexer import Lexer
from parser import Parser 
import sys

Lexer = Lexer()
code : str = sys.stdin.read()
tokens = Lexer.tokenize(code)

print(tokens)
parser = Parser(tokens)
parser.parse_program()