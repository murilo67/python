# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
metros = float(input("\033[1;32mDigite um valor em metros: \033[0m"))
centimetros = metros * 100
milimetros = metros * 1000
print("\033[1;36m--- Conversão de Metros para Centímetros e Milímetros ---\033[0m")
print("\033[1;34mValor em metros: \033[0m\033[1;33m{:.2f}\033[0m".format(metros))
print("\033[1;34mValor em centímetros: \033[0m\033[1;33m{:.2f}\033[0m".format(centimetros))
print("\033[1;34mValor em milímetros: \033[0m\033[1;33m{:.2f}\033[0m".format(milimetros))
