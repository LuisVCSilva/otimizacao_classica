#!/usr/bin/env python

from sympy import Matrix, Symbol, zeros
from sympy.core.compatibility import range
import sys


def combina (n, k):
    if k == 0:
        return [[]]
    combs = [[i] for i in range(n)]
    for i in range(k - 1):
        curr = []
        for p in combs:
            for m in range(p[-1], n):
                curr.append(p + [m])
        combs = curr
    return combs

def gera_simbolo (simbolo_str):
    n = 0
    while True:
        yield Symbol("%s_%d" % (simbolo_str, n))
        n += 1

def vandermonde (grau, dim=1, simbolos='a b c d'):
    simbolos = simbolos.split()
    n = len(simbolos)
    if n < dim:
        novos_simbolos = []
        for i in range(dim - n):
            j, rem = divmod(i, n)
            novos_simbolos.append(simbolos[rem] + str(j))
        simbolos.extend(novos_simbolos)
    termos = []
    for i in range(grau + 1):
        termos.extend(combina(dim, i))
    posto = len(termos)
    V = zeros(posto)
    geradores = [gera_simbolo(simbolos[i]) for i in range(dim)]
    todos_simbolos = []
    for i in range(posto):
        linha_simbolos = [next(g) for g in geradores]
        todos_simbolos.append(linha_simbolos)
        for j, termo in enumerate(termos):
            v_entry = 1
            for k in termo:
                v_entry *= linha_simbolos[k]
            V[i*posto + j] = v_entry
    return V, todos_simbolos, termos

def gera_polinomio (pontos, grau, simbolos):
    qtde_pts = len(pontos)
    dim = len(pontos[0]) - 1
    V, simb_temp, termos = vandermonde(grau, dim)
    subs_dict = {}
    for j in range(dim):
        for i in range(qtde_pts):
            subs_dict[simb_temp[i][j]] = pontos[i][j]
    V_pts = V.subs(subs_dict)
    V_inv = V_pts.inv()
    coeficientes = V_inv.multiply(Matrix([pontos[i][-1] for i in range(qtde_pts)]))
    f = 0
    for j, termo in enumerate(termos):
        t = 1
        for k in termo:
            t *= simbolos[k]
        f += coeficientes[j]*t
    return f




def main():
 x = Symbol('x')
 pontos = [(0, 3), (1, 2), (2, 3)]
 print("f(x) = " + str(gera_polinomio(pontos, len(pontos)-1, [x])))
 
if __name__ == "__main__":
 main()
