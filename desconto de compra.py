compras = float(input("Digite o valor da compra: "))

if compras <= 2000:
    taxa = 0.1
elif compras <= 3000:
    taxa = 0.05
elif compras <= 5000:
    taxa = 0.03
else:
    taxa = 0.02

desconto = compras*taxa
totpagar = compras - desconto

print("compras: R${0:.2f}".format(compras))
print("Desconto: R${0:.2f}".format(desconto))
print("Total: R${0:.2f}".format(totpagar))
