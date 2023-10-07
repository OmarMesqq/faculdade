# 4.ª Lista de Programação em Python — Professor Luiz Fernando
#
# Omar Mesquita Amaral Figueira — EQE112
#
# Escola de Química — UFRJ


# Definição de fração mássica
# Ya= Ma / Msolução

# Definição de fração molar
# Xa = Na / Nsolução

# Importação de módulos e bibliotecas
import numpy as np

# Definição de variáveis

Nsol = 33.5  # N.º total de moles da solução (fornecido no enunciado)

Msol = 182.0  # Massa total da solução

# AVISO 1: As unidades adotadas na resolução dessa questão são g/gmol

# AVISO 2: Por questões de aproximação feita pelo Python 3
# (na formatação de saída: f'{:4.2f}),a última função declarada
# pode apresentar diferenças no resultado da massa molar de até dois décimos

# Item A, Subitem 1: função para cálculo de fração molar dos componentes


def calcFracaoMolar():
    h2x = float(input("Insira o número de moles de gás hidrogênio: "))
    cox = float(input("Insira o número de moles de monóxido de carbono: "))
    co2x = float(input("Insira o número de moles de gás carbônico: "))

    x = np.array([h2x, cox, co2x])  # Array com quantidade de matéria fornecidos pelo usuário

    print(f'Fração molar de H2: {(x[0] / Nsol) : 4.2f}')
    print(f'Fração molar de CO: {(x[1] / Nsol) : 4.2f}')
    print(f'Fração molar de CO2: {(x[2] / Nsol) : 4.2f}')


calcFracaoMolar()


# Item A, Subitem 2: função para cálculo de fração mássica dos componentes

def calcFracaoMassica():
    h2y = float(input("Insira a massa de gás hidrogênio: "))
    coy = float(input("Insira a massa de monóxido de carbono: "))
    co2y = float(input("Insira a massa de gás carbônico: "))

    y = np.array([h2y, coy, co2y])  # Array com a massa dos componentes

    print(f'A fração mássica de H2 é igual a: {(y[0] / Msol) : 4.2f}')
    print(f'A fração mássica de CO é igual a: {(y[1] / Msol) : 4.2f}')
    print(f'A fração mássica de CO2 é igual a: {(y[2] / Msol) : 4.2f}')


calcFracaoMassica()


# Item A, Subitem 3: função para cálculo da massa molar da mistura

def massaMolarMistura():
    fMH2 = float(input("Insira a fração molar de H2: "))
    fMCO = float(input("Insira a fração molar de CO: "))  # Bloco de variáveis para
    fMCO2 = float(input("Insira a fração molar de CO2: "))  # frações molares dos componentes

    mmH2 = float(input("Insira a massa molar do H2: "))  # Bloco de variáveis para
    mmCO = float(input("Insira a massa molar do CO: "))  # massa molar individual de cada componente
    mmCO2 = float(input("Insira a massa molar do CO2: "))

    fm = np.array([fMH2, fMCO, fMCO2])  # Arrays de entrada os quais armazenam as variáveis
    mm = np.array([mmH2, mmCO, mmCO2])  # inseridas em cada bloco acima pelo usuário

    mmMist = (fm[0] * mm[0]) + (fm[1] * mm[1]) + (fm[2] * mm[2])  # Lógica do cálculo da massa molar da mistura
    print("A massa molar da mistura é igual a", mmMist, "g/gmol")


massaMolarMistura()
