def calculaSoma(listaInicial):
    soma = 0
    if type(listaInicial) == int:
        return listaInicial
    for elemento in listaInicial:
        soma += calculaSoma(elemento)
    return soma

        
argumento = [[[1,2,3],4,5,6],7,8,9]
print(calculaSoma(argumento))
