import random
from collections import Counter

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = list(set(lista1) & set(lista2))

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseccao:", sorted(interseccao))

contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

print("Contagem")
for elemento in interseccao:
    print(f"{elemento}: (lista1={contagem_lista1[elemento]}, lista2={contagem_lista2[elemento]})")
