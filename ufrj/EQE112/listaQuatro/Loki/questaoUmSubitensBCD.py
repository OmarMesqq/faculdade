# Item B: Apresentar frações molares e mássicas dos componentes no feed

NsolFeed = 33.5  # Valores da corrente de entrada
MsolFeed = 182.0

fmh2 = 30.0 / NsolFeed  # Atribuição de valores da
fmco = 2.0 / NsolFeed  # família de variáveis "fm" como frações
fmco2 = 1.5 / NsolFeed  # molares

print(f'A fração molar de H2 no feed é igual a: {fmh2 : 4.2f}')
print(f'A fração molar de CO no feed é igual a: {fmco : 4.2f}')
print(f'A fração molar de CO2 no feed é igual a: {fmco2 : 4.2f}', "\n")

fmh2 = 60.0 / MsolFeed  # Reatribuição de valores para as
fmco = 56.0 / MsolFeed  # variáveis "fm" como frações
fmco2 = 66.0 / MsolFeed  # mássicas

print(f'A fração mássica de H2 no feed é igual a: {fmh2 : 4.2f}')
print(f'A fração mássica de CO no feed é igual a: {fmco : 4.2f}')
print(f'A fração mássica de CO2 no feed é igual a: {fmco2 : 4.2f}', "\n")

# Item C: Apresentar frações molares e mássicas dos componentes na saída

# Após a metanação catalítica, a única quantidade de matéria que
# permanece inalterada é a de gás hidrogênio. Assim:

nh2 = 30.0
nco = 2.0 * 0.01  # Multiplicação dos moles de CO e CO₂
nco2 = 1.5 * 0.005  # pelos graus de remoção fornecidos

NsolSaida = nh2 + nco + nco2  # Nº de moles de mistura na saída

fmh2 = nh2 / NsolSaida
fmco = nco / NsolSaida
fmco2 = nco2 / NsolSaida

print(f'A fração molar de H2 na saída  é igual a: {fmh2 : 4.2f}')
print(f'A fração molar de CO na saída é igual a: {fmco : 4.2f}')
print(f'A fração molar de CO2 na saída é igual a: {fmco2 : 4.2f}', "\n")

# Analogamente à quantidade de mol, a única espécie que
# permanece inalterada é a de gás hidrogênio. Desse modo:

mh2 = 60.0
mco = 0.56  # Valores obtidos pelo produto do nº de moles na mistura,
mco2 = 0.33  # grau de remoção e massa molar

MsolSaida = mh2 + mco + mco2

fmh2 = mh2 / MsolSaida
fmco = mco / MsolSaida
fmco2 = mco2 / MsolSaida

print(f'A fração mássica de H2 na saída  é igual a: {fmh2 : 4.2f}')
print(f'A fração mássica de CO na saída  é igual a: {fmco : 4.2f}')
print(f'A fração mássica de CO2 na saída  é igual a: {fmco2 : 4.2f}', "\n")

# Item D: Razão entre as massas molares da mistura antes e depois do processo

mmh2 = 2.0  # Bloco de massas molares
mmco = 28.0  # de cada componente da mistura
mmco2 = 44.0


# Cálculo da massa molar da mistura utilizando
# valores encontrados com o próprio código
mmMistFeed = ((mmh2 * 0.9) + (mmco * 0.06) + (mmco2 * 0.04))

mmMistSaida = ((mmh2 * 1.0) + (mmco * 0.00) + (mmco2 * 0.00))
# Devido à aproximação do Python, as frações molares encontradas
# após a metanação catalítica tendem a 100% para o gás hidrogênio
# enquanto para CO e CO₂, estas tendem a 0. Assim, entende-se
# que tal processo é muito eficiente

print("A razão entre as massas molares da mistura antes e depois"
      " do processo é igual a", mmMistFeed / mmMistSaida)

