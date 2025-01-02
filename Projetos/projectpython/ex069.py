t = tm = tm20 = 0
while True:
    print('-*-' * 10)
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-*-' * 10)
    if i >= 18:
        t += 1
    if s == 'M':
        tm += 1
    if s == 'F' and i < 20:
        tm20 += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print('O total de pessoas com mais de 18 anos é de {} pessoas.'.format(t))
print('O total de pessoas que são homens é igual a {}.'.format(tm))
print('Já o total de mulheres que tem menos de 20 anos é igual a {}'.format(tm20))
