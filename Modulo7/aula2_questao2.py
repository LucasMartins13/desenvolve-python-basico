def substituir_vogais_por_asterisco():
    frase = input("Digite uma frase: ")
    vogais = "aeiouAEIOU"
    
    for vogal in vogais:
        frase = frase.replace(vogal, "*")
    
    print(f"Frase modificada: {frase}")

substituir_vogais_por_asterisco()
