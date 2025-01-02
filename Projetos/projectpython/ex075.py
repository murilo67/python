contador = 0
sub_string = '3'
n = (int(input('Digite um número (De 1 a 10) : ')),
     int(input('Digite outro número (De 1 a 10): ')),
     int(input('Digite mais um número (De 1 a 10): ')),
     int(input('Digite o último número (De 1 a 10): ')),)
print('-+-' * 20)
print(f'Você digitou os valores {n}')
print('-+-' * 20)

n_string = str(n)
print(f'O valor 9 apareceu {n_string.count("9")} vezes')
print('-+-' * 20)

if 3 in n:
    posicao = n.index(3)
    print(f'O valor 3 apareceu na posição {posicao + 1}')
else:
    print('O valor 3 não apareceu em nenhuma posição.')
print('-+-' * 20)
print(f'Os valores pares digitados foram ', end=' ')

for c in n:
    if c % 2 == 0:
        print(f'Os valores pares digitados foram {c}')

print('-+-' * 20)