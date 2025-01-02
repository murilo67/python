num = list()
pares = list()
s = 0
for n in range(1, 10):
    valor = int(input(f'Digite o {n}º valor: '))
    num.append(valor)
print('-*-' * 20)
print(f'[{num[0]}] [{num[1]}] [{num[2]}] \n[{num[3]}] [{num[4]}] [{num[5]}] \n[{num[6]}] [{num[7]}] [{num[8]}]')
print('-*-' * 20)
for v in num:
    if v % 2 == 0:
        s += v
m = num[3], num[4], num[5]
print(f'A soma de todos os números pares é igual a {s}')
print(f'A soma de todos os valores da terceira coluna é igual a {num[2] + num[5] + num[8]}')
print(f'O maior valor registrado na segunda linha na matriz é {max(m)}')
