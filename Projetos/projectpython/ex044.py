#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros
preco_produto = float(input("Digite o preço do produto: "))
condicao_pagamento = input("Digite a condição de pagamento (dinheiro, cheque, cartao a vista, cartao 2x, cartao 3x ou mais): ")

if condicao_pagamento == "dinheiro" or condicao_pagamento == "cheque":
    valor_final = preco_produto - (preco_produto * 0.1)  # 10% de desconto
elif condicao_pagamento == "cartao a vista":
    valor_final = preco_produto - (preco_produto * 0.05)  # 5% de desconto
elif condicao_pagamento == "cartao 2x":
    valor_final = preco_produto  # preço normal
elif condicao_pagamento == "cartao 3x ou mais":
    valor_final = preco_produto + (preco_produto * 0.2)  # 20% de juros
else:
    valor_final = "Condição de pagamento inválida."

print("Valor a ser pago: R$", valor_final)
