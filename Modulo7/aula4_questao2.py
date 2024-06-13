nome_arquivo_frase = "frase.txt"
nome_arquivo_palavras = "palavras.txt"

with open(nome_arquivo_frase, 'r') as arquivo_frase, open(nome_arquivo_palavras, 'w') as arquivo_palavras:
    frase = arquivo_frase.read()
    
    palavras = ''.join(c if c.isalnum() else ' ' for c in frase).split()
    
    for palavra in palavras:
        arquivo_palavras.write(palavra + "\n")

with open(nome_arquivo_palavras, 'r') as arquivo_palavras:
    conteudo = arquivo_palavras.read()
    print(conteudo)
