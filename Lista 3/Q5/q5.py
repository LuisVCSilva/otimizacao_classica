from numpy import *
from util import *


def main():
 problema = {\
 "C"          : 0.15,\
 "a"          : 0.5,\
 "rp"         : 10.0,\
 "x0"         : [0.0,0.0,0.0,0.0],\
 "tol"        : 10**(-6),\
 "gama"       : 3.00,\
 "max_it"     : 100,\
 
 
 "metodo"     : "BFGS",\
 "modo"       : MPFI,\
 "f"          : lambda x: x[0]**2 + x[1]**2 + 2*x[2]**2 - x[3]**2 - 5*x[0] - 5*x[1] - 21*x[2] + 7*x[3] + 100,\
 "restricoes" : [\
                  lambda x:  x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2 + x[0] - x[1] + x[2] - x[3] - 100,\
                  lambda x:  x[0]**2 + 2*x[1]**2 + x[2]**2 + 2*x[3]**2 - x[0] - x[3] - 10,\
                  lambda x:  2*x[0]**2 + x[1]**2 + x[2]**2 + 2*x[0] - x[1] - x[3] - 5\
                ],\
 }


 set_param(problema)
 minimo = solve()
 a = 0.0
 b = 5.0
 h = 0.05
 #plota(a,b,h,[minimo])

main()
