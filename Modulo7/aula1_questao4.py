numero = input("Digite seu número de celular: ")
if len(numero) == 8:
    numero = "9" + numero
if len(numero) == 9 and numero[0] != '9':
    print("Número inválido")
else:
    numero_formatado = numero[:5] + '-' + numero[5:]
    print(f"Número formatado: {numero_formatado}")
