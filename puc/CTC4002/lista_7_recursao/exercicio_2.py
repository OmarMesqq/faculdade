"""
Escreva uma função recursiva que receba um número e retorne-o convertido para
o formato string. (o mesmo que é feito  pela função str()) 
"""

def toStr(n):
    """
    Converte um número inteiro em sua representação de string usando recursão.

    A função usa as operações de divisão inteira (//) e módulo (%) para decompor um 
    inteiro em seus dígitos individuais. A divisão inteira por 10 (n // 10) remove 
    o último dígito do número, enquanto o módulo por 10 (n % 10) extrai o último dígito.
    Esta técnica é aplicável em qualquer base numérica; basta trocar os '10' pela 
    base 'b' desejada.

    Para cada dígito extraído, a função consulta um mapeamento que associa dígitos a 
    suas representações de string. Depois, concatena essas representações de string 
    para formar a representação completa do número original.
    """
    mapping = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
        5: '5', 6: '6', 7: '7', 8: '8', 9: '9'
    }

    if (n < 10): return mapping[n]
    return toStr(n // 10) + mapping[n % 10]


print(toStr(137))