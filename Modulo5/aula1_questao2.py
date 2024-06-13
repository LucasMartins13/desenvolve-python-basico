import random
import math

n = int(input("Insira o valor de n: "))
valores = [random.randint(0, 100) for _ in range(n)]
soma = sum(valores)
raiz_quadrada = math.sqrt(soma)
print(f"A raiz quadrada da soma dos valores é: {raiz_quadrada}")
