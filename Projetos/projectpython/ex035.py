#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
a = int(input('Valor da casa: R$'))
b = int(input('Salário do comprador: R$'))
c = int(input('Quantos anos até o financiamento? '))
e = a / (c * 12)
f = b * 30 / 100
if e <= f:
    print('ACESSO LIBERADO, o valor não exedeu 30%, sua prestacão por mês foi de {:.2f}, sua casa será paga por {} anos com o valor da sua casa de {} reais.'.format(e, c, a))
else:
    print('ACESSO NEGADO, o valor exedeu 30%, sua prestacão por mês foi de {:.2f}, sua casa será paga por {} anos com o valor da sua casa de {} reais.'.format(e, c, a))
