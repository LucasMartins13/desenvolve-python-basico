import random

valores = [random.randint(-100, 100) for _ in range(20)]

valores_ordenados = sorted(valores)
print("Lista ordenada:", valores_ordenados)

print("Lista original:", valores)

indice_maior = valores.index(max(valores))
print("Índice do maior valor:", indice_maior)

indice_menor = valores.index(min(valores))
print("Índice do menor valor:", indice_menor)
