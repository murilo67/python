ma = 0
me = 0
for c in range(1, 6):
    p = float(input('Qual é o seu peso: '))
    if c == 1:
        ma = p
        me = p
    else:
        if p > ma:
            ma = p
        if p < me:
            me = p
print('O maior peso lido foi de {}Kg'.format(ma))
print('O menor peso lido foi de {} Kg'.format(me))