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
 "rp"         : 100.0,\
 "x0"         : [0.1,0.1],\
 "tol"        : 10**(-6),\
 "gama"       : 3.00,\
 "max_it"     : 1000,\
 
 
 "metodo"     : "BFGS",\
 "modo"       : MPFI,\
 "f"          : lambda x: (-1.0) * ((9.0-(x[0]-3.0)**2) * ((x[1]**3)/(27.0*sqrt(3.0)))),\
 "restricoes" : [\
                  lambda x: x[1] - x[0]/sqrt(3.0),\
                  lambda x: x[0]+sqrt(3.0)*x[1]-6,\
                  lambda x: -x[0]\
                ],\
 }


 set_param(problema)
 minimo = solve()
 a = 0.0
 b = 5.0
 h = 0.05
 plota(a,b,h,[minimo])

main()
