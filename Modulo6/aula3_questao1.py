numeros = []
print("Digite pelo menos 4 números inteiros (digite 'sair' para finalizar):")

while True:
    entrada = input("Número: ")
    if entrada.lower() == 'sair':
        if len(numeros) >= 4:
            break
        else:
            print("Por favor, insira pelo menos 4 números.")
    else:
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

print("Lista original:", numeros)
print("Os 3 primeiros elementos:", numeros[:3])
print("Os 2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])
