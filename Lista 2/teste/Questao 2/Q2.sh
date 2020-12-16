#Questao 2 - Alternativa A
#3 x_1^2-5 x_1						0<=x<=3	min x = 5/6
echo "Q2 - A"
echo "Min 3 x_1^2-5 x_1"
echo " --- Secao Aurea"
python3 Metodos/minSecaoAurea.py    "3*x[0]**2-5*x[0]"   "[0.0,    3.0]"   "0.001"
echo " --- Fibonacci"
python Metodos/minFibonacci.py      "3*x[0]**2-5*x[0]"   "[0.0]" "[3.0]"   "0.001"

echo ""
echo ""
echo ""
#Questao 2 - Alternativa B
#(x[0]-3)**2,"(x_1-3)^2"				0=<x<=10 min x = 3
echo "Q2 - B"
echo "Min (x_1-3)**2"
echo " --- Secao Aurea"
python3 Metodos/minSecaoAurea.py    "(x[0]-3)**2"   "[0.0,    10.0]"   "0.001"
echo " --- Fibonacci"
python Metodos/minFibonacci.py      "(x[0]-3)**2"   "[0.0]" "[10.0]"   "0.001"

echo ""
echo ""
echo ""
#Questao 2 - Alternativa C
#(x[0]-3)**2,"(x_1-3)^2"				0.5<=x<=3.5 min x = 2.22939
echo "Q2 - C"
echo "Min (sin(0.1+2*x[0]))/(1+x[0])"
echo " --- Secao Aurea"
python3 Metodos/minSecaoAurea.py    "(sin(0.1+2*x[0]))/(1+x[0])"   "[0.5,    3.5]"   "0.001"
echo " --- Fibonacci"
python Metodos/minFibonacci.py      "(sin(0.1+2*x[0]))/(1+x[0])"   "[0.5]" "[3.5]"   "0.001"


echo ""
echo ""
echo ""
echo "Questao 2 - Interpolacao"
echo "Q2 - A -- f(x) = 3 x_1^2-5 x_1"
echo "Interpolando f(x) =  3 x_1^2-5 x_1 -> [(x,f(x)) | 0 <= x <= 3] -> [(0, 0), (1, -2), (2, 2), (3, 12)]"
python Metodos/interpol.py "[(0, 0), (1, -2), (2, 2), (3, 12)]" #[(0, 0), (1, -2), (2, 2), (3, 12)] -> Gera funcao exata
echo " --- Secao Aurea"
python3 Metodos/minSecaoAurea.py "$(python Metodos/interpol.py '[(0, 0), (1, -2), (2, 2), (3, 12)]')"   "[0.0,    3.0]"   "0.001"
echo " --- Fibonacci"
python3 Metodos/minFibonacci.py  "$(python Metodos/interpol.py '[(0, 0), (1, -2), (2, 2), (3, 12)]')"   "[0.0]" "[3.0]"  "0.001"
echo ""
echo ""
echo ""

echo "Q2 - B -- f(x) = (x_1-3)**2"
echo "Interpolando f(x) = (x_1-3)**2 -> [(x,f(x)) | 0 <= x <= 10] ->    [(0, 9), (1, 4), (2, 1), (3, 0), (4, 1), (5, 4), (6, 9), (7, 16), (8, 25), (9, 36)]"
python Metodos/interpol.py "[(0, 9), (1, 4), (2, 1), (3, 0), (4, 1), (5, 4), (6, 9), (7, 16), (8, 25), (9, 36)]"
echo " --- Secao Aurea"
python3 Metodos/minSecaoAurea.py "$(python Metodos/interpol.py '[(0, 9), (1, 4), (2, 1), (3, 0), (4, 1), (5, 4), (6, 9), (7, 16), (8, 25), (9, 36)]')"   "[0.0,    10.0]"   "0.001"
echo " --- Fibonacci"
python3 Metodos/minFibonacci.py  "$(python Metodos/interpol.py '[(0, 9), (1, 4), (2, 1), (3, 0), (4, 1), (5, 4), (6, 9), (7, 16), (8, 25), (9, 36)]')"   "[0.0]" "[10.0]"   "0.001"
echo ""
echo ""
echo ""

echo "Q2 - C -- f(x) = (sin(0.1+2*x[0]))/(1+x[0])"
echo "Interpolando f(x) = (sin(0.1+2*x[0]))/(1+x[0]) -> [(x,f(x)) | 0 <= x <= 3.5] -> [(0, 0.09983341664682815), (1, 0.43160468332443686), (2, -0.2727590370214701), (3, -0.04554062606802397)]"
python Metodos/interpol.py "[(0, 0.09983341664682815), (1, 0.43160468332443686), (2, -0.2727590370214701), (3, -0.04554062606802397)]"
echo " --- Secao Aurea"
python3 Metodos/minSecaoAurea.py "$(python Metodos/interpol.py '[(0, 0.09983341664682815), (1, 0.43160468332443686), (2, -0.2727590370214701), (3, -0.04554062606802397)]')"   "[0.0,    3.5]"   "0.001"
echo " --- Fibonacci"
python3 Metodos/minFibonacci.py  "$(python Metodos/interpol.py '[(0, 0.09983341664682815), (1, 0.43160468332443686), (2, -0.2727590370214701), (3, -0.04554062606802397)]')"   "[0.0]" "[3.5]"   "0.001"

echo ""
echo ""
echo ""
