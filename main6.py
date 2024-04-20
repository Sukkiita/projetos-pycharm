salario_bruto = int(input("Digite o salário bruto: "))

ir = (11*salario_bruto)/100
inss = (8*salario_bruto)/100
sindicato = (5*salario_bruto)/100
descontos = ir+inss+sindicato
salario_liquido = salario_bruto-descontos

print("O salário líquido será: ", salario_liquido)

