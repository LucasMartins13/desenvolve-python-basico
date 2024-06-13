n = int(input("informe o valor de n"))

maior = 0

if n>0:
    x = int(input("informe o valor de n"))
    if x > maior:
        maior = x
    else:
        n = n-1
else:
    print(maior)
