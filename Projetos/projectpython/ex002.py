#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
msg = input('Qual é o seu nome? ')
print('\033[0;31;40mÉ um prazer te conhecer {}\033[m.'.format(msg) )
