from numpy import *

def minimiza_gradiente_conjugado(f, df, x0, max_it, tol):
  xk = x0
  fk = f(xk)
  gk = df(xk)
  pk = -gk
  for i in range(max_it):
    alfa = 0.01
    xk1 = xk + alfa * pk
    gk1 = df(xk1)
    beta_k1 = dot(gk1, gk1) / dot(gk, gk)
    pk1 = -gk1 + beta_k1 * pk
    if linalg.norm(xk1 - xk) < tol:
      xk = xk1
      break
    xk = xk1
    gk = gk1
    pk = pk1
  return xk

def main():
 f  = lambda x: (12*x[0]**2-16*x[0]+8)
 df = lambda x: (24*x[0]-16)
 x_inicial = array([0.0])
 tol = 1e-4
 max_it = 1000
 x = minimiza_gradiente_conjugado(f, df, x_inicial,max_it=max_it, tol=tol)
 print({'x':x,'f(x)':f(x)})

if __name__ == '__main__':
 main()
