from lexer import Lexer
import sys

Lexer = Lexer()
code : str = sys.stdin.read()
a = Lexer.tokenize(code)
print(a)
