#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# Leitura do preço do produto
preco = float(input("\033[1;32mDigite o preço do produto: R$ \033[0m"))

# Cálculo do desconto de 5%
desconto = 0.05 * preco

# Cálculo do novo preço com desconto
novo_preco = preco - desconto

# Exibição do resultado
print("\033[1;36m--- Cálculo de Desconto em um Produto ---\033[0m")
print("\033[1;34mPreço original: R$ {:.2f}\033[0m".format(preco))
print("\033[1;34mDesconto de 5%: R$ {:.2f}\033[0m".format(desconto))
print("\033[1;34mNovo preço com desconto: R$ {:.2f}\033[0m".format(novo_preco))

