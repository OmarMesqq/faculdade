import numpy as np
import matplotlib.pyplot as plt
from scipy import odr
import scipy.linalg as linalg

# Intervalos fornecidos
tempo = np.array([0.0, 9.0, 16.0, 23.0, 30.0, 34.0, 36.0, 40.0])
conc_celulas = np.array([1.25, 2.45, 5.1, 10.5, 22.0, 33.0, 37.5, 41.0])
conc_glicose = np.array([100.0, 97.0, 90.4, 76.9, 48.1, 20.6, 9.38, 0.63])

# Análise gráfica dos dados de concentração ao longo do tempo
plt.plot(tempo, conc_celulas, '-o', label="Conc. células")
plt.plot(tempo, conc_glicose, '-o', label="Conc. glicose")
plt.xlabel("Tempo (h)")
plt.ylabel("Concentração (g/L)")
plt.legend()
plt.title("Comportamento original dos dados")
plt.show()

# É possível perceber que enquanto a concentração de células aumenta ao longo tempo
# diminui-se a concentração de glicose, que é consumida pelos fungos
# Diante desse contexto, buscamos uma função que cresce ou decresce continuamente
# Em uma exploração inicial de possibilidades, fazer uma regressão linear parece
# inadequada, tendo em vista a pobreza na representação dos dados

# Tempo contínuo para fazer as aproximações numéricas
# baseada no tempo discreto
tempo_cont = np.linspace(0.0, 40.0)

# Aproximação para o crescimento de células 
# polinômios de 1ª (linear), 2ª (quadrático) e 4ª ordem 

# Aprox linear p/ crescimento de células  
data_linear = odr.Data(tempo,conc_celulas)
odr_obj_linear = odr.ODR(data_linear, odr.polynomial(1))
output_linear = odr_obj_linear.run()
poly_linear = np.poly1d(output_linear.beta[::-1])
poly_y_linear = poly_linear(tempo_cont)

# Aprox linear p/ consumo de substrato  
data_linear1 = odr.Data(tempo,conc_glicose)
odr_obj_linear1 = odr.ODR(data_linear1, odr.polynomial(1))
output_linear1 = odr_obj_linear1.run()
poly_linear1 = np.poly1d(output_linear1.beta[::-1])
poly_y_linear1 = poly_linear1(tempo_cont)

# Plot para aprox. linear
plt.figure(figsize=(10,5))

plt.subplot(121)
plt.plot(tempo, conc_celulas, 'o--', label='Conc. células')
plt.plot(tempo_cont, poly_y_linear, label="Aprox. crescimento de células")
plt.legend()
plt.subplot(122)
plt.plot(tempo, conc_glicose, 'o--', label="Conc. glicose")
plt.plot(tempo_cont, poly_y_linear1, label="Aprox. consumo de substrato")
plt.legend()
plt.suptitle("Aproximações lineares")
plt.show()

# Aprox quadrática p/ crescimento de células 

data_quad = odr.Data(tempo,conc_celulas)
odr_obj_quad = odr.ODR(data_quad, odr.polynomial(2))
output_quad = odr_obj_quad.run()
poly_quad = np.poly1d(output_quad.beta[::-1])
poly_y_quad = poly_quad(tempo_cont)

# Aprox quadrática p/ consumo de substrato

data_quad1 = odr.Data(tempo,conc_glicose)
odr_obj_quad1 = odr.ODR(data_quad1, odr.polynomial(2))
output_quad1 = odr_obj_quad1.run()
poly_quad1 = np.poly1d(output_quad1.beta[::-1])
poly_y_quad1 = poly_quad1(tempo_cont)

# Plot para aprox. quadrática
plt.figure(figsize=(10,5))

plt.subplot(121)
plt.plot(tempo, conc_celulas, 'o--', label='Conc. células')
plt.plot(tempo_cont, poly_y_quad, label="Aprox. crescimento de células")
plt.legend()
plt.subplot(122)
plt.plot(tempo, conc_glicose, 'o--', label="Conc. glicose")
plt.plot(tempo_cont, poly_y_quad1, label="Aprox. consumo de substrato")
plt.legend()
plt.suptitle("Aproximações quadráticas")
plt.show()


# Aprox de 4ª ordem p/ crescimento de células 
data = odr.Data(tempo,conc_celulas)
odr_obj = odr.ODR(data, odr.polynomial(4))
output = odr_obj.run()
poly = np.poly1d(output.beta[::-1])
poly_y = poly(tempo_cont)

# Aproximação polinomial de quarta ordem p/ consumo de substrato 
data1 = odr.Data(tempo,conc_glicose)
odr_obj1 = odr.ODR(data1,odr.polynomial(4))
output1 = odr_obj1.run()
poly1 = np.poly1d(output1.beta[::-1])
poly_y1 = poly1(tempo_cont)


# Plot para aprox. polinomial de quarta ordem
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.plot(tempo_cont, poly_y, label="Aproximação polinomial")
plt.plot(tempo, conc_celulas, 'o--', label='Conc. células')
plt.xlabel("Tempo (h)")
plt.ylabel("[células] (g/L)")
plt.legend()

plt.subplot(122)
plt.plot(tempo_cont, poly_y1, label="Aproximação polinomial")
plt.plot(tempo, conc_glicose, 'o--', label="Conc. glicose")
plt.xlabel("Tempo (h)")
plt.ylabel("[subtrato] (g/L)")
plt.legend()

# Mostrar a imagem
plt.suptitle("Aproximações com polinômios de quarto grau")
plt.show()

# Resoluções utilizando sistemas lineares 

# Concentração de células
# Ax^5 + Bx^4 + Cx^3 + Dx^2 + Ex + F
# O modelo acima foi utilizado para imaginar um polinômio que representaria os pontos discretos
# Seguindo com polinômios de 1ª, 2ª e 4ª ordem, muitos pontos eram descartados na análise
# Diante de 6 icógnitas, seriam necessários 6 pontos e apenas 2 são descartados
# Vale ainda ressaltar que aumentando mais a quantidade de pontos utilizados 
# o gráfico não é condizente com o contexto. Ele apresenta subidas e descidas para englobar mais pontos
# mas elas não fazem sentido pensando em crescimento de células e de redução de substrato.

A = np.array([
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
    [tempo[1]**5, tempo[1]**4, tempo[1]**3, tempo[1]**2, tempo[1], 1.0],
    [tempo[2]**5, tempo[2]**4, tempo[2]**3, tempo[2]**2, tempo[2], 1.0],
    [tempo[3]**5, tempo[3]**4, tempo[3]**3, tempo[3]**2, tempo[3], 1.0],
    [tempo[6]**5, tempo[6]**4, tempo[6]**3, tempo[6]**2, tempo[6], 1.0],
    [tempo[7]**5, tempo[7]**4, tempo[7]**3, tempo[7]**2, tempo[7], 1.0]
])
# A escolha de não utilizar os dados dos tempos 30h e 34h se deu
# pois esses pontos fazem parte de um trecho maior que apresenta um comportamento mais linear
# Além disso, de 34h para 36h há uma diferença de tempo muito pequena 

B = np.array([1.25, 2.45, 5.1, 10.5, 37.5, 41.0])

res = linalg.solve(A, B)

B2 = np.array([100.0, 97.0, 90.4, 76.9, 9.38, 0.63])

res2 = linalg.solve(A, B2)

# Já havia feito o modelo do polinômio usando x = np.linspace(0.0, 40.0), mas tem o temp_cont
# Então dá para reaproveitar
x = tempo_cont

plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.plot(tempo, conc_celulas, '-o', label="Conc. células")
plt.plot(x, res[0]*(x**5) + res[1]*(x**4) + res[2]*(x**3) + res[3]*(x**2) + res[4]*x + res[5])
plt.xlabel("Tempo (h)")
plt.ylabel("Concentração (g/L)")
plt.legend()

plt.subplot(122)
plt.plot(tempo, conc_glicose, '-o', label="Conc. glicose")
plt.plot(x, res2[0]*(x**5) + res2[1]*(x**4) + res2[2]*(x**3) + res2[3]*(x**2) + res2[4]*x + res2[5])
plt.xlabel("Tempo (h)")
plt.ylabel("Concentração (g/L)")
plt.legend()
plt.suptitle("Aproximação c/ polinômio de 5ª ordem")
plt.show()
