# pedindo os números
print("Digite o primeiro número:")
print("Utilize números inteiros!")
n1 = int(input(""))
print("Digite o segundo número:")
print("Utilize números inteiros!")
n2 = int(input(""))
# crindo o menu
print("Escolha a operação desejada:")
print("----------------------------")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Média Simples")
print("Informe o número da operação desejada:")
op = int(input(""))
# iniciando calculos
if op == 1:
    res = n1 + n2
    print("O resultado da soma de {} e {} é igual a: {}.".format(n1, n2, res))
elif op == 2:
    res = n1 - n2
    print("O resultado da subtração de {} por {} é igual a: {}.".format(n1, n2, res))
elif op == 3:
    res = n1 * n2
    print("O resultado da multplicção de {} por {} é igual a: {}.".format(n1, n2, res))
elif op == 4:
    if n2 > 0:
        res = n1 / n2
        print("O resultado da divisão de {} por {} é igual a: {}.".format(n1, n2, res))
    elif n1 <= 0 or n2 <= 0:
        print("O programa não pode calcular a divisão pois um dos números digitados foi igual ou menor que 0 (zero)")
elif op == 5:
    res = (n1 + n2) / 2
    print("A média entre {} e {} é igual a: {}.".format(n1, n2, res))
else:
    print("Você digitou o número da operação corretamente, reinicie o programa e tente novamente.")
