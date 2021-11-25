diaria = 60
km = 0.15
KmRodados = int(input("informe os km rodados:"))
QuantDias = int(input("informe a quantos dias o veiculo foi alugado:"))
Total = (KmRodados*km) + (QuantDias*diaria)
print("Total do aluguel é de:",Total,"$")