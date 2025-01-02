galera = list()
soma = media = 0
while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-*-' * 30)
print(f'Ao todo foram cadastradas {len(galera)} pessoas')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}, ', end='')
print()
print('A lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
        print()
print('<< ENCERRADO >>')
