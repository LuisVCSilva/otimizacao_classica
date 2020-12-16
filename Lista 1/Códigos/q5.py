import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm
from math import pi,sqrt
from scipy.optimize import minimize


#minimo =~ (0.540847, 0.361168)
#maximo = n/a
f  = lambda x: x[0] + 1/x[0] + x[1] + 1/x[1]
x0 = [-10.0,10.0]
bnds = ((0.0, 1.0),(0.0, 1.0))
#usando metodo truncado de newton para achar máximo e mínimo da função tal que (0.0, 0.0)<=(x, y)<=(1.0, 1.0)
pts = [np.array([1,1]),np.array([-1,-1])]
xmin, xmax, xstep = -10.0, 10.0, .2
ymin, ymax, ystep = -10.0, 10.0, .2

#força bruta
#x = np.arange(xmin, xmax, xstep)
#y = np.arange(ymin, ymax, ystep)
#xx, yy = np.meshgrid(x, y, sparse=True)
#z = f([xx,yy])
#print((argrelextrema(z,np.greater)))
#h = plt.contourf(x,y,z)

x, y = np.meshgrid(np.arange(xmin, xmax + xstep, xstep), np.arange(ymin, ymax + ystep, ystep))
z = f([x, y])
minima = pts
minima_ = [pt.reshape(-1, 1) for pt in minima]
fig = plt.figure(figsize=(8, 5))
ax = plt.axes(projection='3d', elev=50, azim=-50)
#print(list(minima))
ax.plot_surface(x, y, z, norm=LogNorm(), rstride=1, cstride=1, edgecolor='none', alpha=.8, cmap=plt.cm.jet)
#ax.contour(x, y, z, norm=LogNorm(), rstride=1, cstride=1, edgecolor='none', alpha=.8, cmap=plt.cm.jet,n=500)
#ax.contourf(x,y,z)

#computar o vetor de descida maxima depois
#ax.arrow(0, 0, 0.5, 0.5, head_width=0.05, head_length=0.01, fc='k', ec='k')

for pt in zip(minima_,minima):
 ax.plot(*pt[0], f(list(pt[0])), 'r*', markersize=10)
 ax.text(pt[1][0],pt[1][1],f(list(pt[1])),s=str(( round(pt[1][0],3), round(pt[1][1],3), round(f(list(pt[1])),3)  )))



ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$f(x_1,x_2) = z$')

ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))

plt.show()
