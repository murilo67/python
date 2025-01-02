valores = []
while True:
    valor = int(input('Digite um valor (ou 0 para sair): '))
    if valor == 0:
        break
    if valor not in valores:
        valores.append(valor)

valores.sort()
print('Valores únicos digitados, em ordem crescente:')
print(valores)
