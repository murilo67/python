#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
num = int(input('Digite um número: '))
a = num * 2
print('Seu dobro é \033[0;31;40m{}\033[m'.format(a))
b = num * 3
print('Seu triplo é \033[0;31;40m{}\033[m'.format(b))
c = num ** (1/2)
print('E sua raiz quadrada é \033[0;31;40m{}\033[m'.format(c))
