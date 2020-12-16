# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
f   = lambda x: (x[0]-3)**2 + (x[1]-2)**2

h_1 = lambda x: 2*x[0]+x[1] - 8
h_2 = lambda x: (x[0]-1)**2 + (x[1]-4)**2 - 4

g_1 = lambda x: x[0] + x[1] - 7
g_2 = lambda x: x[0] - 0.25*x[1]**2

x = np.array(range(-100,100))
y = np.array(range(-100,100))
y = f([x,y])
plt.plot(x,y,label='f')

y = h_1([x,y])
plt.plot(x,y,label='h_1')

y = h_2([x,y])
plt.plot(x,y,label='h_2')

y = g_1([x,y])
plt.plot(x,y,label='g_1')

y = g_2([x,y])
plt.plot(x,y,label='g_2')


plt.xlabel('x')
plt.ylabel('y')

# Add a grid
plt.grid(alpha=.4,linestyle='--')

# Add a Legend
plt.legend()

# Show the plot
plt.show()
#f = 2x+y=8 
#g_1 = (x-1)^2 + (y-4)^2 = 4 and x+y<=7 and x-0.25y^2 <=0 and 0<=x<=10 and 0<=y<=10
