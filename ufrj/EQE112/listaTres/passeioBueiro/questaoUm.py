import numpy as np

while True:
    # Massa Específica em kg/m³
    ro = np.array([1.3947, 1.1614, 0.9950, 0.8711])

    # Capacidade Calorífica em J/kg.K
    cp = np.array([1006.0, 1007.0, 1009.0, 1014.0])

    # Viscosidade em N.s/m²
    mi = np.array([159.6 * 10e-7, 184.6 * 10e-7, 208.2 * 10e-7, 230.1 * 10e-7])

    # Condutividade Térmica em W/m.K
    k = np.array([22.3 * 10e-3, 26.3 * 10e-3, 30.0 * 10e-3, 33.8 * 10e-3])

    Ti = float(input("Entre com uma temperatura entre 250K e 400K >> "))
    val = Ti / 250  # Variável utilizada para determinar o intervalo de Tsup e Tinf

    if val < 1 or val > 1.6:  # Caso valor inserido seja menor que 250K ou maior que 400K, programa encerra
        print('Não é possível calcular para a temperatura dada.')
        break
    else:
        pass

# Lógica para escolher o intervalo de temperatura e as propriedades para a interpolação
    if 1 < val < 1.2:
        sup = 300
        inf = 250

        supro = ro[1]
        infro = ro[0]

        supcp = cp[1]
        infcp = cp[0]

        supmi = mi[1]
        infmi = mi[0]

        supk = k[1]
        infk = k[0]

    elif 1.2 < val < 1.4:
        sup = 350
        inf = 300

        supro = ro[2]
        infro = ro[1]

        supcp = cp[2]
        infcp = cp[1]

        supmi = mi[2]
        infmi = mi[1]

        supk = k[2]
        infk = k[1]

    elif 1.4 < val < 1.6:
        sup = 400
        inf = 350

        supro = ro[3]
        infro = ro[2]

        supcp = cp[3]
        infcp = cp[2]

        supmi = mi[3]
        infmi = mi[2]

        supk = k[3]
        infk = k[2]

# "Fórmulas" para retornar o valor interpolado. Surgiram do isolamento de φi na equação dada
    interpolro = supro - ((sup - Ti) * (supro - infro) / (sup - inf))
    interpolcp = supcp - ((sup - Ti) * (supcp - infcp) / (sup - inf))
    interpolmi = supmi - ((sup - Ti) * (supmi - infmi) / (sup - inf))
    interpolk = supk - ((sup - Ti) * (supk - infk) / (sup - inf))

# Retorna a temperatura intermediária e os valores interpolados nesta.
# Depois, encerra o ciclo while True que engloba a lógica inteira da questão
    print(f'T = {Ti:3.2f}, ρ = {interpolro:1.4f}, C = {interpolcp:4.1f}, µ = {interpolmi:1.7f}, k = {interpolk:1.5f}')
    break
