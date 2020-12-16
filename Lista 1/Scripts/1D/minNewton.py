#!/usr/bin/env python

from numpy import *
from scipy.optimize import rosen, rosen_der, rosen_hess, line_search

_epsilon = 1E-12

def approx_fhess_p(x0, p, fprime, epsilon, *args):
    f2 = fprime(*((x0 + epsilon*p,) + args))
    f1 = fprime(*((x0,) + args))
    return (f2 - f1) / epsilon

def _minimize_newtoncg(fun, x0 , jac=None, hess=None, xtol=1e-5, eps=_epsilon):

    f = fun
    fprime = jac
    fhess = hess
    avextol = xtol
    epsilon = eps

    x0 = asarray(x0).flatten()
    maxiter = len(x0)*200
    cg_maxiter = 20*len(x0)

    xtol = len(x0) * avextol
    update = [2 * xtol]
    xk = x0
    allvecs = [xk]
    k = 0
    gfk = None
    old_fval = f(x0)
    old_old_fval = None
    float64eps = finfo(float64).eps
    while add.reduce([abs(x) for x in update]) > xtol:
        b = -fprime(xk)
        maggrad = add.reduce(abs(b))
        eta = min([0.5, sqrt(maggrad)])
        termcond = eta * maggrad
        xsupi = zeros(len(x0), dtype=x0.dtype)
        ri = -b
        psupi = -ri
        i = 0
        dri0 = dot(ri, ri)

        if fhess is not None:
            A = fhess(*(xk,))

        for k2 in xrange(cg_maxiter):
            if add.reduce(abs(ri)) <= termcond:
                break
            if fhess is None:
                if fhess_p is None:
                    Ap = approx_fhess_p(xk, psupi, fprime, epsilon)
                else:
                    Ap = fhess_p(xk, psupi)
            else:
                Ap = dot(A, psupi)
            Ap = asarray(Ap).squeeze()
            curv = dot(psupi, Ap)
            if 0 <= curv <= 3 * float64eps:
                break
            elif curv < 0:
                if (i > 0):
                    break
                else:
                    xsupi = dri0 / (-curv) * b
                    break
            alphai = dri0 / curv
            xsupi = xsupi + alphai * psupi
            ri = ri + alphai * Ap
            dri1 = dot(ri, ri)
            betai = dri1 / dri0
            psupi = -ri + betai * psupi
            i = i + 1
            dri0 = dri1

        pk = xsupi
        gfk = -b
        alphak, fc, gc, old_fval, old_old_fval, gfkp1 = line_search(f, fprime, xk, pk, gfk,old_fval, old_old_fval)
        update = alphak * pk
        xk = xk + update
        allvecs.append(xk)
        k += 1
    return allvecs[-1]



def main():
 f = lambda x: (12*x**2-16*x+8)
 x0 = [0.8, 1.2, 0.7]
 print(rosen_hess)
 res = _minimize_newtoncg(fun=rosen, x0=x0, jac=rosen_der, hess=rosen_hess)
 print(res)

if __name__ == "__main__":
 main()
