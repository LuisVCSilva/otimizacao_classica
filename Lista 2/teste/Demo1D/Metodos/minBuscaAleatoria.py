from numpy import *
from sys import argv

def minBuscaAleatoria (f,a,b,tol,max_it,isAleatorio):
 tol = tol**(-1.0)
 x_otimo = 0.0
 espacoBusca = linspace(a,b,tol)
 if isAleatorio:#nao garante minimo
  for i in range(max_it):
   indice = random.choice(espacoBusca.shape[0], len(a), replace=False)
   elemento_aleatorio = espacoBusca[indice]
   x_otimo = elemento_aleatorio if x_otimo==None or f([elemento_aleatorio])<f([x_otimo]) else x_otimo
 else:#garante um pouco mais
  espacoBusca = [({'x':x,'f(x)':f([x])}) for x in linspace(a,b,tol)]
  x_otimo = sorted(espacoBusca, key = lambda i: i['f(x)'])[0]['x'] 
 return x_otimo
  

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
