def escreva(msg):
    quant = len(msg) + 4
    print('-' * quant)
    print(f'  {msg}')
    print('-' * quant)


escreva(str(input('Escreva o que quiser: ')))
