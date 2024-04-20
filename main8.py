premio = float(input("Digite o valor total do prêmio: "))

imposto = (7*premio)/100
premio_liquido = premio-imposto
primeiro = (46*premio_liquido)/100
segundo = (32*premio_liquido)/100
terceiro = (22*premio_liquido)/100


print("O valor do prêmio é: ", premio)
print("O valor do prêmio descontado será: ", premio_liquido)
print("O valor do desconto será: ", imposto)
print("O primeiro ganhador receberá: ", primeiro)
print("O segundo ganhador receberá: ", segundo)
print("O terceiro ganhador receberá: ", terceiro)

