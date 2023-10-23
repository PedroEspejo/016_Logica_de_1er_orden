from sympy import symbols, Function, ForAll

# Variables
x = symbols('x')

# Funciones de primer orden
F = Function('F')(x)

# Cuantificación de orden superior
formula = ForAll(x, F > 0)

print(formula)
