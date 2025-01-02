#  Colocar no dicionário
aprota = dict()
aprota1 = list()
soma = 0
    # Ler o nome do jogador
aprota['Nome'] = str(input('Nome do jogador: '))

    # Quantidade de gols (Lista)
partidas = int(input('Partidas Jogadas: '))
for c in range(0, partidas):
    gols = int(input(f' Gols na partida {c}: '))
    aprota1.append(gols)
    aprota['Gols'] = aprota1

    # Total de gols
total = sum(aprota1)
aprota['Total'] = total

    # Mostrar dicionário
print('-*-' * 20)
print(aprota)
print('-*-' * 20)

# Organizar o nome
# Organizar os gols
# Organizar o total de gols
for k, v in aprota.items():
    print(f'{k}: {v}')
print('-*-' * 20)

# Organizar os gols por partida
print(f'O jogador {aprota["Nome"]} jogou em {len(aprota1)} partidas.')
for i, o in enumerate(aprota1):
    print(f'    Na partida {i}, foram feitos {o} gols.')
print(f'Total: {total}')

