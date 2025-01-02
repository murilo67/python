def area(larg, comp):
    resul = larg * comp
    print(f'A área do terreno {larg}x{comp} é de {resul}')


print('-*-' * 7)
print('CONTROLE DE TERRENOS')
print('-*-' * 7)
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
area(a, b)
