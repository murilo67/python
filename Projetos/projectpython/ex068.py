import random
while True:
    j = int(input('Digite um valor: '))
    c = random.randint(0, 11)
    t = j + c
    ti = ' '
    while ti not in 'PpIi':
        ti = str(input('Par ou Ímpar? '))

    print(f'Você jogou {j} e o computador {c}. Total de {t}. ', end='')
    print('Deu PAR' if t % 2 == 0 else 'Deu IMPAR')
    if ti == 'Pp':
        if t % 2 == 0:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif ti == 'I':
        if t % 2 == 1:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print('Game Over! Você venceu {} vezes.'.format(v))
