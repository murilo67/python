from random import randint
v = (randint(0, 9), randint(0, 9), randint(0, 9),
     randint(0, 9), randint(0, 9))
m = (v)
print(m)
print(f'O maior valor sorteado foi {max(v)}')
print(f'O menor valor sorteado foi {min(v)}')
