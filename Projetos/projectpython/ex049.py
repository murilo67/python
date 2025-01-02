#
n = int(input('Digite um número para ver sua tabuada: '))
for c in range(0, 11):
    print(c, 'x', n, end=' = ')
    print(c * n)
