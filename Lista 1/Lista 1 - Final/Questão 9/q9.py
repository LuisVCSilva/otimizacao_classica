from scipy import optimize
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from math import pi



f = lambda x: (-1.0) * (pi*x[0]*x[1])
g_1 = lambda x: x[1]-0.12- (-0.07/0.6) * x[0] #ineq
g_2 = lambda x: pi*(3*(x[0]+x[1]) - sqrt((3*x[0]+x[1])+(x[0]+3*x[1]))) - 1.75
bound = 20.0
bnds=((-bound,bound),(-bound,bound))

cons=({'type':'ineq','fun':g_1},{'type':'ineq','fun':g_2})
x0=[1,1]
res= optimize.minimize(f,x0,method='SLSQP',bounds=bnds,constraints=cons)
print(res)
