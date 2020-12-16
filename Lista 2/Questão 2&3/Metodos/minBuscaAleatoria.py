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
  

#def main():
# f = lambda x: (12*x[0]**2-16*x[0]+8)
# a = [0.0]
# b = [10.0]
# tol = 0.0001
# max_it = 1000
# res = minBuscaAleatoria(f,a,b,tol,max_it,False)
# print({'x':res,'f(x)':f(res)})


#if __name__ == "__main__":
# main()
