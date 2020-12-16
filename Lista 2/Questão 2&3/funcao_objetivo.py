from numpy import *

#Q2A
f2_1  = lambda x: 3*x[0]**2-5*x[0],"3 x_1^2-5 x_1"								#0<=x<=3	min x = 5/6
df2_1 = lambda x: 6*x[0]-5,"6 x_1 - 5"

#Q2B
f2_2  = lambda x: (x[0]-3)**2,"(x_1-3)^2"									#0=<x<=10	min x = 3
f_interpolado = lambda x:0.327952853053811*x[0]**3 - 1.50192605267319*x[0]**2 + 1.50574446629699*x[0] + 0.0998334166468282,"0,327*x_1^3 - 1,501*x_1^2 + 1,505*x_1 + 0,099"

df2_2 = lambda x: 2*x[0]-6,"2 x_1-6"

#Q2C
f2_3  = lambda x: (sin(0.1+2*x[0]))/(1+x[0]),"\\frac{(\sin(0.1+2 x_1))}{(1+x_1)}"						#0.5<=x<=3.5	min x = 2.22939
df2_3 = lambda x: (2*(1 + x[0])*cos(0.1 + 2*x[0]) - sin(0.1 + 2*x[0]))/((1 + x[0])**2),"\\frac{(2 (1 + x) \cos(0.1 + 2 x) - \sin(0.1 + 2 x))}{(1 + x)^2}"
#x_1^2 - 3 x_1 x_2 + 4 x_2^2 + x_1 - x_2


#Q3A
f3_1   = lambda x: x[0]**2 - 3*x[0]*x[1] + 4*x[1]**2 + x[0] - x[1],"x_1^2 - 3 x_1 x_2 + 4 x_2^2 + x_1 - x_2"		#min x_1,x_2 = (-5/7, -1/7)
df3_1  = lambda x: array([lambda x:2*x[0] - 3*x[1] + 1,lambda x: -3*x[0] + 8*x[1] - 1])#gradiente
d2f3_1 = lambda x: array([[2,-3],[-3,8]])#hessiana

#Q3B
f3_2   = lambda x: 6*x[0]**2 + 2*x[1]**2 - 6*x[0]*x[1] - x[0] - 2*x[1],"6 x_1^2 + 2 x_2^2 - 6 x_1 x_2 - x_1 - 2 x_2" 	#min x_1,x_2 = (4/3, 5/2)
df3_2  = lambda x: array([lambda x: 12*x[0] - 6*x[1] - 1,lambda x: -6*x[0] + 4*x[1] - 2])#gradiente
d2f3_2 = lambda x: array([[12,-6],[-6,4]])#hessiana

#Q3C
f3_3   = lambda x: x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1] + x[1]**2,"x_1 - x_2 + 2 x_1^2 + 2 x_1 x_2 + x_2^2"		#min x_1,x_2 = (-1,3/2)
df3_3  = lambda x: array([4*x[0] + 2*x[1] + 1 ,2*x[0] + 2*x[1] - 1])#gradiente
d2f3_3 = lambda x: array([[4,2],[2,2]])#hessiana
