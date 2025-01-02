while True:
    a = int(input('Digite um número para ver sua tabuada: '))
    print('-*-' * 10)
    if a < 0:
        break
    for c in range(0, 11):
        print(f'{a} x {c} = {a*c}')
    print('-*-' * 10)
print('Acabou')
