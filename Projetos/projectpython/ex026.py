#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome_completo = input("Digite o nome completo: ")

# Separar o nome em partes
partes_nome = nome_completo.split()

# Primeiro nome
primeiro_nome = partes_nome[0]

# Último nome
ultimo_nome = partes_nome[-1]

# Exibição dos resultados
print("--- Separação do Nome ---")
print("Primeiro nome: ", primeiro_nome)
print("Último nome: ", ultimo_nome)
