c = ('zero', 'um', 'dois', 'três', 'quatro',
      'cinco', 'seis', 'sete', 'oito', 'nove',
      'deis', 'onze', 'doze', 'treze', 'quatorze',
      'quinze', 'dezesseis', 'dezessete', 'dezoito', 'desenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
while True:
      n = int(input('Digite um número entre 0 e 20: '))
      if 0 <= n <= 20:
            break
      print('Tente novamente: ')
print(f'Você digitou o numero {c[n]}')