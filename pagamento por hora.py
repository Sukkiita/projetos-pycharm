nivel = int(input("Digite o nível do professor (1 ou 2): "))
horas = int(input("Digite a quantidade de horas de aula dadas no mês: "))

if nivel == 1:
    salario = 56.00 * horas
else:
    salario = 66.00 * horas

dsr = salario * 0.15;
salario = salario + dsr;
print("O salário do professor é:{0:.2f}".format(salario))
