pa = ('aprender', 'programar', 'linguagens', 'python',
       'curso', 'gratis', 'estudar', 'praticar',
      'trabalhar', 'mercado', 'porgramador', 'futuro')
for c in pa:
    print('\nNa palavra {} temos '.format(c), end='')
    for l in c:
        if l.lower() in 'aeiou':
            print(l, end=' ')
