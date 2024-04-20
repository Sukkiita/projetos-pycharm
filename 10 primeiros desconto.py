for i in range(10):
    nome = input("Digite o seu nome: ")
    compra = float(input("Digite o valor da compra: "))
    if compra >= 1500:
        desconto = (25*compra)/100
    else:
        desconto = (20*compra)/100

    valor_pago = compra - desconto

    print("Nome:", nome)
    print("O valor da compra é:", compra)
    print("O valor do desconto é:", desconto)
    print("O valor a ser pago é:", valor_pago)

print("O valor total de descontos oferecidos foi:", desconto)









