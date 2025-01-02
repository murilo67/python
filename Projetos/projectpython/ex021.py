#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.
nome = input("Digite seu nome completo: ")

# Nome com todas as letras maiúsculas e minúsculas
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()

# Quantidade total de letras (sem considerar espaços)
quantidade_letras_total = 0
index = 0
while index < len(nome):
    if nome[index] != ' ':
        quantidade_letras_total += 1
    index += 1

# Quantidade de letras no primeiro nome
primeiro_nome = ''
index = 0
while index < len(nome) and nome[index] != ' ':
    primeiro_nome += nome[index]
    index += 1

quantidade_letras_primeiro_nome = 0
index = 0
while index < len(primeiro_nome):
    quantidade_letras_primeiro_nome += 1
    index += 1

# Exibição dos resultados
print("--- Informações sobre o Nome ---")
print("Nome em letras maiúsculas:", nome_maiusculo)
print("Nome em letras minúsculas:", nome_minusculo)
print("Quantidade total de letras:", quantidade_letras_total)
print("Quantidade de letras no primeiro nome:", quantidade_letras_primeiro_nome)
