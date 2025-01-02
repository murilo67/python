#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

# Leitura do comprimento dos catetos
cateto_oposto = float(input("\033[1;32mDigite o comprimento do cateto oposto: \033[0m"))
cateto_adjacente = float(input("\033[1;32mDigite o comprimento do cateto adjacente: \033[0m"))

# Cálculo do comprimento da hipotenusa
hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)

# Exibição do resultado
print("\033[1;36m--- Cálculo da Hipotenusa de um Triângulo Retângulo ---\033[0m")
print("\033[1;34mComprimento do cateto oposto: \033[0m\033[1;33m{:.2f}\033[0m".format(cateto_oposto))
print("\033[1;34mComprimento do cateto adjacente: \033[0m\033[1;33m{:.2f}\033[0m".format(cateto_adjacente))
print("\033[1;34mComprimento da hipotenusa: \033[0m\033[1;33m{:.2f}\033[0m".format(hipotenusa))
