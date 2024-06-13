import random

def escolhe_palavra():
    with open("gabarito_forca.txt", 'r') as arquivo:
        palavras = arquivo.readlines()
        return random.choice(palavras).strip().lower()

def imprime_enforcado(erros):
    estagios_enforcado = [
        """
         _______
        |/      |
        |
        |
        |
        |
      __|________
      |         |
      |_________|
        """,
        """
         _______
        |/      |
        |      (_)
        |
        |
        |
      __|________
      |         |
      |_________|
        """,
        """
         _______
        |/      |
        |      (_)
        |       |
        |
        |
      __|________
      |         |
      |_________|
        """,
        """
         _______
        |/      |
        |      (_)
        |      /|
        |
        |
      __|________
      |         |
      |_________|
        """,
        """
         _______
        |/      |
        |      (_)
        |      /|\\
        |
        |
      __|________
      |         |
      |_________|
        """,
        """
         _______
        |/      |
        |      (_)
        |      /|\\
        |      /
        |
      __|________
      |         |
      |_________|
        """,
        """
         _______
        |/      |
        |      (_)
        |      /|\\
        |      / \\
        |
      __|________
      |         |
      |_________|
        """
    ]
    
    print(estagios_enforcado[erros])

def main():
    palavra = escolhe_palavra()
    tamanho_palavra = len(palavra)
    letras_acertadas = ['_'] * tamanho_palavra
    letras_digitadas = []
    tentativas = 0
    max_tentativas = 6
    
    print("Bem-vindo ao jogo da forca!")
    print(f"A palavra tem {tamanho_palavra} letras.")
    print("".join(letras_acertadas))
    
    while '_' in letras_acertadas and tentativas < max_tentativas:
        letra = input("\nDigite uma letra: ").lower()
        
        if letra in letras_digitadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        letras_digitadas.append(letra)
        
        if letra in palavra:
            print("Letra correta!")
            for i in range(tamanho_palavra):
                if palavra[i] == letra:
                    letras_acertadas[i] = letra
        else:
            print("Letra incorreta!")
            tentativas += 1
            imprime_enforcado(tentativas)
        
        print("".join(letras_acertadas))
    
    if '_' not in letras_acertadas:
        print("\nParabéns, você ganhou!")
    else:
        print("\nInfelizmente você perdeu. A palavra era:", palavra)

if __name__ == "__main__":
    main()
