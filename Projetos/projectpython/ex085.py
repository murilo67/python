pi = list()
pares = list()
impares = list()
for c in range(1, 8):
    a = int(input(f'Digite o {c}º valor: '))
    pi.append(a)
for n in pi:
    if n % 2 == 0:
        pares.append(n)
        pares.sort()
    elif n % 2 == 1:
        impares.append(n)
        impares.sort()
print(f'Números Pares: {pares}')
print(f'Números Ímpares: {impares}')
