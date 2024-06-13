frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
contagem_vogais = {}

for i, letra in enumerate(frase):
    if letra in vogais:
        if letra not in contagem_vogais:
            contagem_vogais[letra] = []
        contagem_vogais[letra].append(i)

total_vogais = sum(len(indices) for indices in contagem_vogais.values())
print(f"Total de vogais: {total_vogais}")
for vogal, indices in contagem_vogais.items():
    print(f"Vogal '{vogal}' encontrada nos índices: {indices}")
