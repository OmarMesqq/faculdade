""" 
Escreva uma função recursiva que receba um número inteiro e retorne um número que contenha os 
mesmos algarismos do  número recebido como parâmetro, mas em ordem inversa.  
Exemplo:
inverte(1234) --> 4321 
"""

import math

# def inverteComString(n):
#     if n < 10: 
#         return str(n) 
#     return str(n % 10) + inverte(n // 10)


def maior_potencia_de_dez(n):
    if n <= 0: raise ValueError("Valor ilegal")
    return math.floor(math.log10(n))


def inverte(n):
    if n == 0: return n
    if n < 0: n*= -1
    if n < 10: return n

    i = maior_potencia_de_dez(n)
    
    num = 0
    while i >= 0:
        num += (10**i) * inverte(n % 10) 
        n = n // 10
        i -= 1

    return num


print(inverte(-53))
