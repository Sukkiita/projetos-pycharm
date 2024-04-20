paes = float(input("Digite a quantidade de pães: "))
broas = float(input("Digite a quantidade de broas: "))
total_de_itens = paes+broas
preçopaes = paes*0.80
preçobroas = broas*2.50

vendatotal = preçopaes+preçobroas
fabricaçao = (43*vendatotal)/100
lucro = vendatotal-fabricaçao
poupança = ((15*lucro)/100)
euro = ((15*lucro)/100)/4.60

print("Quantidade de pães e broas vendidas: ", total_de_itens)
print("Valor da venda total de pães e broas: ", vendatotal)
print("Custo de fabricação: ", fabricaçao)
print("Valor a ser guardado na poupança: ", poupança)
print("Euros a serem comprados: ", euro)


