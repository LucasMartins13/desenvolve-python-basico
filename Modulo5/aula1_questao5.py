import emoji

lista_emojis = {
    ":smile:": "😄",
    ":heart:": "❤️",
    ":thumbs_up:": "👍",
    ":sun:": "☀️",
    ":star:": "⭐",
}

print("Lista de Emojis Disponíveis:")
for chave, valor in lista_emojis.items():
    print(f"{chave} -> {valor}")

frase_codificada = input("Digite uma frase com códigos de emojis: ")
frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)
print(f"Frase com Emojis: {frase_emojizada}")
