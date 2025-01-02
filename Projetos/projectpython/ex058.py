import random

numero_aleatorio = random.randint(0, 10)
numero_escolhido = int(input("Tente adivinhar o número escolhido pelo computador (entre 0 e 10): "))

while numero_escolhido != numero_aleatorio:
    print("Você perdeu! TENTE NOVAMENTE")
    numero_escolhido = int(input("Tente adivinhar o número escolhido pelo computador (entre 0 e 10): "))

print("Parabéns! Você venceu!")

