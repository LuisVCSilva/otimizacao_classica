from scipy.optimize import minimize





def solve():
 lamb = -1  #lambda inicial  #-1 porque grad(h)*grad(f)> = 0
 fobj = lambda x: (x[0]-1)**2+(x[1]-1)**2+lamb*(x[0]-x[1]-2)+rp*(x[0]-x[1]-2)**2
 h    = lambda x: x[0]-x[1]-2
 a = -10
 b = 10
 rp = 1  

 x = [1.0,1.0]

 tol         = 10**-6
 nbIteracoes = 10
 rpmax       = 10**5
 gama        = 3
 erro = 1.0
 f0 = fobj(x)
 print("{}\t{}\t{}\t{}".format("x_1","x_2","f(x)","erro"))

 for i in range(nbIteracoes):
    x = minimize(fobj, x, method="Nelder-Mead", tol=tol).x
    f1 = fobj(x)
    erro = abs(f1 - f0) 

    print("{}\t{}\t{}\t{}".format(x[0],x[1],fobj(x),erro))
    f0 = f1
    if erro <= tol:
        return x
    else:
        lamb0 = lamb
        lamb = lamb+2*rp*h(x)
        if abs (lamb-lamb0) <=tol:
            return x
        else:
            rp = gama*rp
            if(rp>rpmax):
                rp = rpmax
    if i==nbIteracoes:
        return x

res = solve()
print(res)
