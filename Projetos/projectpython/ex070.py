tm = t = m = q = 0
b = ''
while True:
    print('-*-' * 20)
    n = str(input('Nome do produto: '))
    r = float(input('Preço: R$'))
    t += r
    if r > 1000:
        tm += 1
    q += 1
    if q == 1 or r < m:
        m = r
        b = n
    print('-*-' * 20)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: '))
        if resp == 'N':
            break
print(f'O total da compra foi de R${t}')
print(f'Temos {tm} produtos custando mais de R$1000')
print(f'O produto mais barato foi o(a) {n} custando R${m}')
