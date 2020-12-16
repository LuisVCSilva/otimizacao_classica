#!/usr/bin/env python

import sys


def minimiza_descida_maxima (f,df,x_n,h,tol,max_it):
 for i in range(max_it):
  x_atual = x_n
  x_n = x_atual - h * df(x_atual)
  descida = x_n - x_atual
  if abs(descida) <= tol:
   break
 return x_n

def main():
 f = lambda x: 12*x**2-16*x+8
 df = lambda x: 24*x-16
 x_n = 0.0
 h = 1E-5
 tol = 1E-5
 max_it = 10000
 res = minimiza_descida_maxima(f,df,x_n,h,tol,max_it)
 print({'x':res,'f(x)':f(res)})
 
if __name__ == "__main__":
 main()
