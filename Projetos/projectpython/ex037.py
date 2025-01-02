#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro: '))
print('''Digite uma das bases para prosseguir:
[ 1 ] converter para base BINÁRIA
[ 2 ] converter para para base OCTAL
[ 3 ] converter para base HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('O número {} convertido para BINÁRIO é {}.'.format(num, bin(num)[2:]))
elif op == 2:
    print('O número {} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('O número {} convertido para HEXADECIMAL É {}'.format(num, hex(num)[2:]))
else:
    print('Deixe de ser malandro e digite o número certo!')
