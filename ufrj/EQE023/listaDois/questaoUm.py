import numpy as np 
import scipy.linalg as linalg
import pandas as pd
import dataframe_image as dfi

# Reação: C3H8 -> C3H6 + H2
# Realizando a análise da fronteira que engloba todo o sistema
# é possível observar que, diante da estequiometria, teremos F1=F4=F5=50 kmol/h, relacionando taxa molar.

# Analisando a fronteira do reciclo: F1 + F6 = F2
# Analisando a fronteira do reator: F3 = 1,4F2 (40% de conversão)
# Analisando a fronteira do sistema de separação: F3 = F4 + F5 + F6

# O sistema linear abaixo diz respeito às seguintes equações:
# F2 - F6 = 50
# F3 - 1,4F2 = 0 
# F3 - F6 = 100

A = np.array([
    [1, 0, -1], 
    [-1.4, 1, 0], 
    [0, 1, -1]
])

B = np.array([50, 0, 100])

# Obtendo as correntes,
# res1 = [F2, F3, F6]

res1 = linalg.solve(A, B)

# temos:

F1 = 50.0
F2 = res1[0]
F3 = res1[1]
F4 = 50.0
F5 = 50.0
F6 = res1[2]

# Obtém-se as frações molares em cada corrente
# por substituições nas equações já encontradas:


# Analisando a fronteira de reciclo:
# F2*XF2_C3H8 = F1 + 0.8*F6 
# F2*XF2_C3H6 = 0.2*F6

# Analisando a fronteira do sistema de separação: 
# F3*XF3_H2 = F4
# F3*XF3_C3H8 = 0.8*F6
# F3*XF3_C3H6 = 0.2*F6 + F5

# Multiplicando por 100 para obter a porcentagem em cada corrente
XF2_C3H8 = (F1 + 0.8*F6)/F2 * 100
XF2_C3H6 = (0.2*F6)/F2 * 100
XF3_H2 = (F4/F3) * 100
XF3_C3H8 = (0.8*F6)/F3 * 100
XF3_C3H6 = (0.2*F6 + F5)/F3 * 100


# Tabela com todas as variáveis do processo
corrente1 = pd.Series({'Corrente': 'F1', 'C3H8 (%)': '100.0', 'C3H6 (%)': '-', 'H2 (%)': '-', 'Taxa molar total (kmol/h)' : F1 })
corrente2 = pd.Series({'Corrente': 'F2', 'C3H8 (%)': XF2_C3H8, 'C3H6 (%)': XF2_C3H6, 'H2 (%)': '-', 'Taxa molar total (kmol/h)' : F2 })
corrente3 = pd.Series({'Corrente': 'F3', 'C3H8 (%)': XF3_C3H8, 'C3H6 (%)': XF3_C3H6, 'H2 (%)': XF3_H2, 'Taxa molar total (kmol/h)' : F3 })
corrente4 = pd.Series({'Corrente': 'F4', 'C3H8 (%)': '-', 'C3H6 (%)': '-', 'H2 (%)': '100.0' , 'Taxa molar total (kmol/h)' : F4 })
corrente5 = pd.Series({'Corrente': 'F5', 'C3H8 (%)': '-', 'C3H6 (%)': '100.0', 'H2 (%)': '-', 'Taxa molar total (kmol/h)' : F5 })
corrente6 = pd.Series({'Corrente': 'F6', 'C3H8 (%)': '80.0', 'C3H6 (%)': '20.0', 'H2 (%)': '-', 'Taxa molar total (kmol/h)' : F6 })

df = pd.DataFrame([corrente1, corrente2, corrente3, corrente4, corrente5, corrente6])

# Formatação de duas casas decimais para "floats"
pd.options.display.float_format = '{:,.2f}'.format

# Salvar imagem (caso Google Chrome esteja instalado)
#dfi.export(df, 'tabela_correntes.png') 

# Caso contrário, printar a tabela no output do código 
print(df)
