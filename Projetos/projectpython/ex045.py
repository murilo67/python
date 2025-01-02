#Crie um programa que faça o computador jogar Jokenpô com você.
import random

com = random.randint(1, 3)
a = int(input('''[1] Pedra
[2] Papel
[3] Tesoura
Escolha e digite: '''))

if com == a:
    print('EMPATE')
elif com == 1 and a == 2:
    print('''JOGADOR GANHOU''')
elif com == 1 and a == 3:
    print('COMPUTADOR GANHOU')
elif com == 2 and a == 1:
    print('COMPUTADOR GANHOU')
elif com == 2 and a == 3:
    print('JOGADOR GANHOU')
elif com == 3 and a == 1:
    print('JOGADOR GANHOU')
elif com == 3 and a == 2:
    print('COMPUTADOR GANHOU')
