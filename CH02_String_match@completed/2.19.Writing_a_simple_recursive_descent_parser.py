# @Time: 2022/4/1 11:46
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:2.19.Writing_a_simple_recursive_descent_parser.py

import re
import collections

NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile("|".join([NUM, PLUS, MINUS, TIMES,
                                  DIVIDE, LPAREN, RPAREN, WS]))

#Tokenizer
Token = collections.namedtuple("Token", ["type", "value"])

def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != "WS":
            yield tok

#Parser

class ExpressionEvaluator:
    def parse(self, text, parse_tree=False):
        self.parse_tree = parse_tree
        self.tokens = generate_tokens(text)
        self.tok = None
        self.nexttok = None
        self._advance()
        return self.expr()

    def _advance(self):
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)


    def _accept(self, toktype):
        if self.nexttok and toktype == self.nexttok.type:
            self._advance()
            return True
        else:
            return False



    def _expect(self, toktype):
        if not self._accept(toktype):
            raise SyntaxError("Expected " + toktype)

    def expr(self):
        exprval = self.term()
        while self._accept("PLUS") or self._accept("MINUS"):
            op = self.tok.type
            next_term = self.term()
            if op == "PLUS":
                if self.parse_tree:
                    exprval = ("+", exprval, next_term)
                else:
                    exprval += next_term
            elif op == "MINUS":
                if self.parse_tree:
                    exprval = ("-", exprval, next_term)
                else:
                    exprval -= next_term
        return exprval

    def term(self):
        termval = self.factor()
        while self._accept("TIMES") or self._accept("DIVIDE"):
            op = self.tok.type
            next_factor = self.factor()
            if op == "TIMES":
                if self.parse_tree:
                    termval = ("*", termval, next_factor)
                else:
                    termval *= next_factor
            elif op == "DIVIDE":
                if self.parse_tree:
                    termval = ("/", termval, next_factor)
                else:
                    termval /= next_factor
        return termval

    def factor(self):
        if self._accept("NUM"):
            return int(self.tok.value)
        elif self._accept("LPAREN"):
            exprval = self.expr()
            self._expect("RPAREN")
            return exprval
        else:
            raise SyntaxError("Expected NUMBER or LPAREN")


e = ExpressionEvaluator()
print(e.parse("2"))
print(e.parse("(2 + 3) *  2 + 1"))
print(e.parse("(2 + 3) *  2 + 1", parse_tree=True))

'''
expr: := term {('+' | '-') term} *

term: := factor {('*' | '/') factor} *

factor: := '('expr')'
        | NUM
'''


from ply.lex import lex
from ply.yacc import yacc
tokens = [ 'NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN' ]

t_ignore = ' \t\n'
t_PLUS = r"\+"
t_MINUS = r"\-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Bad character: {!r}".format(t.value[0]))
    t.skip(1)


lexer = lex()

def p_expr(p):
     '''
     expr : expr PLUS term
     | expr MINUS term
     '''
     if p[2] == '+':
        p[0] = p[1] + p[3]
     elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_expr_term(p):
     '''
     expr : term
     '''
     p[0] = p[1]

def p_term(p):
     '''
     term : term TIMES factor
     | term DIVIDE factor
     '''
     if p[2] == '*':
        p[0] = p[1] * p[3]
     elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = p[1]

def p_factor(p):
    '''
    factor : NUM
    '''
    p[0] = p[1]

def p_factor_group(p):
    '''
    factor : LPAREN expr RPAREN
    '''
    p[0] = p[2]


def p_error(p):
    print('Syntax error')


parser = yacc()
print(parser.parse("2"))
print(parser.parse("2+(3+4)*5"))


# etc

#python's ast module