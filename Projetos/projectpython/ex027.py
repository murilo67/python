#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

# Gerar um número aleatório entre 0 e 5
numero_aleatorio = random.randint(0, 5)

# Solicitar ao usuário para adivinhar o número
numero_escolhido = int(input("Tente adivinhar o número escolhido pelo computador (entre 0 e 5): "))

# Verificar se o número escolhido pelo usuário é igual ao número gerado aleatoriamente
if numero_escolhido == numero_aleatorio:
    print("Parabéns! Você venceu!")
else:
    print("Você perdeu! O número escolhido pelo computador foi", numero_aleatorio)
