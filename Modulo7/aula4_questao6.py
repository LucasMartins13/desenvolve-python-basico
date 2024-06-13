import csv

def limpar_nome_artistas(nome):
    if nome.startswith('"') and nome.endswith('"'):
        return nome[1:-1].replace('","', ',')
    return nome

musicas_populares = []

with open('spotify-2023.csv', newline='', encoding='latin-1') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    
    next(leitor)
    
    for linha in leitor:
        if len(linha) != 10:
            continue
        
        track_name = limpar_nome_artistas(linha[0])
        artist_name = limpar_nome_artistas(linha[1])
        artist_count = int(linha[2])
        released_year = int(linha[3])
        streams = int(linha[8])
        
        if 2012 <= released_year <= 2022 and artist_count == 1:
            musicas_populares.append([track_name, artist_name, released_year, streams])
    
    musicas_populares.sort(key=lambda x: x[2])

print("Lista das músicas mais populares de 2012 a 2022:")
for musica in musicas_populares:
    print(musica)
