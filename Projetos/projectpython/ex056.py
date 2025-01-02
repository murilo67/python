f = 0
mi = 0

for c in range(1, 5):
    n = input('Qual o nome da {}ª pessoa: '.format(c)).strip()
    i = int(input('Qual a idade da {}ª pessoa: '.format(c)))
    s = int(input('''Digite [1] para MASCULINO
Digite [2] para FEMININO
Qual é o seu sexo? '''))

    if s == 2:
        f += 1

    if s == 1 and i < 20:
        a += 1

    mi += i

print('Das 4 pessoas entrevistadas, {} pessoas são mulheres.'.format(f))
print('Das 4 pessoas entrevistadas, {} pessoas são do sexo masculino e têm menos de 20 anos.'.format(a))
print('Há uma média de {} anos das 4 pessoas entrevistadas.'.format(mi / 4))
