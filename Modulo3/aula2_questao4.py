classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").lower()
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

if classe == "guerreiro":
    pontos_validos = forca >= 15 and magia <= 10
elif classe == "mago":
    pontos_validos = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    pontos_validos = 5 < forca <= 15 and 5 < magia <= 15
else:
    pontos_validos = False 

print("Pontos de atributo consistentes com a classe escolhida:", pontos_validos)