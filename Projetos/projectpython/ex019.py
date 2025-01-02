#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
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

# Sorteio do aluno escolhido
escolhido = random.choice(alunos)

# Exibição do resultado
print("\033[1;36m--- Sorteio do Aluno para Apagar o Quadro ---\033[0m")
print("\033[1;34mAlunos participantes:\033[0m")
print("\033[1;33m- {}\033[0m".format(aluno1))
print("\033[1;33m- {}\033[0m".format(aluno2))
print("\033[1;33m- {}\033[0m".format(aluno3))
print("\033[1;33m- {}\033[0m".format(aluno4))
print("\033[1;34mAluno escolhido para apagar o quadro: \033[0m\033[1;33m{}\033[0m".format(escolhido))
