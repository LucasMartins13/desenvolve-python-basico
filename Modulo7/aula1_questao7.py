import random

nomes = ["Alice", "Bob", "Carol"]
n = random.randint(1, 10)
nomes_criptografados = []

for nome in nomes:
    nome_criptografado = ''.join(
        chr(((ord(c) - 33 + n) % 94) + 33) for c in nome)
    nomes_criptografados.append(nome_criptografado)

print(f"Nomes criptografados: {nomes_criptografados}")
print(f"Chave de criptografia: {n}")
