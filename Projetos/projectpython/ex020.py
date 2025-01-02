#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

# Lista com os nomes dos alunos
alunos = []

# Leitura dos nomes dos alunos
aluno1 = input("\033[1;32mDigite o nome do primeiro aluno: \033[0m")
alunos.append(aluno1)

aluno2 = input("\033[1;32mDigite o nome do segundo aluno: \033[0m")
alunos.append(aluno2)

aluno3 = input("\033[1;32mDigite o nome do terceiro aluno: \033[0m")
alunos.append(aluno3)

aluno4 = input("\033[1;32mDigite o nome do quarto aluno: \033[0m")
alunos.append(aluno4)

# Embaralhamento da ordem dos alunos
random.shuffle(alunos)

# Exibição do resultado
print("\033[1;36m--- Sorteio da Ordem de Apresentação ---\033[0m")
print("\033[1;34mOrdem de apresentação dos trabalhos:\033[0m")
print("\033[1;33m1º Aluno: {}\033[0m".format(alunos[0]))
print("\033[1;33m2º Aluno: {}\033[0m".format(alunos[1]))
print("\033[1;33m3º Aluno: {}\033[0m".format(alunos[2]))
print("\033[1;33m4º Aluno: {}\033[0m".format(alunos[3]))
