n = 0
c = 0
s = 0
while n != 999:
    n = int(input('Digite um número [999 para  parar]: '))
    c += 1
    s += n
print('Acabou')
print('Você digitou {} números, e a soma foi {}'.format(c - 1, s - 999))
