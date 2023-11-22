""" 
Escreva uma função recursiva que receba um número inteiro positivo como parâmetro e 
imprima-o verticalmente, ou seja,  um dígito por linha.  
Exemplo:  se o número recebido for 198 a função irá exibir
1
9
8 
""" 

def vertical(n):
    n_str = str(n)
    if len(n_str) == 1:
        digitoVertical = n_str 
        return digitoVertical
    else:
        digitoVertical = n_str[0] + '\n'
    return digitoVertical + vertical(n_str[1:])

print(vertical(198))