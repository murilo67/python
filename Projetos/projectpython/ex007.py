#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média ponderada.
flow = float(input('Digite a primeira nota do aluno: '))
flow1 = float(input('Digite a outra nota do aluno: '))
peso1 = 1
peso2 = 2
conta = ((flow * peso1) + (flow1 * peso2)) / (peso1 + peso2)
print('Sua nota é \033[0;31;40m{}\033[m.'.format(conta))
