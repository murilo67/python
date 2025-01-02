pa = list()
im = list()
n = list()
while True:
    n.append(int(input('Digite um número: ')))
    e = str(input('Quer continuar? [S/N]: '))
    if e in 'Nn':
        break
for i, v in enumerate(n):
    if v % 2 == 0:
        pa.append(v)
    elif v % 2 == 1:
        im.append(v)
print('-*-' * 20)
print(f'Pares: {pa}')
print(f'Ímpares: {im}')
