time = list()

while True:
    # Ler o nome do jogador
    aprota = dict()
    aprota['Nome'] = input('Nome do jogador: ')

    # Quantidade de gols (Lista)
    partidas = int(input('Partidas Jogadas: '))
    aprota1 = list()
    for c in range(0, partidas):
        gols = int(input(f' Gols na partida {c + 1}: '))
        aprota1.append(gols)
    aprota['Gols'] = aprota1

    # Total de gols
    total = sum(aprota1)
    aprota['Total'] = total

    time.append(aprota.copy())

    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite novamente')
        if resp == 'N':
            break

    print('-*-' * 20)

    if resp == 'N':
        break

print(f'{"cod":<4}{"Nome":<15}{"Gols":<25}{"Total":<5}')
print('-' * 50)
for i, jogador in enumerate(time):
    print(f'{i:<4}{jogador["Nome"]:<15}{str(jogador["Gols"]):<25}{jogador["Total"]:<5}')
print('-' * 50)

while True:
    busca = int(input('Mostrar código de qual jogador? [999 para parar]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        jogador = time[busca]
        print(f'O jogador {jogador["Nome"]} jogou em {len(jogador["Gols"])} partidas.')
        for i, gols in enumerate(jogador['Gols']):
            print(f'    Na partida {i + 1}, foram feitos {gols} gols.')
        print(f'Total: {jogador["Total"]}')

