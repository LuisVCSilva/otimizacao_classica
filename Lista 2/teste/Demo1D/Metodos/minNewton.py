from numpy import *
from sys import argv

def minimiza_newton(f, g, H, x0, max_it, tol):
  x = x0
  x_anterior = x
  for i in xrange(max_it):
    direcao_descida = -linalg.solve(H(x), g(x))
    alfa = 0.1
    x = x + alfa * direcao_descida
    if linalg.norm(x - x_anterior) < tol:
      break
    x_anterior = x
  return x.ravel()


def main(args):
 f   = lambda x: eval(args[0])
 df  = lambda x: array(eval(args[1]))
 d2f = lambda x: array(eval(args[2]))
 x_0 = 0.0
 h = 0.01
 max_it = 100
 tol = 0.0001
 res = minimiza_newton(f,df,d2f,x_0,max_it,tol)
 print({'x':res,'f(x)':f(res)})

if __name__ == "__main__":
 main(argv[1:])
