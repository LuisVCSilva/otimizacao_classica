from copy import *
from numpy import *
from sys import argv
from util import cria_csv

def nelder_mead(f,  x_inicial, passo=0.1, limiar_semMelhora=10e-6, max_sem_melhora=10, max_iter=0, alfa=1., gama=2., rho=-0.5, sigma=0.5):
 dim = len( x_inicial)
 melhor_anterior = f( x_inicial)
 sem_melhora = 0
 res = [[ x_inicial, melhor_anterior]]
 saida = []
 for i in range(dim):
  x = copy(x_inicial)
  x[i] = x[i] + passo
  score = f(x)
  res.append([x, score])

 it = 0
 saida = []
 while 1:
  res.sort(key=lambda x: x[1])
  melhor_ponto = res[0][1]
  if max_iter and it >= max_iter:
   cria_csv("NelderMead",saida)
   return res[0]
  it += 1
  saida.append({'res':f(res[-1]),'erro':melhor_ponto-melhor_anterior})
  if melhor_ponto < melhor_anterior - limiar_semMelhora:
   sem_melhora = 0
   melhor_anterior = melhor_ponto
  else:
   sem_melhora += 1
  if sem_melhora >= max_sem_melhora:
   cria_csv("NelderMead",saida)
   return res[0]

  #reposiciona centroide
  x0 = [0.] * dim
  for tup in res[:-1]:
   for i, c in enumerate(tup[0]):
    x0[i] += c / (len(res)-1)

  # reflexao
  xr = x0 + alfa*(x0 - res[-1][0])
  rscore = f(xr)
  if res[0][1] <= rscore < res[-2][1]:
   del res[-1]
   res.append([xr, rscore])
   continue

  # expansao
  if rscore < res[0][1]:
   xe = x0 + gama*(x0 - res[-1][0])
   escore = f(xe)
   if escore < rscore:
    del res[-1]
    res.append([xe, escore])
    continue
   else:
    del res[-1]
    res.append([xr, rscore])
    continue

  # contracao
  xc = x0 + rho*(x0 - res[-1][0])
  cscore = f(xc)
  if cscore < res[-1][1]:
   del res[-1]
   res.append([xc, cscore])
   continue

  # reducao
  x1 = res[0][0]
  nres = []
  for tup in res:
   redx = x1 + sigma*(tup[0] - x1)
   score = f(redx)
   nres.append([redx, score])
  res = nres
 cria_csv("NelderMead",saida)
 return res

def main(args):
 f = lambda x: eval(args[0])
 x_inicial = array(eval(args[1]))
 res = nelder_mead(f, x_inicial)[0]
 print({'x':res,'f(x)':f(res)})

if __name__ == "__main__":
 main(argv[1:])
