#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

# Leitura da largura e altura da parede
largura = float(input("\033[1;32mDigite a largura da parede em metros: \033[0m"))
altura = float(input("\033[1;32mDigite a altura da parede em metros: \033[0m"))

# Cálculo da área da parede
area = largura * altura

# Cálculo da quantidade de tinta necessária em litros
litros_tinta = area / 2

# Exibição do resultado
print("\033[1;36m--- Cálculo de Tinta para Pintar uma Parede ---\033[0m")
print("\033[1;34mÁrea da parede: \033[0m\033[1;33m{:.2f} m²\033[0m".format(area))
print("\033[1;34mQuantidade de tinta necessária: \033[0m\033[1;33m{:.2f} litros\033[0m".format(litros_tinta))
