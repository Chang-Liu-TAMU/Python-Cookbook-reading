# @Time: 2022/4/1 10:34
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:2.18.Tokenizing_Text.py


text = "foo = 23 + 42 * 10"
tokens = [("NAME", "foo"), ("EQ", "="), ("NUM", "23"), ("PLUS", "+"),
          ("NUM", "42"), ("TIMES", "*"), ("NUM", "10")]

import re
NAME = r"(?P<NAME>[][a-zA-Z_][a-zA-Z_0-9]*)"
NUM = r"(?P<NUM>\d+)"
PLUS = r"(?P<PLUS>\+)"
TIMES = r"(?P<TIMES>\*)"
EQ = r"(?P<EQ>=)"
WS = r"(?P<WS>\s+)"

p = re.compile("|".join([NAME, NUM, PLUS, TIMES, EQ, WS]))

s = "foo = 42"
scanner = p.scanner(s)
print(scanner)

try:
    while True:
        a = scanner.match()
        print(a.lastgroup, a.group())
except:
    print("no matches anymore")
# m1 = scanner.match()
# print(m1.lastgroup, m1.group())
# m2 = scanner.match()
# print(m2.lastgroup, m2.group())

from collections import namedtuple

Token = namedtuple("Token", ["type", "value"])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generate_tokens(p, "foo = 100"):
    print(tok)

tokens = (tok for tok in generate_tokens(p, "a b c = 1 2 3")
          if tok.type != "WS")
for tok in tokens:
    print(tok)

#order matters
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat = re.compile('|'.join([LE, LT, EQ])) # Correct
# master_pat = re.compile('|'.join([LT, LE, EQ])) # Incorrect

