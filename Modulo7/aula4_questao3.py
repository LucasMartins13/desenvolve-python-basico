import urllib.request

url = "https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt"
nome_arquivo_estomago = "estomago.txt"

urllib.request.urlretrieve(url, nome_arquivo_estomago)

with open(nome_arquivo_estomago, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    
    print("Texto das primeiras 25 linhas:")
    for i in range(25):
        print(linhas[i].strip())
    
    num_linhas = len(linhas)
    print(f"\nNúmero total de linhas: {num_linhas}")
    
    linha_mais_longa = max(linhas, key=len).strip()
    print(f"\nLinha com maior número de caracteres:\n{linha_mais_longa}")
    
    nome1 = "Nonato"
    nome2 = "Íria"
    contagem_nonato = sum(linha.lower().count(nome1.lower()) for linha in linhas)
    contagem_iria = sum(linha.lower().count(nome2.lower()) for linha in linhas)
    
    print(f"\nMenções aos nomes 'Nonato' e 'Íria':")
    print(f"{nome1}: {contagem_nonato} vezes")
    print(f"{nome2}: {contagem_iria} vezes")
