from numpy import pi
import numpy as np
import matplotlib.pyplot as plt

# Declaração de variáveis

w = (2 * pi) / 365  # Frequência anual de variação
tp = 205  # Dia médio em que ocorre a temperatura de pico


# Definição da equação da temperatura diária média
def equacao(t):
    return Tm + (Tp - Tm) * np.cos(w * (t - tp))


# Declaração de arrays
# Formatação:
# aTm = [Miami, Seattle, Boston] e aTp = [Miami, Seattle, Boston], onde:
# Tm é a temperatura média anual em dada cidade (ºC)
# Tp é a temperatura de pico nessa mesma cidade (ºC)

aTm = np.array([22.1, 10.6, 10.7])
aTp = np.array([28.3, 17.6, 22.9])

print("Escolha uma cidade para calcular a variação de temperatura: \n")
print("0 - Miami")
print("1 - Seattle")
print("2 - Boston\n")
x = int(input("> "))

if x == 0:  # Escolha de Miami
    Tm = aTm[0]
    Tp = aTp[0]
    cidade = "Miami"

elif x == 1:  # Escolha de Seattle
    Tm = aTm[1]
    Tp = aTp[1]
    cidade = "Seattle"

elif x == 2:  # Escolha de Boston
    Tm = aTm[2]
    Tp = aTp[2]
    cidade = "Boston"

else:
    print("Por favor, digite um dos três dígitos (0, 1 ou 2) para a escolha da cidade")

print("Agora, escolha o bimestre em que deseja trabalhar: ")
print("1) Janeiro - Fevereiro")
print("2) Julho - Agosto")
bimestre = int(input("> "))

if bimestre == 1:
    print("Ok! Agora, escolha dois dias do bimestre (entre 0 e 59) em que deseja calcular a diferença de temperatura:")
    t1 = int(input("t1: "))
    t2 = int(input("t2: "))

    if 0 <= t1 and t2 <= 59:
        print("A temperatura média no dia", t1, "é igual a:", equacao(t1))
        print("A temperatura média no dia", t2, "é igual a:", equacao(t2))
        print("Logo, o módulo da variação de temperatura entre os dois dias é igual a:",
              abs(abs(equacao(t2)) - abs(equacao(t1))), "ºC")

    else:
        print("Tente novamente. Os valores devem estar entre 0 e 59 dias")

elif bimestre == 2:
    print(
        "Ok! Agora, escolha dois dias do bimestre (entre 180 e 242) em que deseja calcular a diferença de temperatura:")
    t1 = int(input("t1: "))
    t2 = int(input("t2: "))

    if 180 <= t1 and t2 <= 242:
        print("A temperatura média no dia", t1, "é igual a:", equacao(t1))
        print("A temperatura média no dia", t2, "é igual a:", equacao(t2))
        print("Logo, o módulo da variação de temperatura entre os dois dias é igual a:",
              abs(abs(equacao(t2)) - abs(equacao(t1))), "ºC")

    else:
        print("Tente novamente. Os valores devem estar entre 180 e 242 dias")

else:
    print("Por favor, escolha um dos bimestres ofertados")

# Análise do comportamento gráfico da função temperatura média diária
# Criação de arrays para os intervalos de dias dos bimestres dados

janFev = np.linspace(0, 59, 60)
julAgo = np.linspace(180, 242, 62)

plt.plot(janFev, equacao(janFev), color='cyan', marker='.')
plt.xlabel('Tempo (dias)')
plt.ylabel('Média diária de temperatura (ºC)')
plt.title('Variação da temperatura no bimestre janeiro - fevereiro em ' + cidade)
plt.show()

plt.plot(julAgo, equacao(julAgo), color='magenta', marker='x')
plt.xlabel('Tempo (dias)')
plt.ylabel('Média diária de temperatura (ºC)')
plt.title('Variação da temperatura no bimestre julho - agosto em ' + cidade)
plt.show()
