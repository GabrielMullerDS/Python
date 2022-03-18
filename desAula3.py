print("Digite 3 números: ")
print("Utilize . no lugar de ,")
n1 = float(input(""))
n2 = float(input(""))
n3 = float(input(""))
if n1 >= n2 and n1 >= n3:
    print("O Maior número é: {}".format(n1))
    if n1 == n2 and n2 == n3:
        print("Ambos os Três números são iguais")
    elif n1 == n2:
        print("O 1º e o 2º número são iguais")
    elif n1 == n3:
        print("O 1º e o 3º número são iguais")
    elif n2 == n3:
        print("O 2º e o 3º número são iguais")

elif n2 >= n1 and n2 >= n3:
    print("O Maior número é: {}".format(n2))
    if n1 == n2 and n2 == n3:
        print("Ambos os Três números são iguais")
    elif n1 == n2:
        print("O 1º e o 2º número são iguais")
    elif n1 == n3:
        print("O 1º e o 3º número são iguais")
    elif n2 == n3:
        print("O 2º e o 3º número são iguais")

elif n3 >= n1 and n3 >= n2:
    print("O Maior número é: {}".format(n3))
    if n1 == n2 and n2 == n3:
        print("Ambos os Três números são iguais")
    elif n1 == n2:
        print("O 1º e o 2º número são iguais")
    elif n1 == n3:
        print("O 1º e o 3º número são iguais")
    elif n2 == n3:
        print("O 2º e o 3º número são iguais")

else:
    print("O que você digitou não são números ;-;")
