import math
altura = float(input("Digite a altura da parede em metros: "))
comprimento = float(input("Digite o comprimento da parede em metros: "))

area = altura * comprimento
cobertura_tinta = 3
volume_lata = 3.6
litros_tinta = area / cobertura_tinta
latas_tinta = math.ceil(litros_tinta / volume_lata)
preco_lata = 107.00
preco_total = latas_tinta * preco_lata


print(f"Você precisará de {latas_tinta} latas de tinta.")
print(f"O preço total será de R$ {preco_total:.2f}.")


