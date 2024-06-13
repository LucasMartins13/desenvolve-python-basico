from itertools import permutations

palavra = input("Digite a palavra objetivo: ")
anagramas = set([''.join(p) for p in permutations(palavra)])
print(f"Anagramas de '{palavra}': {', '.join(anagramas)}")
