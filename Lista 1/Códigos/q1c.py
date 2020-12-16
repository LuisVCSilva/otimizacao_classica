from numpy import *
import matplotlib.pyplot as plt
 

f = lambda theta: (1250 - 1250*cos(radians(theta))) - 250*sin(radians(theta)) #energia potencial minima
theta = linspace(0.0,45.0,450)

plt.plot(theta,f(theta),label='f(theta)',linewidth=1)
plt.xlabel('theta')
plt.ylabel('f(theta)')
plt.ylim()
plt.xlim(0.0,45)
x = 11.31
plt.plot(x, f(x), 'bo')
plt.grid(color='k', linestyle='--', linewidth=0.5)
plt.show()
