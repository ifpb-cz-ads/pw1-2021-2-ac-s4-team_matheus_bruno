""" 6. Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado.
Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas 
três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e 
matéria3. """

nome_aluno = input('Informe o nome do aluno:')
materia1 = float(input('Informe a média de Matemática: '))
materia2 = float(input('Informe a média de Física: '))
materia3 = float(input('Informe a média de Geografia: '))

nota_padrao = 7

if (materia1 > nota_padrao) and (materia2 > nota_padrao) and (materia3 > nota_padrao):
    print('O aluno %s foi aprovado, pois tirou em todas as matérias uma nota acima de %d' %(nome_aluno, nota_padrao))
else:
    print('O aluno %s reprovou' %nome_aluno)