#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

genero = int(input('''
[ 1 ] Masculino
[ 2 ] Feminino
Digite seu sexo de acordo com o que está acima: '''))

ano_nascimento = int(input('Em que ano você nasceu? '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if genero == 1:
    if idade < 18:
        c = 18 - idade
        print('Ainda não está na hora. Faltam {} anos para você se alistar ao serviço militar.'.format(c))
    elif idade == 18:
        print('Está na hora certa de se alistar. Comece agora!')
    else:
        d = idade - 18
        print('Infelizmente já passou da hora. Já deveria ter se alistado há {} anos atrás.'.format(d))
elif genero == 2:
    print('Por conta de seu gênero, você não precisa se alistar para o serviço militar.')
else:
    print('Opção de gênero inválida. Digite 1 para Masculino ou 2 para Feminino.')
