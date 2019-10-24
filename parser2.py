# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from real_lexer import tokens



# Start here?


def p_term_type(p):
    '''type : INT
       | CINT
       | FLOAT
       | BOOL
       | VOID'''
    #WARNING STILL NEED NOALIAS...
    p[0] = Node("type", [p[1],p[3]], p[2])


def p_expression_vdecl(p):
    'vdecl : type varid'
    p[0] = Node("vdecl", [p[1],p[3]], p[2])


def p_expression_tdecls(p):
    '''tdecls : type
       | type COMMA tdecls'''
    p[0] = Node("tdecls", [p[1],p[3]], p[2])

def p_expression_vdecls(p):
    '''vdecls : vdecl
       | vdecl COMMA vdecls'''
    p[0] = Node("tdecl", [p[1],p[3]], p[2])


def p_expression_blk(p):
	'block : LBRACE statements RBRACE'
	p[0] = p[1]

def p_expression_stmts(p):
	'statements : statement PLUS'
	p[0] = p[1]

def p_expression_stmt(p):
	'''statement : block
				 | vdecl EQU expression SEMICO
				 | expression SEMICO
				 | PRINT expression SEMICO
				 | PRINT slit SEMICO'''
	#WARNING pretty sure this is wrong
	p[0] = p[1]

def p_expression_exps(p):
    '''expressions : expression
                   | expression COMMA expression'''
    print("Expressions called")
    p[0] = p[1]

def p_factor_lit(p):
    'factor : LIT'
    print("test called")
    p[0] = p[1]

def p_expression_exp(p):
    '''expression : LPAREN expression RPAREN
       | binop
       | uop
       | LIT
       | varid
       | globid LPAREN expressions RPAREN'''
    #WARNING Maybe needs question mark after expression?

    p[0] = p[1]

    print("Expression Expression called")
    # if isInstance(p[1], globid) and p[2] == '(':
   	# 	if isInstance(p[3], expressions) and p[4] == ')':
   	# 		p[0] = None
   	# 	elif p[3] == ')':
   	# 		p[0] = None




def p_expression_binop(p):
    '''binop : arith-ops
       | logic-ops
       | varid EQU expression
       | LBRACK type RBRACK expression'''
    print("Expression Binop called")
    p[0] = Node("binop", [p[1],p[3]], p[2])


def p_expression_arith(p):
    '''arith-ops : expression TIMES expression
       | expression DIVIDE expression
       | expression PLUS expression
       | expression MINUS expression'''
    print("Expression arith called")
    p[0] = Node("arith-ops", [p[1],p[3]], p[2])

def p_expression_logic(p):
    '''logic-ops : expression EQU expression
       | expression LTH expression
       | expression BTH expression
       | expression BAND expression
       | expression BOR expression'''
    print("Expression Binop called")
    p[0] = Node("logic-ops", [p[1],p[3]], p[2])

def p_term_uop(p):
    '''uop : NEG expression
       | MINUS expression'''
    print("Expression UOP called")
    p[0] = not p[1]

def p_term_globid(p):
    'globid : ident'
    p[0] = p[1]




# def p_expression_prog(p):
# 	'prog : extern function'
# 	p[0] = p[1]

# def p_expression_extern(p):
# 	'extern : extern type globid LPAREN tdecls RPAREN SEMICO' #WARNING DID THIS WRONG
# 	p[0] = p[1]

	

def p_expression_func(p):
	'function : DEF type globid LPAREN vdecls RPAREN block' #WARNING DID THIS WRONG
	p[0] = p[1]
	



'''    

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]




def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = ('group-expression',p[2])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number-expression',p[1])
'''

# Error rule for syntax errors

# def p_error(p):

#     print("Syntax error in input!")
#     print(p)

# Build the parser

parser = yacc.yacc()

result = parser.parse("2 + 3")
#result = parser.parse("2")




