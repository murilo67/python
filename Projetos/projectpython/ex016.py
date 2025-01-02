#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Leitura do número real
numero = float(input("\033[1;32mDigite um número real: \033[0m"))

# Obtendo a parte inteira do número
parte_inteira = int(numero)

# Exibição do resultado
print("\033[1;36m--- Obtendo a Parte Inteira de um Número Real ---\033[0m")
print("\033[1;34mNúmero real: \033[0m\033[1;33m{}\033[0m".format(numero))
print("\033[1;34mParte inteira: \033[0m\033[1;33m{}\033[0m".format(parte_inteira))
