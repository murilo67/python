from datetime import date

ano_atual = date.today().year
maiores_idade = 0
menores_idade = 0

for c in range(1, 8):
    ano_nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1

print('Pessoas maiores de idade:', maiores_idade)
print('Pessoas menores de idade:', menores_idade)
