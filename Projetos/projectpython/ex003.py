#Crie um programa que leia dois números e mostre a soma entre eles.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
som = num1 + num2
print('\033[0;31;40m A soma entre \033[0;32;40m{} \033[0;31;40me \033[0;32;40m{} \033[0;31;40mé igual a \033[0;32;40m{}\033[m'.format(num1, num2, som))