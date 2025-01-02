#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input("Digite a velocidade do carro em Km/h: "))

limite_velocidade = 80  # Limite de velocidade em Km/h
valor_multa_por_km = 7  # Valor da multa por cada Km acima do limite

if velocidade > limite_velocidade:
    # Calcular a quantidade de Km acima do limite
    km_acima = velocidade - limite_velocidade

    # Calcular o valor da multa
    valor_multa = km_acima * valor_multa_por_km

    print("Você foi multado! A velocidade excedeu o limite em {:.2f} Km/h.".format(km_acima))
    print("O valor da multa é R$ {:.2f}.".format(valor_multa))
else:
    print("Velocidade dentro do limite permitido.")
