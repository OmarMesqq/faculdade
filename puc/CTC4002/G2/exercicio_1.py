"""
São entradas de uma função:
- cor 
- diametro do aro 
- e uma lista de listas da seguinte forma:
[ ['marca_1', 'cor_1', x], ['marca_2', 'cor_2', y], ...]

onde x e y são tamanhos de aros de bicicletas. 

Escreva uma função que retorne também uma lista de listas no seguinte formato:

[ ['marca_1', a], ['marca_2', b], ...]

onde a e b são a quantidade de bicicletas (sublistas da entrada)
que são da cor desejada e de tamanho do aro maior ou igual ao desejado 

Obs.: A lista de entrada só pode ser percorrida uma vez
"""

def pegaBicicletas(cor: str, diametro: int, lista: []):
    marcas = {}
    achado = False

    for marca, cor_bicicleta, tamanho_aro in lista: 
        if cor_bicicleta == cor and tamanho_aro >= diametro: 
            if marca in marcas: 
                marcas[marca] += 1
            else: 
                marcas[marca] = 1

    return marcas


corMock = 'azul'
aroMock = 25
listaMock = [
    ['MarcaA', 'vermelho', 20],
    ['MarcaB', 'azul', 24],
    ['MarcaC', 'azul', 26],
    ['MarcaD', 'preto', 25],
    ['MarcaE', 'azul', 30],
    ['MarcaF', 'verde', 22],
    ['MarcaG', 'azul', 20]
]

print(pegaBicicletas(corMock, aroMock, listaMock))

