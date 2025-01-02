#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes
a = float(input('Digite uma medida: '))
b = float(input('Digite outra medida: '))
c = float(input('Digite mais uma medida: '))
if a < b + c and b < c + a and c < b + a:
    print('É um triângulo!')
    if a == b == c:
        print('É um triângulo EQUILÁTERO.')
    elif a != b != c != a:
        print('É um triângulo ESCALENO.')
    else:
        print('É um triângulo ISÓSCELES.')

else:
    print('Não é um triângulo.')
