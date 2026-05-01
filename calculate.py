import sympy as sp
import numpy as np
from numpy.f2py.auxfuncs import throw_error
from sympy import solveset


def surf_area(x, y, f, b, a, axis):
    f = sp.sympify(f)
    b = sp.sympify(b)
    a = sp.sympify(a)
    if axis.lower() == 'y':
        df = sp.diff(f, x)
        #maybe add abs(x)??
        expr = x * sp.sqrt(1 + df ** 2)
        s = ((2 * sp.pi) * sp.integrate(expr, (x, a, b)))
    elif axis.lower() == 'x':
        df = sp.diff(f, x)
        expr = f * sp.sqrt(1 + df ** 2)
        s = ((2 * sp.pi) * sp.integrate(expr, (x, a, b)))
    else:
        throw_error("Enter valid input")
    return s
