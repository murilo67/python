a = int(input('Digite um número: '))
divisores = 0

for c in range(1, a + 1):
    if a % c == 0:
        divisores += 1

if divisores == 2:
    print(a, "é um número primo.")
else:
    print(a, "não é um número primo.")
    