# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from real_lexer import tokens



# Start here?


def p_expression_exp(p):
    '''expression : LPAREN expression RPAREN
       | LIT
       | binop
       | varid'''
    #WARNING Maybe needs question mark after expression?

    p[0] = p[1]

    print("Expression Expression called")
    # if isInstance(p[1], globid) and p[2] == '(':
    #   if isInstance(p[3], expressions) and p[4] == ')':
    #     p[0] = None
    #   elif p[3] == ')':
    #     p[0] = None
def p_expression_arith(p):
    '''arith-ops : expression TIMES expression
       | expression DIVIDE expression
       | expression PLUS expression
       | expression MINUS expression'''
    print("Expression arith called")
    p[0] = p[1]

def p_expression_logic(p):
    '''logic-ops : expression EQU expression
       | expression LTH expression
       | expression BTH expression
       | expression BAND expression
       | expression BOR expression'''
    print("Expression logic called")
    p[0] = p[1]



def p_expression_binop(p):
    '''binop : arith-ops
       | logic-ops'''
    print("Expression Binop called")
    p[0] = p[1]

parser = yacc.yacc()

result = parser.parse("2 == 3")
#result = parser.parse("2")




