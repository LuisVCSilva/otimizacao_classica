from numpy import *

from os import system
from inspect import getsource
from sys import argv
from util import cria_csv


def secaoAurea (f,intervalo,epsilon):
 a = [intervalo[0]]
 b = [intervalo[1]]

 k = 0
 y = []
 z = []

 y.append(a[k] + ((3-sqrt(5))/2.0) * (b[k]-a[k]))
 z.append(a[k] + ((sqrt(5)-1)/2.0) * (b[k]-a[k]))

 f_y = [f([y[k]])]
 f_z = [f([z[k]])]

 erro = []
 result = []
 while 1:
  erro.append((b[k]-a[k]))
  result.append((b[k]+a[k])/2.0)
  if b[k]-a[k] < epsilon:
   saida = [{"k":j,"a":a[j],"b":b[j],"y":y[j],"f(y)":f_y[j],"z":z[j],"f(z)":f_z[j],"erro":erro[j],"min":result[j]} for j in range(k+1)]
   cria_csv("Secao Aurea",saida)
   return saida

  elif f([y[k]])>f([z[k]]):
   a.append(y[k])
   b.append(b[k])
   y.append(z[k])
   z.append((a[k+1] + ((sqrt(5)-1)/2.0) * (b[k+1]-a[k+1])))
   f_y.append(f([y[k+1]]))
   f_z.append(f([z[k+1]]))
  else:
   a.append(a[k])
   b.append(z[k])
   z.append(y[k])
   y.append(a[k+1] + ((3-sqrt(5))/2.0) * (b[k+1] - a[k+1]))
   f_y.append(f([y[k+1]]))
   f_z.append(f([z[k+1]]))
  k = k+1


def main(args):
 f = lambda x: eval(args[0])
 intervalo = eval(args[1])
 #print([(x,f([x])) for x in range(10)])
 epsilon = eval(args[2])
 res = secaoAurea(f,intervalo,epsilon)
 print({'x':res[-1]['z'],'f(x)':f([res[-1]['z']])})

if __name__ == "__main__":
 main(argv[1:])
