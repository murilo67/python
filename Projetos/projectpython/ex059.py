n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Mais números
    [5] Sair do programa''')
    op = int(input('>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Qual será a sua opção? '))
    if op == 1:
        s = n1 + n2
        print('A soma entre {} e {} é igual a {}.'.format(n1, n2, s))
    elif op == 2:
        pr = n1 * n2
        print('O resultado entre {} x {} é igual a {}.'.format(n1, n2, pr))
    elif op == 3:
        if n1 > n2:
            maior = n1
            print('O maior número dentre os digitados é {}.'.format(n1))
        else:
            maior = n2
            print('O maior número dentre os digitados é {}.'.format(n2))
    elif op == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('PROJETO FINALIZADO')
    else:
        print('Número inválido. DIGITE NOVAMENTE')
    print('=-=' * 20)
print('PROGRAMA FINALIZADO')