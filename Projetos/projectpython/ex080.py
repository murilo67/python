valor = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valor[-1]:
        valor.append(n)
    else:
        pos = 0
        while pos < len(valor):
            if n <= valor[pos]:
                valor.insert(pos, n)
                break
            pos += 1
print(f'Os valores digitados foram {valor}')
