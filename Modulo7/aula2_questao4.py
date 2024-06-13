def validador_senha(senha):
    if (len(senha) < 8 or 
        not any(char.isupper() for char in senha) or
        not any(char.islower() for char in senha) or
        not any(char.isdigit() for char in senha) or
        not any(char in "@#$" for char in senha)):
        return False
    return True

senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1)) 
print(validador_senha(senha2))  
print(validador_senha(senha3))  
