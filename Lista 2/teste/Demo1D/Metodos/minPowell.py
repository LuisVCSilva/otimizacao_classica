from numpy import *
from sys import argv
 
def minimiza_powell (f,a,b,tol):
 x1 = a
 x2 = a+b
 x3 = b
 
 f1 = f(x1)
 f2 = f(x2)
 f3 = f(x3)
 tol = 0.01
 
 while x3-x1>tol:
  x4 = 0.5 * (((x2**2 - x3**2) * f1 + (x3**2-x1**2) * f2 + (x1**2 - x2**2) * f3) / (( x2-x3) * f1 + (x3-x1)*f2 + (x1-x2)*f3))
  f4 = f(x4)
  if x4>x2:
   if f4<f2:
    x1 = x2
    x2 = x4
    f1 = f2
    f2 = f4
    x3 = x4
    f3 = f4
   if f4<f2:
    x3 = x2
    x2 = x4
    f3 = f2
    f2 = f4
   x1 = x4
   f1 = f4
 return x4

def main(args):
 f = lambda x: eval(args[0])
 a = array(eval(args[1]))
 b = array(eval(args[2]))
 tol = eval(args[3])
 res = minimiza_powell(f,a,b,tol)
 print({'x':res,'f(x)':f(res)})

if __name__ == "__main__":
 main(argv[1:])
