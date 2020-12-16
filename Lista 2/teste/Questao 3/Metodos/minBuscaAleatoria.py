from numpy import *
from sys import argv
from util import cria_csv
import pandas as pd

def geraPontos(p1, p2, parts,h,f):
 pontos = []
 for i in linspace(p1[0], p2[0], parts+h):
  for j in linspace(p1[1], p2[1], parts+h):
   pontos.append((i,j,f([i,j])))
 return pontos

def minBuscaAleatoria (f,a,b,tol,max_it,isAleatorio):
 pontos = geraPontos((0.0,0.0),(5.0,5.0),100,0.1,f)
 saida = sorted(pontos,key=lambda x: x[-1])
 df = pd.DataFrame(saida, columns=["x_1","x_2","f(x_1,x_2)"])
 df.to_csv('BuscaAleatoria.csv', index=False)
 return saida[0]
  

def main(args):
 f = lambda x: eval(args[0])
 a = array(eval(args[1]))
 b = array(eval(args[2]))
 tol = eval(args[3])
 max_it = eval(args[4])
 res = minBuscaAleatoria(f,a,b,tol,max_it,False)
 print({'x':res,'f(x)':f(res)})


if __name__ == "__main__":
 main(argv[1:])
