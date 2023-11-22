""" 
Escreva uma função recursiva que receba um número inteiro e retorne um número que 
contenha os mesmos algarismos do  número recebido como parâmetro, mas em ordem inversa. 
Se o número recebido for 198 a função irá exibir
8
9
1
""" 
def verticalInvertido(n):
    n_str = str(n)
    ultimoDigito = len(n_str) - 1
    if len(n_str) == 1:
        digitoVertical = n_str 
        return digitoVertical
    else:
        digitoVertical = n_str[ultimoDigito] + '\n'
    return digitoVertical + verticalInvertido(n_str[:ultimoDigito])


print(verticalInvertido(198))