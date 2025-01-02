n = []
for c in range(1, 6):
    n.append(int(input('Digite um valor: ')))

print('-*-' * 30)
print(n)

maior_valor = max(n)
menor_valor = min(n)

print(f'O maior valor é {maior_valor}')
print(f'O menor valor é {menor_valor}')

print('-*-' * 30)

indices_maior = []
indices_menor = []

for i, v in enumerate(n):
    if v == maior_valor:
        indices_maior.append(i)
    elif v == menor_valor:
        indices_menor.append(i)

print(f'O maior valor foi encontrado nas posições {indices_maior}')
print(f'O menor valor foi encontrado nas posições {indices_menor}')

print('-*-' * 30)
