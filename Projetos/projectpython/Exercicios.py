list_numero = []

for c in range(0, 4):
    numero = int(input('Digite um número: '))
    numero_string = str(numero)
    for c in numero_string:
        numero_especifico = numero_string.count('3')
        list_numero.append(numero_especifico)
list_numero_int = int(''.join(map(str, list_numero)))
soma = sum(int(list_numero_int) for numero in list_numero)
print(soma)


