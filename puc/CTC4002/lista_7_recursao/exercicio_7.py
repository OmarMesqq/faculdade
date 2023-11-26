"""
Escreva uma função recursiva que receba um número inteiro n, na base 10, 
uma base B e retorne o número n representado  na base B.  
Dica: O número decimal deve ser dividido sucessivas vezes pela base. 
O resto de cada divisão ocupará, sucessivamente, as  posições de ordem 0, 1, 2 e assim por diante, 
até que o resto da última divisão (que resulta em quociente 0) ocupe a posição  de mais alta ordem.
Exemplo:  
19 (dec) == 10011 (bin)  
278 (dec) == 116 (hex)
"""


def toBaseB(n, b):
    """
    Complexidade espacial e temporal: O(logb n)
    """
    if n // b == 0: return f'{n % b}'
    return toBaseB(n // b, b) + f'{n % b}'
    

print(oct(24149721), "?=", toBaseB(24149721,8))
print(bin(19), "?=", toBaseB(19,2))
print(hex(2443), "?=", toBaseB(2443,16))
