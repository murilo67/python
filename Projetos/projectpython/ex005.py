#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input('Digite um número: '))
a = num + 1
b = num - 1
print('Considerando \033[0;31;40m{}\033[m como um número, temos o seu sucessor, que é \033[0;31;40m{}\033[m e seu antecessor, que é \033[0;31;40m{}\033[m.'.format(num, a, b))
