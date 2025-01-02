ex = input('Digite a expressão: ')
pi = list()

for sim in ex:
    if sim == '(':
        pi.append('(')
    elif sim == ')':
        if len(pi) > 0:
            pi.pop()
        else:
            pi.append(')')
            break

if len(pi) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está inválida.')
