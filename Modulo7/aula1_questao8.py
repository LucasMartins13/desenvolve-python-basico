cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

cpf_numeros = cpf.replace('.', '').replace('-', '')

def calcular_digito_verificador(cpf, multiplicadores):
    soma = sum(int(a) * b for a, b in zip(cpf, multiplicadores))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

if len(cpf_numeros) != 11 or not cpf_numeros.isdigit():
    print("CPF inválido")
else:
    primeiro_digito = calcular_digito_verificador(cpf_numeros[:9], range(10, 1, -1))
    segundo_digito = calcular_digito_verificador(cpf_numeros[:9] + str(primeiro_digito), range(11, 1, -1))

    if cpf_numeros[-2:] == f"{primeiro_digito}{segundo_digito}":
        print("CPF válido")
    else:
        print("CPF inválido")
