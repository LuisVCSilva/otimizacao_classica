from numpy import *
from sys import argv

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

    Hk1 = (I - rho_k * outer(sk, yk)).dot(Hk).dot(I - rho_k * outer(yk, sk)) + rho_k * outer(sk, sk)

    if linalg.norm(xk1 - xk) < tol:
      xk = xk1
      break

    Hk = Hk1
    xk = xk1

  return xk.ravel()


def main(args):
 f  = lambda x: eval(args[0])
 df = lambda x: eval(args[1])
 x_inicial = array(eval(args[2]))
 max_it = eval(args[3])
 tol    = eval(args[4])
 res = minimiza_bfgs(f, df, x_inicial,max_it,tol)
 print({"x":res,"f(x)":f(res)})

if __name__ == "__main__":
 main(argv[1:])