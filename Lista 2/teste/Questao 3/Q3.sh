echo "Busca Aleatoria"
echo " --- Min x_1^2 - 3 x_1 x_2 + 4 x_2^2 + x_1 - x_2"
python Metodos/minBuscaAleatoria.py "x[0]**2 - 3*x[0]*x[1] + 4*x[1]**2 + x[0] - x[1]" "[0.0]" "[5.0]" "0.01" "1000"

echo " --- Min 6 x_1^2 + 2 x_2^2 - 6 x_1 x_2 - x_1 - 2 x_2"
python Metodos/minBuscaAleatoria.py "6*x[0]**2 + 2*x[1]**2 - 6*x[0]*x[1] - x[0] - 2*x[1]" "[0.0]" "[5.0]" "0.01" "1000"

echo " --- Min x_1 - x_2 + 2 x_1^2 + 2 x_1 x_2 + x_2^2"
python Metodos/minBuscaAleatoria.py "x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1] + x[1]**2" "[0.0]" "[5.0]" "0.01" "1000"


echo ""
echo ""
echo ""


echo "Newton"
echo " --- Min x_1^2 - 3 x_1 x_2 + 4 x_2^2 + x_1 - x_2"
python Metodos/minNewton.py "x[0]**2 - 3*x[0]*x[1] + 4*x[1]**2 + x[0] - x[1]" "array([2*x[0] - 3*x[1] + 1, -3*x[0] + 8*x[1] - 1])" "array([[2, -3],[-3, 8]])" "array([0.0, 0.0])" "0.001" "10000" "0.001"

echo " --- Min 6 x_1^2 + 2 x_2^2 - 6 x_1 x_2 - x_1 - 2 x_2"
python Metodos/minNewton.py "6*x[0]**2 + 2*x[1]**2 - 6*x[0]*x[1] - x[0] - 2*x[1]" "array([12*x[0] - 6*x[1] - 1,-6*x[0] + 4*x[1] - 2])" "array([[12,-6],[-6,4]])" "array([0.0, 0.0])" "0.001" "10000" "0.001"

echo " --- Min x_1 - x_2 + 2 x_1^2 + 2 x_1 x_2 + x_2^2"
python Metodos/minNewton.py "x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1] + x[1]**2" "array([4*x[0] + 2*x[1] + 1 ,2*x[0] + 2*x[1] - 1])" "array([[4,2],[2,2]])" "array([0.0, 0.0])" "0.001" "10000" "0.001"


echo ""
echo ""
echo ""


echo "Gradiente Conjugado"
echo " --- Min x_1^2 - 3 x_1 x_2 + 4 x_2^2 + x_1 - x_2"
python Metodos/minGradConjugado.py "x[0]**2 - 3*x[0]*x[1] + 4*x[1]**2 + x[0] - x[1]" "array([2*x[0] - 3*x[1] + 1, -3*x[0] + 8*x[1] - 1])" "[0.0,0.0]" "0.001" "10000"

echo " --- Min 6 x_1^2 + 2 x_2^2 - 6 x_1 x_2 - x_1 - 2 x_2"
python Metodos/minGradConjugado.py "6*x[0]**2 + 2*x[1]**2 - 6*x[0]*x[1] - x[0] - 2*x[1]" "array([12*x[0] - 6*x[1] - 1,-6*x[0] + 4*x[1] - 2])" "[0.0,0.0]" "0.001" "10000"

echo " --- Min x_1 - x_2 + 2 x_1^2 + 2 x_1 x_2 + x_2^2"
python Metodos/minGradConjugado.py "x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1] + x[1]**2" "array([4*x[0] + 2*x[1] + 1 ,2*x[0] + 2*x[1] - 1])" "[0.0,0.0]" "0.001" "10000"


echo ""
echo ""
echo ""


echo "Maxima Descida"
echo " --- Min x_1^2 - 3 x_1 x_2 + 4 x_2^2 + x_1 - x_2"
python Metodos/minMaximaDescida.py "x[0]**2 - 3*x[0]*x[1] + 4*x[1]**2 + x[0] - x[1]" "array([2*x[0] - 3*x[1] + 1, -3*x[0] + 8*x[1] - 1])" "[0.0,0.0]" "0.001" "0.0001" "10000"

echo " --- Min 6 x_1^2 + 2 x_2^2 - 6 x_1 x_2 - x_1 - 2 x_2"
python Metodos/minMaximaDescida.py "6*x[0]**2 + 2*x[1]**2 - 6*x[0]*x[1] - x[0] - 2*x[1]" "array([12*x[0] - 6*x[1] - 1,-6*x[0] + 4*x[1] - 2])" "[0.0,0.0]" "0.001" "0.0001" "10000"

echo " --- Min x_1 - x_2 + 2 x_1^2 + 2 x_1 x_2 + x_2^2"
python Metodos/minMaximaDescida.py "x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1] + x[1]**2" "array([4*x[0] + 2*x[1] + 1 ,2*x[0] + 2*x[1] - 1])" "[0.0,0.0]" "0.001" "0.0001" "10000"


echo ""
echo ""
echo ""


echo "Nelder-Mead"
echo " --- Min x_1^2 - 3 x_1 x_2 + 4 x_2^2 + x_1 - x_2"
python Metodos/minNelderMead.py "x[0]**2 - 3*x[0]*x[1] + 4*x[1]**2 + x[0] - x[1]" "[0.0,0.0]"

echo " --- Min 6 x_1^2 + 2 x_2^2 - 6 x_1 x_2 - x_1 - 2 x_2"
python Metodos/minNelderMead.py "6*x[0]**2 + 2*x[1]**2 - 6*x[0]*x[1] - x[0] - 2*x[1]" "[0.0,0.0]"

echo " --- Min x_1 - x_2 + 2 x_1^2 + 2 x_1 x_2 + x_2^2"
python Metodos/minNelderMead.py "x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1] + x[1]**2" "[0.0,0.0]"


echo ""
echo ""
echo ""


echo "BFGS"
echo " --- Min x_1^2 - 3 x_1 x_2 + 4 x_2^2 + x_1 - x_2"
python Metodos/minBFGS.py "x[0]**2 - 3*x[0]*x[1] + 4*x[1]**2 + x[0] - x[1]" "array([2*x[0] - 3*x[1] + 1,-3*x[0] + 8*x[1] - 1])" "[0.0, 0.0]" "1000" "0.001"

echo " --- Min 6 x_1^2 + 2 x_2^2 - 6 x_1 x_2 - x_1 - 2 x_2"
python Metodos/minBFGS.py "6*x[0]**2 + 2*x[1]**2 - 6*x[0]*x[1] - x[0] - 2*x[1]" "array([12*x[0] - 6*x[1] - 1, -6*x[0] + 4*x[1] - 2])" "[0.0, 0.0]" "1000" "0.001"

echo " --- Min x_1 - x_2 + 2 x_1^2 + 2 x_1 x_2 + x_2^2"
python Metodos/minBFGS.py "x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1] + x[1]**2" "array([4*x[0] + 2*x[1] + 1 ,2*x[0] + 2*x[1] - 1])" "[0.0, 0.0]" "1000" "0.001"
