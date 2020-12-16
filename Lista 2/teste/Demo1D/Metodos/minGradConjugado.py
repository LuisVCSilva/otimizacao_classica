from numpy import *
from sys import argv

def minimiza_gradiente_conjugado(f, df, x0, max_it, tol):
  xk = x0
  fk = f(xk)
  gk = df(xk)
  pk = -gk
  for i in range(max_it):
    alfa = 0.01
    xk1 = xk + alfa * pk
    gk1 = df(xk1)
    beta_k1 = dot(gk1, gk1) / dot(gk, gk)
    pk1 = -gk1 + beta_k1 * pk
    if linalg.norm(xk1 - xk) < tol:
      xk = xk1
      break
    xk = xk1
    gk = gk1
    pk = pk1
  return xk

def main(args):
 f  = lambda x: eval(args[0])
 df = lambda x: eval(args[1])
 x_inicial = array(eval(args[2]))
 tol = eval(args[3])
 max_it = eval(args[4])
 x = minimiza_gradiente_conjugado(f, df, x_inicial,max_it=max_it, tol=tol)
 print({'x':x,'f(x)':f(x)})

if __name__ == "__main__":
 main(argv[1:])
