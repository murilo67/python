res = 'S'
soma = q = m = ma = me = 0
while res in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    q += 1
    if q == 1:
        ma = me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
    res = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
m = soma / q
print('Você digitou {} números e a média foi {}.'.format(q, m))
print('Já o maior número foi {} e o menor número foi {}.'.format(ma, me))
