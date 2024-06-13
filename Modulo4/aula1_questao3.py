n1 = int(input("Informe o valor de n1"))
n2 = int(input("Informe o valor de n2"))
n3 = int(input("Informe o valor de n3"))

m = (n1 + n2 + n3)/3

if m>=60:
    print("aprovado")
elif m>=40 and m<60:
    print("Recuperaçao")
else:
    print("Reprovado")