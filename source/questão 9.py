dias = int (input ("insira a quantidade de dias:"))
horas= int (input ("insira a quantidade de horas:"))
minutos= int(input("insira a quantidade de minutos:"))
segundos = int(input("insira a quantidade de segundos:"))
soma = dias*86400+horas*3600+minutos*60
resultado = soma+segundos
print("o resultado é",resultado)
