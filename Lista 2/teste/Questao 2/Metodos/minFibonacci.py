#!/usr/bin/env python

from numpy import *
from sys import argv
from util import cria_csv
from inspect import getsource

fibonacci = lambda n: n if n<=1 else fibonacci(n-2) + fibonacci(n-1)
def minimiza_fibonacci(f, a, b, tol=0.01):
 fa = f(a)
 fb = f(b)
 h = abs(tol)
 num_fibonacci = 50
 saida = []
 n = (b-a)/tol
 n = n-1 if n*tol==b-a else n
 
 i = 1
 while (i<num_fibonacci):
  if (fibonacci(i-1) + fibonacci(i))>=n:
   break
  if i>num_fibonacci:
   return
  i += 1
 x1 = a + fibonacci(i - 1) * tol
 x2 = a + fibonacci(i) * tol
 fx1 = f(x1)
 if x2 <= b:
  fx2 = f(x2) 
 else:
  fx2 = sys.maxint
 while i > 0:
  erro = a-b
  saida.append({'i':i,'x1':x1,'f(x1)':fx1,'x2':x2,'f(x2)':f(x2),'a':a,'f(a)':fa,'b':b,'f(b)':fb,'erro':erro})
  if (fx1 > fx2): #min max
   a = x1
   fa = fx1
   x1 = x2
   fx1 = fx2
   i = i-1
   if i==0:
    break
   x2 = a + fibonacci(i) * tol
   if x2 <= b:
    fx2 = f(x2) 
   else:
    fx2 = sys.maxint
  else:
   b = x2
   fb = fx2
   x2 = x1
   fx2 = fx1
   i = i-1
   if i==0:
    break
   x1 = a + fibonacci(i - 1) * tol
   fx1 = f(x1)
   
 cria_csv("Fibonacci",saida)
 return x2 



def main(args):
 f = lambda x: eval(args[0])
 a = array(eval(args[1]))
 b = array(eval(args[2]))
 tol = eval(args[3])
 res = minimiza_fibonacci( f, a, b, tol);       
 print({"x":res,"f(x)":f(res)})

if __name__ == "__main__":
 main(argv[1:])
