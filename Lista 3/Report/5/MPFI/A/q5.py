from numpy import *
from util import *


def main():
 problema = {\
 "C"          : 0.15,\
 "a"          : 0.5,\
 "rp"         : 10.0,\
 "x0"         : [1.0,1.0],\
 "tol"        : 10**(-6),\
 "gama"       : 3.00,\
 "max_it"     : 100,\
 
 
 "metodo"     : "Nelder-Mead",\
 "modo"       : MPFE,\
 "f"          : lambda x: x[0]**2 + 2*x[1]**2 - 2*x[0]*x[1] - 14*x[0] - 14*x[1] + 10,\
 "restricoes" : [\
                  lambda x:  4*x[0]**2 + x[1]**2 - 25
                ],\
 }


 set_param(problema)
 minimo = solve()
 a = 0.0
 b = 5.0
 h = 0.05
 plota(a,b,h,[minimo])

main()
