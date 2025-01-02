camp = ('Sport Recife', 'Vila Nova', 'Criciúma', 'Novorizotino',
        'EC Vitória', 'Mirassol', 'Juventude', 'Guarani',
        'Atlético-GO', 'Ceará-SC', 'Botafogo SP', 'Ituano', 'CRB',
        'Ponte Preta', 'Sampaio Corrêa', 'Tombense', 'Chapecoense',
        'Londrina', 'Avaí', 'ABC')
print(f'''Os 5 primeiros times são {camp[1:6]}, já os últimos colocados do time são
{camp[17:]}. Aqui está os times em ordem alfabética {sorted(camp)} e o time Chapecoense está na posição {camp.index('Chapecoense')+1}º''')
