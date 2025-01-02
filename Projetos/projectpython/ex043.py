#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
pes = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = pes / (alt ** 2)
if imc < 18.5:
    print('Com {} Kg e com {} metros de altura, seu IMC é de {:.2f}. Você está ABAIXO DO PESO.'.format(pes, alt, imc))
elif 25 > imc > 18.5:
    print('Com {} Kg e com {} metros de altura, seu IMC é de {:.2f}. Você está no PESO IDEAL.'.format(pes, alt, imc))
elif 30 > imc > 25:
    print('Com {} Kg e com {} metros de altura, seu IMC é de {:.2f}. Você está no SOBREPESO.'.format(pes, alt, imc))
elif 40 > imc > 30:
    print('Com {} Kg e com {} metros de altura, seu IMC é de {:.2f}. Você está na OBESIDADE.'.format(pes, alt, imc))
else:
    print('Com {} Kg e com {} metros de altura, seu IMC é de {:.2f}. Você está com OBESIDADE MÓRBIDA.'.format(pes, alt, imc))
