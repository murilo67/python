#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
sal = str(input('Digite uma frase: '))
stri = type(sal)
num = (sal.isnumeric())
alph = (sal.isalpha())
alnu = (sal.isalnum())
space = (sal.isspace())
upp = (sal.isupper())
low = (sal.islower())
til = (sal.istitle())
print('Seu tipo é \033[0;31;40m{}\033[m. '.format(stri))
print('Ele é numerico? \033[0;31;40m{}\033[m.'.format(num))
print('Ele é alpha? \033[0;31;40m{}\033[m.'.format(alph))
print('Ele é alphanumerico? \033[0;31;40m{}\033[m.'.format(alnu))
print('Tem espaços? \033[0;31;40m{}\033[m.'.format(space))
print('Tem letras maiúsculas? \033[0;31;40m{}\033[m.'.format(upp))
print('Tem letras minúsculas? \033[0;31;40m{}\033[m.'.format(low))
print('Ele é capitalizado? \033[0;31;40m{}\033[m.'.format(til))
