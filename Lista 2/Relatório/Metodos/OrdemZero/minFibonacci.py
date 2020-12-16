from numpy import *

fibonacci = lambda n: n if n<=1 else fibonacci(n-2) + fibonacci(n-1)

def minimiza_fibonacci(f, a, b, tol=0.01):
 h = abs(tol)
 fa = f(a)
 fb = f(b)
 num_fibonacci = 100

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
 return x2.ravel()

def main():
 f = lambda x: (12*x[0]**2-16*x[0]+8)
 a = array([0.0])
 b = array([12.0])
 tol = 0.0001
 res = minimiza_fibonacci(f, a, b, tol)
 print({"x":res,"f(x)":f(res)})

if __name__ == "__main__":
 main()
