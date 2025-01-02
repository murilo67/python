# Colocar no dicionário:
import datetime

ctps = dict()
    # Ler o nome
ctps['Nome'] = str(input('Nome: '))

    # Ler o ano de nascimento (com idade)
ano = datetime.datetime.now().year
nasci = int(input('Ano de nascimento: '))
idade = ano - nasci
ctps['Idade'] = idade

    # Saber se tem uma carteira de trabalho (CTPS) ou não tem
cart = int(input('Carteira de Trabalho (0 para não tem): '))
if cart == 0:
    ctps['CTPS'] = cart
    print('-*-' * 30)
    for k, v in ctps.items():
        print(f'{k}: {v}')
else:
    ctps['CTPS'] = cart
    # Saber o ano de contratação (tempo que trabalha)
    ctps['Ano de contratação'] = int(input('Ano de contratação: '))
    # saber o salário
    ctps['Salário'] = int(input('Salário: R$'))
    # Máquina dirá quanto tempo falta para se aposentar e tudo acima
    apos = 65 - idade
    ctps['Aposentadoria'] = ctps['Idade'] + ((ctps['Ano de contratação'] + 35) - ano)
    print('-*-' * 30)
    for k, v in ctps.items():
        print(f'{k}: {v}')
