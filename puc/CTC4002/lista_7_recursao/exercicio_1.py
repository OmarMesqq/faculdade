""" 
Escreva uma função recursiva que receba um número inteiro como 
parâmetro e retorne a quantidade de vezes que os  algarismos 3 e 4 aparecem no número. 
Exemplo: se o número for 239424, a função retornará 3. 
"""

def qtdDeAlgarismos(inteiro):
    inteiro = str(inteiro)

    if len(inteiro) == 0:
        return contador

    contador = 1 if inteiro[0] == '3' or inteiro[0] == '4' else 0

    return contador + qtdDeAlgarismos(inteiro[1:])

print(qtdDeAlgarismos(239424)) 
