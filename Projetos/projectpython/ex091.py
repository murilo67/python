from random import randint
from operator import itemgetter
from time import sleep
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = dict()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-*-' * 30)
for c, i in enumerate(ranking):
    print(f'{c+1}º lugar: {i[0]} com {i[1]}.')
    sleep(1)
