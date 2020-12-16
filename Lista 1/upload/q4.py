import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm
from math import pi
from scipy.optimize import minimize


#minimo =~ (0.540847, 0.361168)
#maximo = n/a
f  = lambda x: -pi*(0.072)*x[0]*x[1]+(x[0]-0.5)**2 + (x[1]-0.3)**2
x0 = [-10.0,10.0]
res = minimize(f, x0, method='Powell', tol=1e-6)

xmin, xmax, xstep = -4.5, 4.5, .2
ymin, ymax, ystep = -4.5, 4.5, .2

x, y = np.meshgrid(np.arange(xmin, xmax + xstep, xstep), np.arange(ymin, ymax + ystep, ystep))
z = f([x, y])
minima = res.x
minima_ = minima.reshape(-1, 1)
fig = plt.figure(figsize=(8, 5))
ax = plt.axes(projection='3d', elev=50, azim=-50)
print(list(minima))
ax.plot_surface(x, y, z, norm=LogNorm(), rstride=1, cstride=1, edgecolor='none', alpha=.8, cmap=plt.cm.jet)
#ax.contour(x, y, z, norm=LogNorm(), rstride=1, cstride=1, edgecolor='none', alpha=.8, cmap=plt.cm.jet,n=500)
ax.text(minima[0],minima[1],f(list(minima)),s=str((minima[0],minima[1],f(list(minima)))))


ax.plot(*minima_, f(list(minima_)), 'r*', markersize=10)

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$f(x_1,x_2) = z$')

ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))

plt.show()
