from numpy import *

def minimiza_descida_maxima(f, grad, x_inicial, h, max_it, tol):
  x = x_inicial
  x_anterior = x
  for i in xrange(max_it):
    direcao_descida = -grad(x)
    alfa = h
    x = x + alfa * direcao_descida
    if linalg.norm(x - x_anterior) < tol:
      break
    x_anterior = x
  return x

#def main():
# f = lambda x: 12*x[0]**2-16*x[0]+8
# df = lambda x: 24*x[0]-16
# x_0 = array([0.0])
# h = 1E-5
# tol = 1E-10
# max_it = 100000000
# res = minimiza_descida_maxima(f,df,x_0,h,max_it,tol)
# print({'x':res,'f(x)':f(res)})
 
#if __name__ == "__main__":
# main()
