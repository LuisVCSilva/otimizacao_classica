from numpy import *

fibonacci = lambda n: n if n<=1 else fibonacci(n-2) + fibonacci(n-1)

def minimiza_fibonacci(f, a, b, tol=0.01):
 h = abs(tol)
 fa = f(a)
 fb = f(b)
 num_fibonacci = 100
 result = []
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
  if (fx1 > fx2):
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
  result.append({'i':i,'a':a,'fa':fa,'b':b,'fb':fb,'x1':x1,'fx1':fx1,'x2':x2,'fx2':fx2})
  print([i,a[0],fa,b[0],fb,x1[0],fx1,x2[0],fx2])
 return result

def main():
 f = lambda x: (sin(0.1+2*x[0]))/(1+x[0])
 a = array([0.0])
 b = array([3.0])
 tol = 0.0001
 res = minimiza_fibonacci(f, a, b, tol)
 print(res[-1]['x2'])
 #print({"x":res,"f(x)":f(res)})

if __name__ == "__main__":
 main()
