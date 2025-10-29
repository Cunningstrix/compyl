import re

TOKENS : dict[str, str] = {
    'IDENTIFIER' :      r'[a-zA-Z_]\w*\b',
    'COONSTANT' :        r'[0-9]+\b',
    'INT':              r'int\b',
    'VOID':             r'void\b',
    'RETURN':           r'return\b',
    'OPEN_PARENTHESIS': r'\(',
    'CLOSE_PARENTHESIS':r'\)',
    'OPEN_BRACE':       r'{',
    'CLOSE_BRACE':      r'}',
    'SEMICOLON':        r';',
    'SKIP':             r'[ \n\t]+',
    'MISSMATCH':        r'.'

}

token_re : str = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKENS.items()))

class Lexer:
    @staticmethod
    def tokenize(code) -> list[tuple[str,str]]:
        tokens : list[tuple[str,str]] = []

        for match in token_re.finditer(code):
            found : str = match.lastgroup
            val : str = match.group()

            if found == 'SKIP':
                continue
            elif found == "MISSMATCH":
                raise SyntaxError(f'Syntax missmatch : {val}')
            else:
                tokens.append((found,val))

        return tokens