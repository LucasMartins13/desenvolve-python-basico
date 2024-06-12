ano = int(input("Insira um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não Bissexto")

for ano in [1900, 2000, 2016, 2017]:
    print(f"Ano {ano}: ", end="")
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("Bissexto")
    else:
        print("Não Bissexto")
