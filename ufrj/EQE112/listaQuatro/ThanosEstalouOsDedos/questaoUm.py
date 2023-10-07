import numpy as np


# Para considerar o efeito da mudança
# de temperatura nas propriedades físicas,
# resgatei a tabela e a lógica de interpolação
# da questão 1 do último nível
# da lista 3. Ela fornece valores para propriedades físicas
# do ar a pressão ambiente

def interpol(val, x):
    # Massa Específica em kg/m³
    ro = np.array([1.3947, 1.1614, 0.9950, 0.8711])

    # Viscosidade em N.s/m²
    mi = np.array([159.6 * 10e-7, 184.6 * 10e-7, 208.2 * 10e-7, 230.1 * 10e-7])

    # Lógica para escolher o intervalo de temperatura e as propriedades para a interpolação
    if 1 < val < 1.2:
        sup = 300
        inf = 250

        supro = ro[1]
        infro = ro[0]

        supmi = mi[1]
        infmi = mi[0]

    elif 1.2 < val < 1.4:
        sup = 350
        inf = 300

        supro = ro[2]
        infro = ro[1]

        supmi = mi[2]
        infmi = mi[1]

    elif 1.4 < val < 1.6:
        sup = 400
        inf = 350

        supro = ro[3]
        infro = ro[2]

        supmi = mi[3]
        infmi = mi[2]

        interpolro = supro - ((sup - Ti) * (supro - infro) / (sup - inf))
        interpolmi = supmi - ((sup - Ti) * (supmi - infmi) / (sup - inf))

        if x == 1:
            return interpolro
        if x == 2:
            return interpolmi


Ti = float(input("Entre com uma temperatura entre 250K e 400K >> "))
val = Ti / 250  # Variável utilizada para determinar o intervalo de Tsup e Tinf

if val < 1 or val > 1.6:  # Caso valor inserido seja menor que 250K ou maior que 400K, programa encerra
    print('Não é possível calcular para a temperatura dada.')

else:
    pass


D = 0.01  # diâmetro do tubo circular em m
L = 1.3  # comprimento do tubo circular em m
Dab = 26.0 * 10e-6  # coeficiente de difusão H₂O, ar em m²/s
As = np.pi * D * L  # área de troca de massa em m²
roAs = 0.0226  # massa específica da água em condição de saturação em kg/m³
roAin = 1000.0  # massa específica da água em condição de entrada em kg/m³

mdot = float(input("Insira um valor para taxa mássica: "))
Red = ((4 * mdot) / (np.pi * D * interpol(val,2)))  # Adimensional de Reynolds
Sc = (interpol(val,2) / (interpol(val,1) * Dab))  # Adimensional de Schmidt

# Bloco de "limites" para valores
# para taxa mássica. Obtidos pelo isolamento
# da equação do adimensional de Reynolds
# Para os valores dados, 0.6 <= Sc =< 2.5,
# então a seguinte relação vale:
mdotMin = 1.441991027997715e-05  # Menor valor (para 10 < Red)
mdotMaxLam = 0.00288398205599543  # Valor de virada de regime laminar para turbulento (Red = 2000)
mdotMax = 0.05046968597992002  # Valor máximo, isto é, Red < 35000

# Cálculo do coeficiente de convecção mássica (hm) em m/s
if mdot < mdotMin:
    quit("Insira um valor maior para taxa mássica")

elif mdotMin <= mdot < mdotMaxLam:  # Laminar
    hm = (1.86 * Dab * pow((D / L) * Red * Sc, 1 / 3)) / D

elif mdotMaxLam <= mdot < mdotMax:  # Turbulento
    hm = (0.023 * Dab * pow(Red, 0.83) * pow(Sc, 0.44)) / D

else:
    quit("Insira um valor menor para a taxa mássica")

roAout = - ((roAs - roAin) * np.exp((-As * hm * interpol(val, 1)) / mdot)) + roAs

print("A concentração mássica de água na saída é igual a", roAout, "kg/m³")
