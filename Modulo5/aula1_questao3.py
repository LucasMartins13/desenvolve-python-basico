
import random

numero_secreto = random.randint(1, 10)
acertou = False

while not acertou:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        print("Parabéns! Você acertou.")
        acertou = True
