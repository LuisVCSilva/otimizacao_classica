#!/usr/bin/env python
fibonacci = lambda n: n if n<=1 else fibonacci(n-2) + fibonacci(n-1)
from math import sqrt

def minimiza_fibonacci(f, a, b, tol=0.01):
 h = abs(tol)
 num_fibonacci = 50
 fa = f(a)
 fb = f(b)
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
 return x2 


f = lambda x: 3*x**2-5*x

def main():
 a = 0.0                   
 b = 3.0                  
 fa = f(a)
 fb = f(b)
 tol = 0.001
 res = minimiza_fibonacci(f, a, b, tol);       
 print({"x":res,"f(x)":f(res)})

if __name__ == "__main__":
 main()
