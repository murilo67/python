#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
# Leitura da quantidade de km percorridos e dias de aluguel
km_percorridos = float(input("\033[1;32mDigite a quantidade de km percorridos: \033[0m"))
dias_aluguel = int(input("\033[1;32mDigite a quantidade de dias de aluguel: \033[0m"))

# Cálculo do preço a pagar
preco_km = 0.15 * km_percorridos
preco_dias = 60 * dias_aluguel
preco_total = preco_km + preco_dias

# Exibição do resultado
print("\033[1;36m--- Cálculo de Preço de Aluguel de Carro ---\033[0m")
print("\033[1;34mQuantidade de km percorridos: \033[0m\033[1;33m{:.2f} km\033[0m".format(km_percorridos))
print("\033[1;34mQuantidade de dias de aluguel: \033[0m\033[1;33m{}\033[0m".format(dias_aluguel))
print("\033[1;34mPreço por km percorrido: \033[0m\033[1;33mR$ {:.2f}\033[0m".format(preco_km))
print("\033[1;34mPreço por dias de aluguel: \033[0m\033[1;33mR$ {:.2f}\033[0m".format(preco_dias))
print("\033[1;34mPreço total a pagar: \033[0m\033[1;33mR$ {:.2f}\033[0m".format(preco_total))
