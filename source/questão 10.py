salário = int(input("Informe o valor do salario:"))
aumento= int(input("informe a % do aumento no salario:"))
ValorAumento = salário*(aumento/100)
ValorSalario = salário+ValorAumento
TotalAumento = ValorSalario - salário
print("Seu salário de",salário,"vai para",ValorSalario,"com aumento de",TotalAumento)