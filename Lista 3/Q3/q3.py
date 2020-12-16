from numpy import *
from util import *

'''
default

 "C"          : 0.15,\           #0.15
 "a"          : 0.5,\            #0.5
 "rp"         : 10000.0,\        #10.0
 "x0"         : [1.0,1.0],\      #1.0, 1.0
 "tol"        : 10**(-6),\       #10^-6
 "gama"       : 3.00,\           #3.0 para MPFE 0.003 para MPFI
 "max_it"     : 100,\            #100
 
 
 "metodo"     : "Nelder-Mead",\ #Nelder-Mead
 "modo"       : MPFI,\          #MPFE
'''


def main():
 problema = {\
 "C"          : 0.15,\
 "a"          : 0.5,\
 "rp"         : 10000.0,\
 "x0"         : [1.0,1.0],\
 "tol"        : 10**(-6),\
 "gama"       : 3.00,\
 "max_it"     : 100,\
 
 
 "metodo"     : "BFGS",\
 "modo"       : LA,\
 "f"          : lambda x: (x[0]-1)**2 + (x[1]-1)**2,\
 "restricoes" : [\
                  lambda x: x[0]+x[1]-0.5
                ],\
 }


 set_param(problema)
 minimo = solve()
 a = 0.0
 b = 5.0
 h = 0.05
 plota(a,b,h,[minimo])

main()
