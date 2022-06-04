

import sympy
from sympy import symbols, integrate, N

x = symbols('x')
fx = sympy.sqrt(16-(x-4)**2)
a = integrate(fx, (x, 3, 8))
b = integrate(fx, (x, 5, 8))
print(N(a-b))