from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import *
from scipy.optimize import minimize

penalidade_interior = lambda x: f(x)+rp*sum([(-1/g(x) if g(x)<=(-C*(rp)**a) else -(2*(-C*(rp)**a)-g(x))/((-C*(rp)**a)**2)) for g in restricoes])
penalidade_exterior = lambda x: f(x)+rp*sum([max(0,g(x))**2 for g in restricoes])

C = 0.15
a = 0.5

global metodo
metodo = None

global x0
x0     = None

global max_it
max_it = None

global tol
tol    = None

global gama
gama   = None

global rp
rp     = None

global f
f      = None

global restricoes
restricoes = None

global _restricoes_igualdade
restricoes_igualdade = None

global _restricoes_desigualdade
restricoes_desigualdade = None


global modo
modo = None

def set_param (problema):
 global metodo
 metodo = problema["metodo"]

 global x0
 x0 = problema["x0"]

 global max_it
 max_it = problema["max_it"]

 global tol
 tol    = problema["tol"]

 global gama
 gama   = problema["gama"]

 global rp
 rp     = problema["rp"]

 global f
 f      = problema["f"]

 global restricoes
 restricoes = problema["restricoes"]
 
 global restricoes_igualdade
 restricoes_igualdade = problema["restricoes_igualdade"]

 global restricoes_desigualdade
 restricoes_desigualdade = problema["restricoes_desigualdade"]


 global modo
 modo = problema["modo"]

def MPFI():
 global gama
 gama = 1/(10.0*gama)
 f_obj = lambda x: f(x)+rp*sum([(-1/g(x) if g(x)<=(-C*(rp)**a) else -(2*(-C*(rp)**a)-g(x))/((-C*(rp)**a)**2)) for g in restricoes])
 x = x0

 serie_erro = []
 serie_fx = []

 print("{}\t{}\t{}\t{}".format("x_1","x_2","f(x)","erro"))
 for i in range(max_it):
    x_ant=x
    x=minimize(f_obj, x, method=metodo, tol=tol).x
    erro = abs(f_obj(x)-f_obj(x_ant))
    serie_erro.append(erro)
    serie_fx.append(f_obj(x))
    
    print("{}\t{}\t{}\t{}".format(x[0],x[1],f(x),erro))
    if erro<=tol:
        plotaConvergencia(serie_erro,serie_fx)
        return x
    global rp
    rp = gama*rp

def MPFE():
 f_obj = lambda x: f(x)+rp*sum([max(0,g(x))**2 for g in restricoes_desigualdade] + rp*sum(h(x) for h in restricoes_igualdade))
 xant = x0

 serie_erro = []
 serie_fx = []

 print("{}\t{}\t{}\t{}".format("x_1","x_2","f(x)","erro"))
 for i in range(max_it):
    xatual=minimize(f_obj, xant, method=metodo, tol=tol).x
    erro = abs(f_obj(xatual)-f_obj(xant))
    serie_erro.append(erro)
    serie_fx.append(f_obj(xatual))


    print("{}\t{}\t{}\t{}".format(xatual[0],xatual[1],f(xatual),erro))
    if erro<=tol:
        plotaConvergencia(serie_erro,serie_fx)
        return xatual
    else:
        xant = xatual
        global rp        
        rp = gama*rp

def LA():
 a = -10
 b = 10
 rp = 1 
 x = [1.0, 1.0]
 lamb1 = -1
 lamb2 = -1
 tol = 10**-6
 nbIteracoes = 100
 rpmax = 10**5
 gama = 3.0
 
 h  = lambda x: x[0]-x[1]-2
 ps = lambda x: max(x[0]+x[1]-0.5,(-lamb1/(2*rp)))
 
 f  = lambda x: (x[0]-1)**2+(x[1]-1)**2+lamb1*(ps(x))+rp*(ps(x))**2+lamb2*(h(x))+rp*(h(x))**2
 
 f0 = f(x)
 erro = 1 
 
 
 print("{}\t{}\t{}\t{}".format("x_1","x_2","f(x)","erro")) 
 for i in range(nbIteracoes):
     x = minimize (f, x, method="Nelder-Mead", tol=tol).x
     f1 = f(x) 
     erro = abs(f1-f0)
     f0 = f1
     print("{}\t{}\t{}\t{}".format(x[0],x[1],f(x),erro))
     if erro<=tol:  
         return x
         break
     else:
         lamb10 = lamb1
         lamb20 = lamb2
         lamb1 = lamb1+2*rp*ps(x)
         lamb2 = lamb2+2*rp*h(x)  # atualização do lambda
         if abs(lamb1-lamb10) <= tol and abs(lamb2-lamb20) <= tol: 
             return x
             break
         else:
             rp = gama*rp 
             if rp>rpmax: 
                 rp = rpmax
     if i==nbIteracoes:
         return x

def plota (xMin,xMax,h,pontos):
   fig = figure()
   ax  = fig.add_subplot(111, projection='3d')

   X = np.arange(xMin, xMax, h)
   Y = np.arange(xMin, xMax, h)
   X, Y = np.meshgrid(X, Y)
   Z = f([X,Y])


   superficie = ax.contour(X, Y, Z, cmap=cm.hot, antialiased=True,alpha=0.8)
   for ponto in pontos:
      ax.scatter(ponto[0],ponto[1],ponto[2],marker=["o","^"][0],c=["r","b"][1],s=10)
      ax.text(ponto[0],ponto[1],ponto[2],s=str(ponto))
   savefig("contorno.png")

   superficie = ax.plot_surface(X, Y, Z, cmap=cm.hot,linewidth=1.0, antialiased=True,alpha=0.8)
   for ponto in pontos:
      ax.scatter(ponto[0],ponto[1],ponto[2],marker=["o","^"][0],c=["r","b"][1],s=10)
      ax.text(ponto[0],ponto[1],ponto[2],s=str(ponto))
   savefig("superficie.png")

def plotaConvergencia (x,y):
 plot(range(len(x)),x,'-g^',label = "Erro")
 plot(range(len(x)),y,'-r^',label = "f(x)")
 xlabel('Iteração')
 ylabel('Valor')
 legend()
 suptitle("Min f(x) = " + str(y[-1]) + "\nIterações = " + str(len(x)) + "\nErro = " + str(x[-1]),fontsize=10)
 savefig("convergencia.png")

def solve ():
 x = modo()
 return [x[0],x[1],f(x)]
