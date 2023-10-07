# Inicialização de listas
lista_DRE = []
lista_mediaFinal = []
lista_sitFinal = []

while True:

    DRE = int(input("Insira seu DRE: "))

    if DRE < 0:
        break
    else:
        pass
    p1 = float(input("Insira sua nota na P1: "))
    p2 = float(input("Insira sua nota na P2: "))

    mf = (p1 + p2) / 2.0

    lista_DRE.append(DRE)
    lista_mediaFinal.append(mf)

    if mf >= 7.0:
        sitFinal = "Aprovação"
    elif 3.0 <= mf < 7.0:
        sitFinal = "PF"
    elif mf < 3.0:
        sitFinal = "Reprovação"

    lista_sitFinal.append(sitFinal)

print()

for x in range(len(lista_sitFinal)):
    print("Estudante:", lista_DRE[x])
    print("Média Final:", lista_mediaFinal[x])
    print("Situação Final:", lista_sitFinal[x])
    print("----------")
