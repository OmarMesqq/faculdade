print("Olá! Insira seu DRE e suas notas na P1 e na P2 para calcular sua média final")

dre = int(input("DRE: "))
if dre <= 0:
    exit("Por favor, insira um DRE válido")

p1 = float(input("Nota na P1: "))
p2 = float(input("Nota na P2: "))

mf = (p1 + p2) / 2

if mf >= 7.0:
    print("Parabéns! Aproveite as férias da aprovação direta!")

elif 3.0 <= mf < 7.0:
    print("Sem estresse. Você deve fazer a Prova Final para conseguir a aprovação.")

elif mf < 3.0:
    print("Sinto muito. Sua pobre alma está reprovada sem chance de fazer a PF. Até o próximo período!")
