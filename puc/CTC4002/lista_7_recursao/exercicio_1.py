""" 
Escreva uma função recursiva que receba um número inteiro como 
parâmetro e retorne a quantidade de vezes que os  algarismos 3 e 4 aparecem no número. 
Exemplo: se o número for 239424, a função retornará 3. 
"""

def qtdDeAlgarismos_iterativo(inteiro):
    inteiro = str(inteiro)
    qtd = 0

    for i in inteiro: 
        if (i == '3' or i == '4'): 
            qtd += 1

    return qtd


def qtdDeAlgarismos(inteiro):
    inteiro_str = str(inteiro)

    if len(inteiro_str) == 1: 
        if inteiro_str in ['3', '4']:
            return 1 
        else: 
            return 0 
    
    first_count = 1 if inteiro_str[0] in ['3', '4'] else 0
    return first_count + qtdDeAlgarismos(inteiro_str[1:])





print(qtdDeAlgarismos(239424)) 
