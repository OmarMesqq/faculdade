"""
Escreva uma função recursiva que receba um número inteiro (n) e um algarismo (a) 
e "elimine" o algarismo a do número n.
Exemplos 
•  Número 12342 e algarismo 2 --> a função retornará 134  
•  Número 12342 e algarismo 5 --> a função retornará 12342  
•  Número 2 e algarismo 2 --> a função retornará 0   
"""

def eliminacao(n, a):
    n_str = str(n)
    
    if len(n_str) == 1:
        return 0 if n_str == f'{a}' else n_str
        
        
    if n_str[0] == f'{a}':
        final =  eliminacao(n_str[1:], a)
        return final[:-1] if final[-1] == '0' else final

    else: 
        final = n_str[0] + f'{eliminacao(n_str[1:], a)}'
        return final[:-1] if final[-1] == '0' else final
        
        
   
        
    

print(eliminacao(12342, 2)) # deve imprimir 134
print(eliminacao(12342, 5)) # deve imprimir 12342
print(eliminacao(2, 2)) # deve imprimir 0 
