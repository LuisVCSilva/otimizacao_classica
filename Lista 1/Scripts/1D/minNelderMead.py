#!/usr/bin/env python

from numpy import *

def minimiza_nelder_mead(func, x0, simplex_inicial=None, xtol=1e-4, fxtol=1e-4,adaptativo=False):
    avalFO, func = [0],func
    if adaptativo:
        dim = float(len(x0))
        rho = 1
        chi = 1 + 2/dim
        psi = 0.75 - 1/(2*dim)
        sigma = 1 - 1/dim
    else:
        rho = 1
        chi = 2
        psi = 0.5
        sigma = 0.5

    nonzdelt = 0.05
    zdelt = 0.00025

    x0 = asfarray(x0).flatten()

    if simplex_inicial is None:
        N = len(x0)

        sim = zeros((N + 1, N), dtype=x0.dtype)
        sim[0] = x0
        for k in range(N):
            y = array(x0, copy=True)
            if y[k] != 0:
                y[k] = (1 + nonzdelt)*y[k]
            else:
                y[k] = zdelt
            sim[k + 1] = y
    else:
        sim = asfarray(simplex_inicial).copy()
        if sim.ndim != 2 or sim.shape[0] != sim.shape[1] + 1:
            raise ValueError("O simplex inicial deve ser uma matriz com dimensoes (N+1,N)")
        if len(x0) != sim.shape[1]:
            raise ValueError("Tamanho do simplex inicial nao eh compativel com tamanho do chute inicial (x0)")
        N = sim.shape[1]


    vetores = [sim[0]]



    maxiter = N * 200
    maxfun = N * 200

    one2np1 = list(range(1, N + 1))
    fsim = zeros((N + 1,), float)

    for k in range(N + 1):
        fsim[k] = func(sim[k])

    ind = argsort(fsim)
    fsim = take(fsim, ind, 0)

    sim = take(sim, ind, 0)#ordenacao do simplex, tal que a linha 0 possua o menor valor na funcao

    iterations = 1

    while (avalFO[0] < maxfun and iterations < maxiter):
        if (max(ravel(abs(sim[1:] - sim[0]))) <= xtol and
                max(abs(fsim[0] - fsim[1:])) <= fxtol):
            break

        xbar = add.reduce(sim[:-1], 0) / N
        xr = (1 + rho) * xbar - rho * sim[-1]
        fxr = func(xr)
        encolhe = 0

        if fxr < fsim[0]:
            xe = (1 + rho * chi) * xbar - rho * chi * sim[-1]
            fxe = func(xe)

            if fxe < fxr:
                sim[-1] = xe
                fsim[-1] = fxe
            else:
                sim[-1] = xr
                fsim[-1] = fxr
        else:  # fsim[0] <= fxr
            if fxr < fsim[-2]:
                sim[-1] = xr
                fsim[-1] = fxr
            else:  # fxr >= fsim[-2]
                # Encolhe
                if fxr < fsim[-1]:
                    xc = (1 + psi * rho) * xbar - psi * rho * sim[-1]
                    fxc = func(xc)

                    if fxc <= fxr:
                        sim[-1] = xc
                        fsim[-1] = fxc
                    else:
                        encolhe = 1
                else:
                    # Encolhe internamente
                    xcc = (1 - psi) * xbar + psi * sim[-1]
                    fxcc = func(xcc)

                    if fxcc < fsim[-1]:
                        sim[-1] = xcc
                        fsim[-1] = fxcc
                    else:
                        encolhe = 1

                if encolhe:
                    for j in one2np1:
                        sim[j] = sim[0] + sigma * (sim[j] - sim[0])
                        fsim[j] = func(sim[j])

        ind = argsort(fsim)
        sim = take(sim, ind, 0)
        fsim = take(fsim, ind, 0)
        iterations += 1
        vetores.append(sim[0])

    x = sim[0]
    fval = min(fsim)

    if avalFO[0] >= maxfun:
        print("Algoritmo falhou: numero maximo de avaliacoes da funcao foi atingido")
    elif iterations >= maxiter:
        print("Algoritmo falhou: numero maximo de iteracoes foi atingido")
    else:
        1
        print({'x':x,'f(x)':fval})
        print("Iteracoes: %d" % iterations)
        print("Avaliacoes da FO: %d" % avalFO[0])
    result = vetores
    return x

def main():
 f = lambda x: (12*x**2-16*x+8)
 res = minimiza_nelder_mead(f, [0.0],adaptativo=False)
 print({'x':res,'f(x)':f(res)})

if __name__ == "__main__":
 main()
