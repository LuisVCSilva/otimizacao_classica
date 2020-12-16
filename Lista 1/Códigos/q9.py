import numpy as np
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt

f = lambda x: np.pi*x[0]*x[1]

h_1 = lambda x: 2*x[0] + x[1] - 8
h_2 = lambda x: (x[0]-1)**2 + (x[1]-4)**2 - 4 

g_1 = lambda x: x[0] + x[1]-7
g_2 = lambda x: x[0] - 0.25*x[1]**2


lim = 100.0
xlist = np.linspace(-lim, lim, 1000)
ylist = np.linspace(-lim, lim, 1000)
X, Y = np.meshgrid(xlist, ylist)
_f = f([X,Y])
#_h1 = h_1([X,Y])
#_h2 = h_2([X,Y])

#_g1 = g_1([X,Y])
#_g2 = g_2([X,Y])

plt.figure()
__f = plt.contour(X, Y, _f,colors=["green"])

#pontos encontrados
plt.plot(0.7371, 0.0340,'bo');
plt.plot(-0.0852, 0.1299,'bo');


#plt.clabel(__f, inline=True, fontsize=10)
plt.title('Contour Plot')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.show()
