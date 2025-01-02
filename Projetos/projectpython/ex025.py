#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input("Digite uma frase: ")

# Contagem da letra "A"
quantidade_a = frase.upper().count('A')

# Posição da primeira ocorrência de "A"
primeira_posicao = frase.upper().find('A') + 1

# Posição da última ocorrência de "A"
ultima_posicao = frase.upper().rfind('A') + 1

# Exibição dos resultados
print("--- Informações sobre a Letra 'A' na Frase ---")
print("Quantidade de vezes que aparece: ", quantidade_a)
print("Posição da primeira ocorrência: ", primeira_posicao)
print("Posição da última ocorrência: ", ultima_posicao)
