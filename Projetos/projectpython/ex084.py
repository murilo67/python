pessoas = []
z = 0
while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    pessoas.append((nome, peso))
    z += 1
    sn = input('Quer continuar? [S/N]: ')
    if sn.lower() not in ('s', 'sim'):
        break
    print('-*-' * 20)

print(f'No total foram cadastradas {z} pessoas.')

pesos = [p[1] for p in pessoas]
print(f'O maior peso cadastrado foi de {max(pesos)}Kg:', end='')
for c in pessoas:
    if c[1] == max(pesos):
        print(f'[{c[0]}], ', end='')
print(f'O peso mais leve foi {min(pesos)}Kg.', end='')
for c in pessoas:
    if c[1] == min(pesos):
        print(f'[{c[0]}], ', end='')
