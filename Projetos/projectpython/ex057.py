F = 'Feminino'
M = 'Masculino'

p = str(input('Qual é o seu sexo [F/M]: ')).upper()

while p != M and p != F:
    if p != M and p != F:
        p = str(input('Valor inválido. Digite novamente: ')).upper()
else:
    print('Valor válido')
print('Acabou')

