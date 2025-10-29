class Function:
    def __init__(self, name : str, body: str):
        self.name : str = name
        self.body : str = body

class Program:
    def __init__(self,functions : list[Function]):
        self.functions : list[Function] = []

class Expression:
    def __init__(self, expr):
        self.value : str = expr

class Constant:
    def __init__(self,value : int):
        self.value : int = value

class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return ('EOF', '')
    
    def parse_program(self):
        funcs = [self.parse_function()]
        return Program(funcs)
    
    def parse_function(self):
        self.expect('INT')
        name = self.expect('IDENTIFIER')
        self.expect('OPEN_PARENTHESIS')
        self.expect('VOID')
        self.expect('CLOSE_PARENTHESIS')
        self.expect('OPEN_BRACE')
        body = self.parse_statement()
        self.expect('CLOSE_BRACE')
        return Function(name, body)
    
    def parse_statement(self):
        if self.current()[0] == 'RETURN':
            self.expect('RETURN')
            expr = self.parse_expression()
            self.expect('SEMICOLON')
            return Expression(expr)
        else:
            raise SyntaxError(f'Expected return INT; at index {self.pos}' )
    
    def parse_expression(self) -> Constant:
        tok = self.current()
        if tok[0] == 'CONSTANT':
            val : int = int(self.expect('CONSTANT'))
            return Constant(val)
        raise SyntaxError(f"Expected int at index {self.pos}" )

    def expect(self,kind):
        tok = self.current()
        if tok[0] == kind:
            self.pos += 1
            return tok[1]
        raise SyntaxError(f'Expected token {kind} but got {tok[0]} instead')
    
        

    


