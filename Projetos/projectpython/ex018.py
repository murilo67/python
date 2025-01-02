#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

# Leitura do ângulo
angulo = float(input("\033[1;32mDigite um ângulo em graus: \033[0m"))

# Conversão do ângulo para radianos
angulo_rad = math.radians(angulo)

# Cálculo do seno, cosseno e tangente
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

# Exibição do resultado
print("\033[1;36m--- Cálculo do Seno, Cosseno e Tangente de um Ângulo ---\033[0m")
print("\033[1;34mÂngulo: \033[0m\033[1;33m{:.2f}°\033[0m".format(angulo))
print("\033[1;34mSeno: \033[0m\033[1;33m{:.2f}\033[0m".format(seno))
print("\033[1;34mCosseno: \033[0m\033[1;33m{:.2f}\033[0m".format(cosseno))
print("\033[1;34mTangente: \033[0m\033[1;33m{:.2f}\033[0m".format(tangente))
