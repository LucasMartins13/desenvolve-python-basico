import csv

# Dados dos livros
livros = [
    {"Título": "Dom Casmurro", "Autor": "Machado de Assis", "Ano de publicação": 1899, "Número de páginas": 256},
    {"Título": "1984", "Autor": "George Orwell", "Ano de publicação": 1949, "Número de páginas": 328},
    {"Título": "O Senhor dos Anéis", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1954, "Número de páginas": 1178},
    {"Título": "A Revolução dos Bichos", "Autor": "George Orwell", "Ano de publicação": 1945, "Número de páginas": 144},
    {"Título": "Harry Potter e a Pedra Filosofal", "Autor": "J.K. Rowling", "Ano de publicação": 1997, "Número de páginas": 223},
    {"Título": "Crime e Castigo", "Autor": "Fiódor Dostoiévski", "Ano de publicação": 1866, "Número de páginas": 551},
    {"Título": "O Pequeno Príncipe", "Autor": "Antoine de Saint-Exupéry", "Ano de publicação": 1943, "Número de páginas": 96},
    {"Título": "Cem Anos de Solidão", "Autor": "Gabriel García Márquez", "Ano de publicação": 1967, "Número de páginas": 417},
    {"Título": "A Metamorfose", "Autor": "Franz Kafka", "Ano de publicação": 1915, "Número de páginas": 55},
    {"Título": "A Revolução dos Bichos", "Autor": "George Orwell", "Ano de publicação": 1945, "Número de páginas": 144}
]

# Nome do arquivo CSV
nome_arquivo = "meus_livros.csv"

# Escrevendo os dados no arquivo CSV
with open(nome_arquivo, 'w', newline='') as arquivo_csv:
    colunas = ["Título", "Autor", "Ano de publicação", "Número de páginas"]
    escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)
    
    escritor.writeheader()
    
    for livro in livros:
        escritor.writerow(livro)

print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
