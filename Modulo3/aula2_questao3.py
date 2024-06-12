idade = int(input("Digite sua idade: "))
jogou_tres_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ") == "True"
jogos_vencidos = int(input("Quantos jogos já venceu? "))


pode_ingressar = 16 <= idade <= 18 and jogou_tres_jogos and jogos_vencidos >= 1
print("Apto para ingressar no clube de jogos de tabuleiro:", pode_ingressar)
