#bryly.py
import math

# Figury płaskie
def o_kwadratu(a):
    return 4 * a

def p_kwadratu(a):
    return a**2

def o_prostokata(a, b):
    return 2 * (a + b)

def p_prostokata(a, b):
    return a * b

def o_rownolegloboku(a, b):
    return 2 * (a + b)

def p_rownolegloboku(a, h):
    return a * h

def o_trapezu(a, b, c, d):
    return a + b + c + d

def p_trapezu(a, b, h):
    return ((a + b) * h) / 2

def o_trojkata(a, b, c):
    return a + b + c

def p_trojkata(a, h):
    return (a * h) / 2

def p_trojkata_rownobocznego(a):
    return (a**2 * math.sqrt(3)) / 4

def o_kola(r):
    return 2 * math.pi * r

def p_kola(r):
    return math.pi * r**2

def o_rombu(a):
    return 4 * a

def p_rombu(e, f):
    return (e * f) / 2

# Bryły
def p_szescianu(a):
    return 6 * a**2

def v_szescianu(a):
    return a**3

def p_prostopadloscianu(a, b, c):
    return 2 * (a*b + b*c + a*c)

def v_prostopadloscianu(a, b, c):
    return a * b * c

def p_graniastoslupa(pp, pb):
    return 2 * pp + pb

def v_graniastoslupa(pp, h):
    return pp * h

def p_ostroslupa(pp, pb):
    return pp + pb

def v_ostroslupa(pp, h):
    return (1/3) * pp * h

def p_walca(r, h):
    return 2 * math.pi * r * (r + h)

def v_walca(r, h):
    return math.pi * r**2 * h

def p_stozka(r, l):
    return math.pi * r * (r + l)

def v_stozka(r, h):
    return (1/3) * math.pi * r**2 * h

def p_kuli(r):
    return 4 * math.pi * r**2

def v_kuli(r):
    return (4/3) * math.pi * r**3