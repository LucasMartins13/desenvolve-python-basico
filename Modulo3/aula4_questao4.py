distancia = float(input("Insira a distância da entrega em quilômetros: "))
peso = float(input("Insira o peso do pacote em quilogramas: "))

if distancia <= 100:
    preco_por_kg = 1.00
elif 101 <= distancia <= 300:
    preco_por_kg = 1.50
else:
    preco_por_kg = 2.00

frete = peso * preco_por_kg

if peso > 10:
    frete += 10

print(f"O valor do frete é: R${frete:.2f}")
