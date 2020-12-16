from numpy import *


def minimiza_descida_maxima(f, grad, x_inicial, h, max_it, tol):
  x = x_inicial
  x_anterior = x
  for i in range(max_it):
    direcao_descida = grad(x)
    alfa = h
    x = x + alfa * direcao_descida
    if linalg.norm(x - x_anterior) < tol:
      break
    x_anterior = x
  return x

def main():
 f  = lambda x: x[0]**2 - 3*x[0]*x[1] + 4*x[1]**2 + x[0] - x[1],"x_1^2 - 3 x_1 x_2 + 4 x_2^2 + x_1 - x_2"		#min x_1,x_2 = (-5/7, -1/7)
 df = lambda x: array([2*x[0] - 3*x[1] + 1,-3*x[0] + 8*x[1] - 1])
 x_0 = array([0.0,0.0])
 h = 1E-3
 tol = 1E-3
 max_it = 10000
 res = minimiza_descida_maxima(f,df,x_0,h,max_it,tol)
 print(res)
 
if __name__ == "__main__":
 main()
