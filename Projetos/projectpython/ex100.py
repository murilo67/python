import random


def sorteia():
    numeros = []
    for c in range(5):
        numeros.append(random.randint(1, 100))
    return numeros


def somaPar(lista):
    somapares = 0
    for numero in lista:
        if numero % 2 == 0:
            somapares += numero
    return somapares


# Teste do programa
numeros_sorteados = sorteia()
print("Números sorteados:", numeros_sorteados)

soma_pares = somaPar(numeros_sorteados)
print("Soma dos números pares:", soma_pares)
