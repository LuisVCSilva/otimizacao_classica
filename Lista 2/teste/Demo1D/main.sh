python3 Metodos/interpol.py "[(1,3),(2,1),(3,2),(5,10)]"

python Metodos/minBuscaAleatoria.py "12*x[0]**2-16*x[0]+8" "[0.0]" "[10.0]" "0.001" "10000"
python3 Metodos/minSecaoAurea.py "12*x[0]**2-16*x[0]+8" "[0.0,10.0]" "0.001"
python Metodos/minFibonacci.py "12*x[0]**2-16*x[0]+8" "[0.0]" "[3.0]" "0.0001"
python Metodos/minPowell.py "12*x[0]**2-16*x[0]+8" "[-0.5]" "[0.5]" "0.001"
python Metodos/minNelderMead.py "12*x[0]**2-16*x[0]+8" "[0.0]"

python Metodos/minMaximaDescida.py "12*x[0]**2-16*x[0]+8" "24*x[0]-16" "[0.0]" "0.001" "0.0001" "1000000"
python Metodos/minGradConjugado.py "12*x[0]**2-16*x[0]+8" "24*x[0]-16" "[0.0]" "0.001" "100000"

python Metodos/minNewton.py "12*x[0]**2-16*x[0]+8" "[24*x-16]" "[[24]]"

python Metodos/minBFGS.py "12*x[0]**2-16*x[0]+8" "24*x[0]-16" "[0.0]" "1000" "0.0001"
