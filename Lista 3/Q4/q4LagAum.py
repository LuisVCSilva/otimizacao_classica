from scipy.optimize import minimize
from util import *

def q4():
 a = -10
 b = 10
 rp = 1 
 x = [1.0, 1.0]
 lamb1 = -1
 lamb2 = -1
 tol = 10**-6
 nbIteracoes = 100
 rpmax = 10**5
 gama = 3.0
 
 h  = lambda x: x[0]-x[1]-2
 ps = lambda x: max(x[0]+x[1]-0.5,(-lamb1/(2*rp)))
 
 f  = lambda x: (x[0]-1)**2+(x[1]-1)**2+lamb1*(ps(x))+rp*(ps(x))**2+lamb2*(h(x))+rp*(h(x))**2
 
 f0 = f(x)
 erro = 1 
 
 
 print("{}\t{}\t{}\t{}".format("x_1","x_2","f(x)","erro")) 
 for i in range(nbIteracoes):
     x = minimize (f, x, method="Nelder-Mead", tol=tol).x
     f1 = f(x)  # valor da função para o novo x
     erro = abs(f1-f0)  # erro
     f0 = f1
     print("{}\t{}\t{}\t{}".format(x[0],x[1],f(x),erro))
     if erro<=tol:  # criterio de parada
         return x
         break
     else:
         lamb10 = lamb1
         lamb20 = lamb2
         lamb1 = lamb1+2*rp*ps(x)
         lamb2 = lamb2+2*rp*h(x)  # atualização do lambda
         if abs(lamb1-lamb10) <= tol and abs(lamb2-lamb20) <= tol:  # criterio de parada caso o lambda não mude de valor
             return x
             break
         else:
             rp = gama*rp  # incremento do rp
             if rp>rpmax:  # caso o rp ultrapasse o valor de rp maximo
                 rp = rpmax
     if i==nbIteracoes:
         return x
 
res = q4()

a = 0.0
b = 5.0
h = 0.05
