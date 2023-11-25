""" 
Escreva uma função recursiva que receba dois números inteiros, com mesma quantidade de algarismos, 
e retorne True, se  todo algarismo que ocupe determinada ordem no 1º número for menor do que o 
algarismo que ocupe a ordem  correspondente no 2º número, ou False, caso contrário.  
Exemplo:
algMenores( 1234 , 2456 ) --> True  
algMenores( 1234 , 2436 ) --> False 
""" 

def algMenores(m, n): 
    if len(str(m)) != len(str(n)): 
        raise IndexError("Números não tem a mesma quantidade de algarismos!")
    
    if m < 10 and n < 10: 
        if m < n: return True
        return False 
    

    return algMenores(m // 10, n // 10) and algMenores(m % 10, n % 10)


print(algMenores(1234 , 2456))