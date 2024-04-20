
altura = float(input("Digite a altura da parede: "))
comprimento = float(input("Digite o comprimento da parede: "))

parede  = altura*comprimento
litrosparede = parede/3
latas = litrosparede/3.6
preçoparede = latas*107


print("A quantidade de latas de tinta a serem compradas é: ", latas, ". O preço total será: ", preçoparede)


