from scipy import optimize
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def connectpoints(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')

def func(x):
 return (-1) * (4*x[0]*x[1])

bnds=((0,100),(0,5))

cons=({'type':'eq','fun':lambda x:((x[0]**2)/4)+x[1]**2-4})
x0=[1,1]
res= optimize.minimize(func,x0,method='SLSQP',bounds=bnds,constraints=cons)
print(res.x)

x = np.linspace(-10.0, 10.0, 100)
y = np.linspace(-10.0, 10.0, 100)
X, Y = np.meshgrid(x,y)
F = (X**2)/4 + (Y**2)/4 - 4.0
plt.grid()
plt.contour(X,Y,F,[0])

x = [2.0*sqrt(2),2.0*sqrt(2)]
y = [2.0*sqrt(2),-2.0*sqrt(2)]
plt.plot(x,y, 'ro')
connectpoints(x,y,0,1)

x = [2.0*sqrt(2),-2.0*sqrt(2)]
y = [2.0*sqrt(2),2.0*sqrt(2)]
plt.plot(x,y, 'ro')
connectpoints(x,y,0,1)


x = [-2.0*sqrt(2),-2.0*sqrt(2)]
y = [-2.0*sqrt(2),2.0*sqrt(2)]
plt.plot(x,y, 'ro')
connectpoints(x,y,0,1)

x = [2.0*sqrt(2),-2.0*sqrt(2)]
y = [-2.0*sqrt(2),-2.0*sqrt(2)]
plt.plot(x,y, 'ro')
connectpoints(x,y,0,1)


#connectpoints(x,y,0,1)

plt.axis('equal')
plt.show()
