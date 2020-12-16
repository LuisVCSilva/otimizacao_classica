from Metodos.interpol		import gera_polinomio
from Metodos.minBFGS		import minimiza_bfgs
from Metodos.minBuscaAleatoria	import minBuscaAleatoria
from Metodos.minFibonacci	import minimiza_fibonacci
from Metodos.minGradConjugado	import minimiza_gradiente_conjugado
from Metodos.minMaximaDescida	import minimiza_descida_maxima
from Metodos.minNelderMead	import nelder_mead
from Metodos.minNewton		import minimiza_newton
from Metodos.minPowell		import minimiza_powell
from Metodos.minSecaoAurea	import secaoAurea
from sympy import Symbol
from sympy.utilities.lambdify import lambdify, implemented_function

from funcao_objetivo import *
from plotaFuncao import *
from inspect import getsource

tol = 10**-5                      #tolerancia do algoritmo de otimizacao
intervalo = (-5.0,5.0)              #intervalo do plot
qtdePontos = 50                  #resolucao do grafico

#Questao 2
#funcoes    = [f2_1,f2_2,f2_3]
#derivadas = [df2_1,df2_2,df2_3]
#intervalos = [[0.0,3.0],[0.0,10.0],[0.5,3.5]] 

#funcoes = [f_interpolado]
#intervalos = [[0.0,10.0]]
#for questao in zip(funcoes,intervalos):
# a = array([questao[1][0]])
# b = array([questao[1][1]])
# f,f_txt = tuple(questao[0])
# res = minimiza_fibonacci(f,a,b,tol)[-1]['x2']
 
# plota1D(f,array([res,f(res)]),intervalo,qtdePontos,"Min $"+f_txt+"$ via Fibonacci",f_txt)

# res = secaoAurea(f,[a,b],tol)
# res = res[-1]['z']
# plota1D(f,array([res,f(res)]),intervalo,qtdePontos,"Min $"+f_txt+"$ via Seção Áurea",f_txt)

# x = Symbol('x')
# intervalo = [a,b]
# pontos = [(x,f([x])) for x in linspace(min(intervalo),max(intervalo),4)]
# f =      lambda x: eval(str(gera_polinomio(pontos,len(pontos)-1, [x])).replace("x","x[0]"))
# f_txt =  str(gera_polinomio(pontos,len(pontos)-1, [x]))
# res = secaoAurea(f,[min(pontos)[0],max(pontos)[0]],0.001)
# res = res[-1]['z']
 #plota1D(f,array([res,f(res)]),intervalo,qtdePontos,"Min $"+f_txt+"$ via Seção Áurea",f_txt)
#Questao 3
funcoes    = [f3_1,f3_2,f3_3]
gradientes = [df3_1,df3_2,df3_3]
hessianas  = [d2f3_1,d2f3_2,d2f3_3]
intervalos = [[-10.0,10.0],[-10.0,10.0],[-10.0,10.0]] 

for questao in zip(funcoes,gradientes,hessianas,intervalos):
 a = array([questao[3][0]])
 b = array([questao[3][1]])
 f,f_txt = tuple(questao[0])
 df = questao[1]
 d2f = questao[2]

 #res = 
 #ponto = res
 #plota2D(f,ponto,range(*intervalo),qtdePontos,"Min $"+f_txt+"$ via Busca Aleatória",f_txt)

 #res = 
 #ponto = res
 #plota2D(f,ponto,range(*intervalo),qtdePontos,"Min $"+f_txt+"$ via Seção Áurea",f_txt)

 #res = 
 #ponto = res
 #plota2D(f,ponto,range(*intervalo),qtdePontos,"Min $"+f_txt+"$ via Fibonacci",f_txt)

 #res = 
 #ponto = res
 #plota2D(f,ponto,range(*intervalo),qtdePontos,"Min $"+f_txt+"$ via Powell",f_txt)


 res = nelder_mead(f,  array([0.0,0.0]), passo=0.1, limiar_semMelhora=10e-6, max_sem_melhora=10, max_iter=0, alfa=1., gama=2., rho=-0.5, sigma=0.5)
 ponto = res
 plota2D(f,ponto,intervalo,qtdePontos,"Min $"+f_txt+"$ via Nelder Mead",f_txt)


 #res = 
 #ponto = res
 #plota2D(f,ponto,range(*intervalo),qtdePontos,"Min $"+f_txt+"$ via Gradiente Conjugado",f_txt)

 #res = 
 #ponto = res
 #plota2D(f,ponto,range(*intervalo),qtdePontos,"Min $"+f_txt+"$ via Máxima Descida",f_txt)

 #res   = minimiza_newton(f,df,d2f,x_0,max_it,tol)
 #ponto = res
 #plota2D(f,ponto,range(*intervalo),qtdePontos,"Min $"+f_txt+"$ via Newton",f_txt)

 #res = 
 #ponto = res
 #plota2D(f,ponto,range(*intervalo),qtdePontos,"Min $"+f_txt+"$ via BFGS",f_txt)
