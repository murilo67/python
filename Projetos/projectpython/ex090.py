boletim = {
    'Nome': input('Nome: '),
    'Média do aluno': float(input('Média escolar do aluno: '))
}
situacao = 'APROVADO' if boletim['Média do aluno'] >= 6.00 else 'REPROVADO'

print(f'''Nome: {boletim['Nome']}
Média: {boletim['Média do aluno']}
Sua situação final é igual a {situacao}''')
