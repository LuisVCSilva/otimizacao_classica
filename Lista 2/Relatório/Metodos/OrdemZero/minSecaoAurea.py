from numpy import *

def reduz_intervalo(func, xa=array([0.0]), xb=array([1.0]), \
                    max_cresc=110.0, maxiter=1000):
 razao_aurea = (1.0+sqrt(5.0))/2.0
 tol = 1e-21
 fa = func(*(xa,))
 fb = func(*(xb,))
 if (fa < fb):
  xa, xb = xb, xa
  fa, fb = fb, fa
 xc = xb + razao_aurea * (xb - xa)
 fc = func(*((xc,)))
 avaliacoesFO = 3
 iter = 0
 while (fc < fb):
  tmp1 = (xb - xa) * (fb - fc)
  tmp2 = (xb - xc) * (fb - fa)
  val = tmp2 - tmp1
  if abs(val) < tol:
   denom = 2.0 * tol
  else:
   denom = 2.0 * val
  w = xb - ((xb - xc) * tmp2 - (xb - xa) * tmp1) / denom
  wlim = xb + max_cresc * (xc - xb)
  iter += 1
  if (w - xc) * (xb - w) > 0.0:
   fw = func(*((w,)))
   avaliacoesFO += 1
   if (fw < fc):
    xa = xb
    xb = w
    fa = fb
    fb = fw
    return xa, xb, xc, fa, fb, fc, avaliacoesFO
   elif (fw > fb):
    xc = w
    fc = fw
    return xa, xb, xc, fa, fb, fc, avaliacoesFO
   w = xc + razao_aurea * (xc - xb)
   fw = func(*((w,)))
   avaliacoesFO += 1
  elif (w - wlim)*(wlim - xc) >= 0.0:
   w = wlim
   fw = func(*((w,)))
   avaliacoesFO += 1
  elif (w - wlim)*(xc - w) > 0.0:
   fw = func(*((w,)))
   avaliacoesFO += 1
   if (fw < fc):
    xb = xc
    xc = w
    w = xc + razao_aurea * (xc - xb)
    fb = fc
    fc = fw
    fw = func(*((w,)))
    avaliacoesFO += 1
  else:
   w = xc + razao_aurea * (xc - xb)
   fw = func(*((w,)))
   avaliacoesFO += 1
  xa = xb
  xb = xc
  xc = w
  fa = fb
  fb = fc
  fc = fw
 return xa, xb, xc, fa, fb, fc

def minimiza_secao_aurea (func, xa, xb, xc, xtol=0.001, maxiter=5000):
 fa,fb,fc = func(xa),func(xb),func(xc)
 tol = xtol
 avaliacoesFO = 0
 conjSecaoAurea = ((1.0+sqrt(5.0))/2.0)-1.0
 complConjSecaoAurea = 1.0 - conjSecaoAurea
 x3 = xc
 x0 = xa
 if (abs(xc - xb) > abs(xb - xa)):
  x1 = xb
  x2 = xb + complConjSecaoAurea * (xc - xb)
 else:
  x2 = xb
  x1 = xb - complConjSecaoAurea * (xb - xa)
 f1 = func(*((x1,)))
 f2 = func(*((x2,)))
 avaliacoesFO += 2
 nit = 0
 for i in range(maxiter):
  if abs(x3 - x0) <= tol * (abs(x1) + abs(x2)):
   break
  if (f2 < f1):
   x0 = x1
   x1 = x2
   x2 = conjSecaoAurea * x1 + complConjSecaoAurea * x3
   f1 = f2
   f2 = func(*((x2,)))
  else:
   x3 = x2
   x2 = x1
   x1 = conjSecaoAurea * x2 + complConjSecaoAurea * x0
   f2 = f1
   f1 = func(*((x1,)))
  avaliacoesFO += 1
  nit += 1
  xmin = x1 if f1 < f2 else x2
  ymin = f1 if f1 < f2 else f2
 return xmin

def main():
 f = lambda x: 12*x[0]**2-16*x[0]+8
 xa, xb, xc, fa, fb, fc = reduz_intervalo(f)
 res = minimiza_secao_aurea(f,xa, xb, xc)
 print({"x":res,"f(x)":f(res)})

if __name__ == "__main__":
 main()
