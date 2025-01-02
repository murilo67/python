#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Leitura do valor em reais
valor_reais = float(input("\033[1;32mDigite a quantidade de dinheiro em reais: \033[0m"))

# Taxa de câmbio
cambio = 5.50

# Cálculo do valor em dólares
valor_dolares = valor_reais / cambio

# Exibição do resultado
print("\033[1;36m--- Conversão de Reais para Dólares ---\033[0m")
print("\033[1;34mValor em reais: \033[0m\033[1;33mR$ {:.2f}\033[0m".format(valor_reais))
print("\033[1;34mValor em dólares: \033[0m\033[1;33mUS$ {:.2f}\033[0m".format(valor_dolares))
