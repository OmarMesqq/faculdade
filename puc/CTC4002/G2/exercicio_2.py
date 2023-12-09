digitos = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

def totalGasto():
    dic = {}
    
    with open("gastos.txt") as gastos:
       for linha in gastos:
           if linha.startswith(digitos) == False:
            categoria = linha.strip("\n").split(",")[0]
            dic[categoria] = 0
           else:
            valorInteiro = linha.strip("\n").split(",")[2]
            valorDecimal = linha.strip("\n").split(",")[3]
            valor = valorInteiro + '.' + valorDecimal

            dic[categoria] += float(valor)
    
    return dic
            

gastosMensais = totalGasto()

#  Para acessar as chaves do dicionario, use: 
#  for chave in dicionario
# Já para os valores: 
# for valor in dicionario.values()
# E para os pares:
for categoria, valor in gastosMensais.items(): 
    print(f"Gastos na categoria {categoria}:", valor, "reais")

