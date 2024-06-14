import csv

def carregar_usuarios(arquivo):
    usuarios = {}
    with open(arquivo, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            usuarios[row['ID']] = {
                'nome': row['Nome'],
                'senha': row['Senha'],
                'permissao': row['Permissao']
            }
    return usuarios

def salvar_usuarios(arquivo, usuarios):
    with open(arquivo, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ID', 'Nome', 'Senha', 'Permissao'])
        writer.writeheader()
        for id, dados in usuarios.items():
            row = {'ID': id, 'Nome': dados['nome'], 'Senha': dados['senha'], 'Permissao': dados['permissao']}
            writer.writerow(row)

def criar_usuario(usuarios, id, nome, senha, permissao):
    if id in usuarios:
        return "ID já existe."
    usuarios[id] = {'nome': nome, 'senha': senha, 'permissao': permissao}
    return "Usuário criado com sucesso."

def listar_usuarios(usuarios):
    for id, dados in usuarios.items():
        print(f"ID: {id}, Nome: {dados['nome']}, Permissao: {dados['permissao']}")

def atualizar_usuario(usuarios, id, nome=None, senha=None, permissao=None):
    if id not in usuarios:
        return "ID não encontrado."
    if nome:
        usuarios[id]['nome'] = nome
    if senha:
        usuarios[id]['senha'] = senha
    if permissao:
        usuarios[id]['permissao'] = permissao
    return "Usuário atualizado com sucesso."

def deletar_usuario(usuarios, id):
    if id in usuarios:
        del usuarios[id]
        return "Usuário deletado com sucesso."
    return "ID não encontrado."

def main():
    arquivo_usuarios = 'usuarios.csv'
    
    usuarios = carregar_usuarios(arquivo_usuarios)
    
    print(criar_usuario(usuarios, '4', 'Carlos', 'senha123', 'funcionario'))
    
    print("Lista de usuários:")
    listar_usuarios(usuarios)
    
    print(atualizar_usuario(usuarios, '4', senha='nova_senha'))
    
    print(deletar_usuario(usuarios, '4'))
    
    salvar_usuarios(arquivo_usuarios, usuarios)

if __name__ == "__main__":
    main()