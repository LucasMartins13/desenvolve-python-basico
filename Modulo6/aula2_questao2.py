import random

num_elementos = random.randint(5, 20)

elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Imprimir a lista
print("Lista elementos:", elementos)

soma_elementos = sum(elementos)
print("Soma dos valores:", soma_elementos)

media_elementos = soma_elementos / num_elementos
print("Média dos valores:", media_elementos)
