#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# Leitura da temperatura em graus Celsius
celsius = float(input("\033[1;32mDigite a temperatura em graus Celsius: \033[0m"))

# Conversão para graus Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Exibição do resultado
print("\033[1;36m--- Conversão de Temperatura ---\033[0m")
print("\033[1;34mTemperatura em graus Celsius: \033[0m\033[1;33m{:.2f} °C\033[0m".format(celsius))
print("\033[1;34mTemperatura em graus Fahrenheit: \033[0m\033[1;33m{:.2f} °F\033[0m".format(fahrenheit))
