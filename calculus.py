#calculus sample
import sympy
from sympy import Symbol, solve, pprint, Derivative, Integral
#Fetch symbols
x = Symbol('x')
y = Symbol('y')

#Solving equation system
expression1 = 2*x + 3*y -6
expression2 = 3*x + 2*y -12
solution = solve((expression1,expression2),dict=True)
pprint(f"\nStart of print: Solving equation system\n{solution}\nEnd of print.")

#differentiation
f = 1/3*(sympy.root(x,2))
df_dx = Derivative(f,x).doit()
print(f"\nStart of print: Differentiation\n{df_dx}\nEnd of print.")
#substitution into differentiation
print(f"\nStart of print: Substitution into differentiation\n{df_dx.subs({x:3})}\nEnd of print.")

#intergration
g = 5*x*(x-3)**1/2
intergrate = Integral(g,x).doit()
pprint(f"\nStart of print: Intergration\n{intergrate}\nEnd of print.")
result = Integral(g,x,(x,3,7)).doit()
#indefinite intergrals
pprint(f"\nStart of print: Indefinite Intergrals\n{result}\nEnd of print.")
