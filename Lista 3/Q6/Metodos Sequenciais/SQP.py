from numpy import *
from scipy.optimize import minimize
from random import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import *

'''
O SQP é um modela um problema de otimização não linear para uma dada iteração x_k, em um
subproblema de Programação Quadrática (QP), uma vez resolvido esta instância de problema,
esta solução é usada para construir uma nova iteração x_k + 1. Eventualmente x_k
converge para x*.
'''
def registro (x):
 print((x[0],x[1],f(x)))

xMin = -5.0
xMax =  5.0
bnds=((xMin,xMax),(xMin,xMax))


f  = lambda x: (-1.0) * ((9.0-(x[0]-3.0)**2) * ((x[1]**3)/(27.0*sqrt(3.0))))

h1 = lambda x : x[0]/sqrt(3) - x[1]
h2 = lambda x : 6 - (x[0]+ sqrt(3) * x[1])
h3 = lambda x : x[0]
bnds=((0,100),(0,5))
cons=(\
     {'type':'ineq','fun':h1},\
     {'type':'ineq','fun':h2},\
     {'type':'ineq','fun':h3})
x0 = array([1.0, 1.0])
res= minimize(f,x0,method='SLSQP',bounds=bnds,constraints=cons,callback=registro,options={'disp':True})

minimo = [res.x[0],res.x[1],res.fun]#[res.x[0],res.x[1],res.fun] 


fig = figure()
ax  = fig.add_subplot(111, projection='3d')

X = np.arange(xMin, xMax, 0.05)
Y = np.arange(xMin, xMax, 0.05)
X, Y = np.meshgrid(X, Y)
Z = f([X,Y])

superficie = ax.plot_surface(X, Y, Z, cmap=cm.hot,linewidth=1.0, antialiased=True,alpha=0.8)
ax.scatter(minimo[0],minimo[1],minimo[2],marker=["o","^"][0],c=["r","b"][1],s=10)
ax.text(minimo[0],minimo[1],minimo[2],s=str(minimo))
show()
