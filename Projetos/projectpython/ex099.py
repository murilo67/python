def maior(*args):
    if len(args) == 0:
        print("Nenhum valor foi informado.")
        return None

    maior_valor = args[0]
    for valor in args:
        if valor > maior_valor:
            maior_valor = valor

    return maior_valor


# Teste do programa
valores = [10, 45, 23, 67, 1, 100]
resultado = maior(*valores)
print(f"O maior valor é: {resultado}")
