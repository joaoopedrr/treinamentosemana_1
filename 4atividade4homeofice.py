def notar(*notas, situacao=False):
    informacoes = {}
    informacoes['Quantidade de notas'] = len(notas)
    informacoes['Maior nota'] = max(notas)
    informacoes['Menor nota'] = min(notas)
    informacoes['Média da turma'] = sum(notas) / len(notas)

    if situacao:
        media_minima_aprovacao = 7.0
        if informacoes['Média da turma'] >= media_minima_aprovacao:
            informacoes['Situação'] = 'Aprovado'
        else:
            informacoes['Situação'] = 'Reprovado'

    return informacoes

notas_alunos = (8.5, 7.2, 9.0, 6.8, 7.5)
resultado = notar(*notas_alunos, situacao=True)
print(resultado)
