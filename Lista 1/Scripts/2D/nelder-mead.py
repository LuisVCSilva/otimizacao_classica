import copy
import math
import numpy as np
from math import *

def nelder_mead(f,  x_inicial, passo=0.1, limiar_semMelhora=10e-6, max_sem_melhora=10, max_iter=0, alfa=1., gama=2., rho=-0.5, sigma=0.5):
 dim = len( x_inicial)
 melhor_anterior = f( x_inicial)
 sem_melhora = 0
 res = [[ x_inicial, melhor_anterior]]

 for i in range(dim):
  x = copy.copy( x_inicial)
  x[i] = x[i] + passo
  score = f(x)
  res.append([x, score])

 iters = 0
 while 1:
  res.sort(key=lambda x: x[1])
  best = res[0][1]

  if max_iter and iters >= max_iter:
   return res[0]
  iters += 1

  if best < melhor_anterior - limiar_semMelhora:
   sem_melhora = 0
   melhor_anterior = best
  else:
   sem_melhora += 1
  if sem_melhora >= max_sem_melhora:
   return res[0]

  #reposiciona centroid
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


if __name__ == "__main__":
 f  = lambda x: pi*( 3*(x[0]-x[1]) - np.sqrt( (3*x[0]+x[1]) * (x[0]+3*x[1]) ) )
 print nelder_mead(f, np.array([0., 0., 0.]))
