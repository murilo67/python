# Ler a frase do usuário
frase = input("Digite uma frase: ")

# Remover espaços em branco da frase
frase_sem_espacos = frase.replace(" ", "")

# Converter a frase para letras minúsculas
frase_sem_espacos = frase_sem_espacos.lower()

# Verificar se a frase invertida é igual à original
if frase_sem_espacos == frase_sem_espacos[::-1]:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
