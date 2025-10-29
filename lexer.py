import re
import sys

TOKENS = {
    'identifier' :      r'[a-zA-Z_]\w*\b',
    'constant' :        r'[0-9]+\b',
    'int':              r'int\b',
    'void':             r'void\b',
    'return':           r'return\b',
    'open_parenthesis': r'\(',
    'close_parenthesis':r'\)',
    'open_brace':       r'{',
    'close_brace':      r'}',
    'semicolon':        r';'

}

code = sys.stdin.read()

while len(code):
    matched = False
    #remove useless spaces. 
    if code[0].isspace():
        code = code[1:]
        continue

    for name,regex in TOKENS.items():
        match = re.match(regex,code)
        #if we have a match we process here and remvoe the match from the string.
        if match:
            matched = True
            value = match.group(0)
            print(f"TOKEN: {name} VALUE : {value}")
            code = code[match.end():]
            break
    if not matched:
        print("Error no match found at ")
        break
