#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input("Digite o nome completo: ")

# Verificação se o nome contém "SILVA"
if "SILVA" in nome.upper():
    print("O nome contém 'SILVA'.")
else:
    print("O nome não contém 'SILVA'.")
