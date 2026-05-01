import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from numpy.f2py.auxfuncs import throw_error
from calculate import surf_area
from plot import plot

x = sp.symbols("x")
y = sp.symbols("y")
axis = input("Rotate around x-axis (enter 'x') or y-axis (enter 'y')? ")
print("""
Function Input Guide:
  x**n        means xⁿ
  sqrt(x)     means √x
  sin(x)      means sin(x)
  cos(x)      means cos(x)
  tan(x)      means tan(x)
  log(x)      means ln(x)
  E           means Euler's number e
  exp(x)      means eˣ
  exp(x**2)   means e^(x²)
  x*E**2      means x · e²
  pi          means π
Important:
  Use ** for exponents
  Use * for multiplication
  Write 3*x, not 3x
""")
if axis.lower() == 'y':
    f = input("Enter y = f(x):")
elif axis.lower() == 'x':
    f = input("Enter y = f(x):")
else:
    throw_error("Invalid input")
a = input("Enter Lower Bound: ")
b = input("Enter Upper Bound: ")
#s = surf_area(x, y, f, b, a, axis)
#print(f"{sp.pretty(s)}\n")
#print(f"Approx:{s.evalf()}")
plot(a, b, f, x, axis)








