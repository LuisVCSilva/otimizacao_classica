from math import sqrt
import numpy as np
import csv
from os import system
from inspect import getsource

def cria_csv(filename,res):
 csv_file = filename+".csv"
 csv_columns = res[0].keys()
 try:
     with open(csv_file, 'w') as csvfile:
         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
         writer.writeheader()
         for data in res:
             writer.writerow(data)
 except IOError:
     print("I/O error: " + filename)

def secaoAurea (f,intervalo,epsilon):
 a = [intervalo[0]]
 b = [intervalo[1]]

 k = 0
 y = []
 z = []

 y.append(a[k] + ((3-sqrt(5))/2.0) * (b[k]-a[k]))
 z.append(a[k] + ((sqrt(5)-1)/2.0) * (b[k]-a[k]))

 f_y = [f(y[k])]
 f_z = [f(z[k])]

 erro = []
 result = []
 while 1:
  erro.append((b[k]-a[k]))
  result.append((b[k]+a[k])/2.0)
  if b[k]-a[k] < epsilon:
   saida = [{"k":j,"a":a[j],"b":b[j],"y":y[j],"f(y)":f_y[j],"z":z[j],"f(z)":f_z[j],"erro":erro[j],"min":result[j]} for j in range(k+1)]
   cria_csv("Seção Áurea -- "+getsource(f).split(',')[0].split(": ")[1].replace(".",",").replace("/","\\"),saida)
   return saida

  elif f(y[k])>f(z[k]):
   a.append(y[k])
   b.append(b[k])
   y.append(z[k])
   z.append((a[k+1] + ((sqrt(5)-1)/2.0) * (b[k+1]-a[k+1])))
   f_y.append(f(y[k+1]))
   f_z.append(f(z[k+1]))
  else:
   a.append(a[k])
   b.append(z[k])
   z.append(y[k])
   y.append(a[k+1] + ((3-sqrt(5))/2.0) * (b[k+1] - a[k+1]))
   f_y.append(f(y[k+1]))
   f_z.append(f(z[k+1]))
  k = k+1


#f = lambda x: (12*x**2-16*x+8)
#intervalo = [0.0, 1.0]
#epsilon = 0.001
#res = secaoAurea(f,intervalo,epsilon)
#print(res)
#csv_file = "resultado.csv"
#csv_columns = res[0].keys()
#try:
#    with open(csv_file, 'w') as csvfile:
#        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#        writer.writeheader()
#        for data in res:
#            writer.writerow(data)
#except IOError:
#    print("I/O error") 

#system("cat resultado.csv")

