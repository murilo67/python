ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    m = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], m])  # Correção aqui: Adicionando uma lista contendo nome, notas e média.
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break

print('-*-' * 30)
for i, aluno in enumerate(ficha):  # Correção aqui: Usando a variável "aluno" para acessar os dados corretamente.
    nome = aluno[0]
    media = aluno[2]
    print(f'Média do Aluno {i} ({nome}): {media}')

while True:
    print('-*-' * 30)
    opc = int(input('Mostrar nota de qual aluno (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        aluno = ficha[opc]
        nome = aluno[0]
        notas = aluno[1]
        print(f'Notas de {nome} são {notas}')
