p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d  = p1 + (10 - 1) * r
for c in range(p1, d + r, r):
    print(c, end=' - ')
print('CABOOOOOOOO')
