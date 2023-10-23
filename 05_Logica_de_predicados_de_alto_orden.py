from sympy import symbols, ForAll, Eq

# Variables
x, y = symbols('x y')

# Predicados de primer orden
P = Eq(x, 2)
Q = Eq(y, 3)

# Cuantificación de alto orden
formula = ForAll(x, ForAll(y, P & Q))

print(formula)
