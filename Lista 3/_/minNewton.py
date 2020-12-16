from numpy import *
from sys import argv
from util import cria_csv

def minimiza_newton(f, g, H, x0, max_it, tol):
  x = x0
  x_anterior = x
  saida = []
  for i in xrange(max_it):
    direcao_descida = -linalg.solve(H(x), g(x))
    alfa = 0.1
    x = x + alfa * direcao_descida
    erro = linalg.norm(x - x_anterior)
    if linalg.norm(x - x_anterior) < tol:
      break
    saida.append({'direcao_descida':direcao_descida,'x':x,'f(min)':f(x),'erro':erro})
    x_anterior = x
  cria_csv("Newton",saida)
  return x.ravel()


def main(args):
 f   = lambda x: (eval(args[0]))
 df  = lambda x: (eval(args[1]))
 d2f = lambda x: (eval(args[2]))
 x_0 = eval(args[3])
 h = eval(args[4])
 max_it = eval(args[5])
 tol = eval(args[6])
 res = minimiza_newton(f,df,d2f,x_0,max_it,tol)
 print({'x':res,'f(x)':f(res)})

if __name__ == "__main__":
 main(argv[1:])
