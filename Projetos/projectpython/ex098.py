from time import sleep

def contador(inicio, fim, passo):
    for c in range(inicio, fim, passo):
        print(c, end=' ', flush=True)
        sleep(1)
    print()


# Contagem de 1 a 10 com um passo de 1
for i in range(1, 10 + 1, 1):
    print(i, end=' ', flush=True)
    sleep(1)
print()

# Contagem de 10 a 0 com um passo de -2
for j in range(10, 0 - 1, -2):
    print(j, end=' ', flush=True)
    sleep(2)
print()

# Obter entrada do usuário e contar usando a função definida
ini = int(input('Início: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fi, pas)
