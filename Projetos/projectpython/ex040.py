#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO
import math
n1 = float(input('Primeira nota (Proccessual): '))
n2 = float(input('Segunda nota (Formal): '))
c = (n1 + (n2 * 2)) / 3
if c >= 6:
    print('Você tirou {:.2f}. Você foi APROVADO.'.format(c))
elif c < 6:
    print('Você tirou {:.2f}. Infelizmente precisará ir para REPOSIÇÃO.'.format(c))
    r = (6 * 2) - c
    m = math.ceil(r)
    print('Você vai precisar de {} pontos para passar.'.format(m))
