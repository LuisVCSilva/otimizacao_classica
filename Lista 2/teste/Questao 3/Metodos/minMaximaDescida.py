from numpy import *
from sys import argv
from util import cria_csv

def minimiza_descida_maxima(f, grad, x_inicial, h, max_it, tol):
  x = x_inicial
  x_anterior = x
  saida = []
  for i in xrange(max_it):
    direcao_descida = -grad(x)
    alfa = h
    x = x + alfa * direcao_descida
    erro = linalg.norm(x - x_anterior)
    if linalg.norm(x - x_anterior) < tol:
      break
    x_anterior = x
    saida.append({'direcao_descida':direcao_descida,'x':x,'f(min)':f(x),'x_anterior':x_anterior,'erro':erro})
  cria_csv("MaximaDescida",saida)
  return x

def main(args):
 f = lambda x: eval(args[0])
 df = lambda x: eval(args[1])
 x_0 = array(eval(args[2]))
 h = float(eval(args[3]))
 tol = float(eval(args[4]))
 max_it = int(eval(args[5]))
 res = minimiza_descida_maxima(f,df,x_0,h,max_it,tol)
 print({'x':res,'f(x)':f(res)})
 
if __name__ == "__main__":
 main(argv[1:])
