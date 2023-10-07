print("Você deseja fazer uso de um ciclone ou um hidrociclone?\n")
print("1 - Ciclone (apropriado para separar misturas gás-sólido)")
print("2 - Hidrociclone (apropriado para separar misturas líquido-sólido)\n")
escolha = input(">> ")

if escolha == "1":
    print("Ok! Escolha o diâmetro do ciclone:")
    Dc = float(input(">> "))

    print("Valores das proporções dimensionais do equipamento para o diâmetro dado:")
    print("Bc = ", Dc / 4.0)
    print("De = ", Dc / 2.0)
    print("Hc = ", Dc / 2.0)
    print("Lc = ", 2.0 * Dc)
    print("Sc = ", Dc / 8.0)
    print("Zc = ", 2.0 * Dc)
    print("Jc = ", Dc / 4)


elif escolha == "2":
    print("Certo! Determine o diâmetro do hidrociclone:")
    D = float(input(">> "))

    print("Valores das proporções dimensionais do equipamento para o diâmetro dado:")
    print("L = ", 5.0 * D)
    print("b = ", 0.28 * D)
    print("e = ", 0.34 * D)
    print("I = ", 0.40 * D)

else:
    print("Por favor, escolha entre uma das duas opções de equipamento")
