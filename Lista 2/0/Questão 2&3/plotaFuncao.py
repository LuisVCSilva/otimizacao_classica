from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm
from scipy.signal import argrelextrema

def plota1D(f,ponto,intervalo,qtdePontos,titulo,legenda):  
 x = linspace(min(intervalo),max(intervalo),qtdePontos) 
 y = f([x])
 plot(x, y)
 plot([ponto[0]], [ponto[1]], 'ro')
 print(ponto)
 annotate(str(ponto), (ponto.reshape(1, -1)[0]))
 legend(['$'+legenda+'$'])
 title(titulo)
 savefig(titulo.replace("/","")+".png")
 show()

def plota2D(f,ponto,intervalo,qtdePontos,titulo,legenda):
 xmin, xmax, xstep = intervalo[0], intervalo[1], 1.0/(qtdePontos+0.0)
 ymin, ymax, ystep = intervalo[0], intervalo[1], 1.0/(qtdePontos+0.0)
 x, y = np.meshgrid(np.arange(xmin, xmax + xstep, xstep), np.arange(ymin, ymax + ystep, ystep))
 z = f([x, y])

 fig = figure(figsize=(8, 5))
 ax = axes(projection='3d', elev=50, azim=-50)
 ax.plot_surface(x, y, z, norm=LogNorm(), rstride=1, cstride=1, edgecolor='none', alpha=.8, cmap=cm.jet)


 minima = [ponto[0]]
 minima_ = [pt.reshape(-1, 1) for pt in minima]
 for pt in zip(minima_,minima):
  ax.plot(*pt[0], f(list(pt[0])), 'r*', markersize=10)
  ax.text(pt[1][0],pt[1][1],f(list(pt[1])),s=str(( round(pt[1][0],3), round(pt[1][1],3), round(f(list(pt[1])),3)  )))

 ax.set_xlabel('$x_1$')
 ax.set_ylabel('$x_2$')
 ax.set_zlabel('$f(x_1,x_2) = z$')

 ax.set_xlim((xmin, xmax))
 ax.set_ylim((ymin, ymax))
 show()

 #x = linspace(min(intervalo),max(intervalo),qtdePontos)
 #y = linspace(min(intervalo),max(intervalo),qtdePontos)
 #X, Y = np.meshgrid(x, y)
 #Z = f([X,Y])
 #figure()
 #print(ponto)
 #plot([ponto[0]], [ponto[1]], 'ro')
 #annotate(str(ponto), ponto[0])
 #cp = contour(X, Y, Z)
 #clabel(cp, inline=True, fontsize=10)
 #xlabel('$x_1$')
 #ylabel('$x_2$')
 #legend(['$'+legenda+'$'])
 #title(titulo)
 #savefig(titulo.replace("/","")+".png")
 #show()
