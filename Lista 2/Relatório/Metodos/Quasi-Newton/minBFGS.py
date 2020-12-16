from numpy import *

def minimiza_bfgs(f, df, x_inicial, max_it, tol):
  xk = x_inicial
  I = eye(xk.size)
  Hk = I

  for i in range(max_it):
    direcao_descida_1 = df(xk)
    direcao_descida_2 = -Hk.dot(direcao_descida_1)

    alfa = 0.1

    xk1 = xk + alfa * direcao_descida_2
    direcao_descida_1_1 = df(xk1)

    sk = xk1 - xk
    yk = direcao_descida_1_1 - direcao_descida_1

    rho_k = 1.0 / yk.dot(sk)

    Hk1 = (I - rho_k * outer(sk, yk)).dot(Hk). \
    dot(I - rho_k * outer(yk, sk)) + rho_k * outer(sk, sk)

    if linalg.norm(xk1 - xk) < tol:
      xk = xk1
      break

    Hk = Hk1
    xk = xk1

  return xk.ravel()


def main():
 f  = lambda x: 12*x[0]**2-16*x[0]+8
 df = lambda x: 24*x[0]-16
 x_inicial = array([0.0])
 max_it = 10000
 tol    = 0.00001 
 res = minimiza_bfgs(f, df, x_inicial,max_it,tol)
 print({"x":res,"f(x)":f(res)})

if __name__ == "__main__":
 main()
