#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = input("Digite o nome da cidade: ")

# Verificação se o nome começa com "SANTO"
if cidade[:5].upper() == "SANTO":
    print("A cidade começa com o nome 'SANTO'.")
else:
    print("A cidade não começa com o nome 'SANTO'.")
