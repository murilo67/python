s = 0
for c in range(0, 501, 2):
    if c % 3 == 0:
        s = s + c
print ('A soma dos números ímpares multiplos de 3 é igual a {}'.format(s))
