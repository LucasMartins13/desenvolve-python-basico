num1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input(f"Digite o elemento {i+1} da lista 1: ")) for i in range(num1)]

num2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = [int(input(f"Digite o elemento {i+1} da lista 2: ")) for i in range(num2)]

lista_intercalada = []
min_length = min(num1, num2)

for i in range(min_length):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

if num1 > num2:
    lista_intercalada.extend(lista1[min_length:])
else:
    lista_intercalada.extend(lista2[min_length:])

print("Lista intercalada:", lista_intercalada)
