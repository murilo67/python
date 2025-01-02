pri = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
ter = pri
con = 1
tot = 0
ma = 10
while ma != 0:
    tot = tot + ma
    while con <= tot:
        print('{} - '.format(ter), end='')
        ter += ra
        con += 1
    print('PAUSA')
    ma = int(input('Quantos termos que você quer mostrar a mais? '))
print('GERADOR DE PA FINALIZADO')
