#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: O primeiro valor é maior, O segundo valor é maior, Não existe valor maior, os dois são iguais.
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
if a > b:
    print('O PRIMEIRO valor é MAIOR.')
elif b > a:
    print('O SEGUNDO valor é MAIOR.')
else:
    print('Os dois valores são IGUAIS.')
