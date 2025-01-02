pri = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
ter = pri
con = 1
while con <= 10:
    print('{} - '.format(ter), end='')
    ter += ra
    con += 1
print('FIM')
