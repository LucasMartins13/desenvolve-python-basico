comprimento = int(input("Digite o comprimento do terreno (em metros): "))
largura = int(input("Digite a largura do terreno (em metros): "))
preco_m2 = float(input("Digite o preço do metro quadrado da região: "))

area_m2 = comprimento * largura

preco_total = preco_m2 * area_m2

print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")
