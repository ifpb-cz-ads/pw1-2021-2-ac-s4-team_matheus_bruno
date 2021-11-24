""" 5. Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. 
Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00. """

pessoa1 = input('Informe o nome da primeira pessoa: ')
pessoa2 = input('Informe o nome da segunda pessoa: ')

salario_pessoa1 = float(input('Informe o salario da primeira pessoa: '))
salario_pessoa2 = float(input('Informe o salario da segunda pessoa: '))
salario_padrao = 1200


if(salario_pessoa1 > salario_padrao) and (salario_pessoa2 > salario_padrao):
    print('As duas pessoas: %s e %s devem pagar impostos, pois o salário é maior que %.2f' %(pessoa1, pessoa2, salario_padrao))
elif salario_pessoa1 > salario_padrao:
    print('Nome: %s deve pagar imposto, pois o salário é maior que %.2f' %(pessoa1, salario_padrao))
elif salario_pessoa2 > salario_padrao:
    print('Nome: %s deve pagar imposto, pois o salário é maior que %.2f' %(pessoa2,salario_padrao))
else:
    print('Nenhum dos dois deve pagar imposto, pois os salários sao menores que %f' %salario_padrao)