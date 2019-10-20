# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex
import sys
# List of token names.   This is always required
tokens = (
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'LPAREN',
'RPAREN',
'lit',
'type',
'ident',
'varid',

)

type_regex = r'(int|cint|float|bool|void)'
# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_lit     = r'true|false|[0-9]+(\.[0-9]+)?'
t_type    = r'' + type_regex + r'|(noalias )?ref ' + type_regex
t_ident   = r'[a-zA-Z_]+[a-zA-Z0-9_]*'
t_varid   = r'\$' + t_ident


# Define a rule so we can track line numbers
def t_newline(t):
 r'\n+'
 t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
 print("Illegal character '%s'" % t.value[0])
 t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = ''
with open(sys.argv[1], 'r') as my_file:
	data += (my_file.read())
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
 tok = lexer.token()
 if not tok: 
     break      # No more input
 print(tok)
