from random import randint
import time
jogos = []
n = int(input('Quantos palpites gerar na MEGA-SENA? '))

for r in range(n):
    numeros = []
    for _ in range(6):
        num = randint(1, 60)
        while num in numeros:
            num = randint(1, 60)
        numeros.append(num)

    jogos.append(numeros)
    print(jogos)
