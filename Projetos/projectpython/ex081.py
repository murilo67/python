valor = list()
while True:
    c = valor.append(int(input('Digite um valor: ')))
    s = str(input('Quer continuar? [S/N]: '))
    if s in 'Nn':
        break
print('-*-' * 20)
print(f'O número de valores digitados foi de {len(valor)}')
valor.sort(reverse=True)
print(f'Lista de valores em ordem decrescente: {valor}')
if 5 in valor:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
