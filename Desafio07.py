import time #importando para utilizar como 'delay' entre as funções do while
lista = {'Rodofonso': '11999999999', 'Robersvalda': '11988888888'} #'cadastro'
x = 0
while x < 6:
    x = int(input('Escolha uma das opções a seguir: \n'
          '--------------------------------\n'
          'Listar  .....................  1\n'
          'Buscar  .....................  2\n'
          'Adicionar  ..................  3\n'
          'Alterar  ....................  4\n'
          'Listar somente Nomes  .......  5\n'
          'Sair  .......................  6\n'
          'Obs: didite o Número da opção   \n'
          '--------------------------------\n'))

    if x == 1:
        print(lista)
        print('Aguarde alguns segundos')
        time.sleep(2.5) #utilizando o 'delay' para retornar a lista
    elif x == 2:
        nome = input('Digite o nome de quem você está buscando: ')
        print(lista.get(nome, "Essa pessoa não tem um número cadastrado no sistema ;-;"))
        print('Aguarde alguns segundos')
        time.sleep(2.5) #utilizando o 'delay' para retornar a lista
    elif x == 3:
        nome = input('Digite o nome de quem você deseja cadastrar: ')
        num = input('Digite o número da pessoa que você esta cadastrando: ')
        lista[nome] = num
        print(lista, '\nCadastro realizado com sucesso!')
        print('Aguarde alguns segundos')
        time.sleep(2.5) #utilizando o 'delay' para retornar a lista
    elif x == 4:
        nome = input('Digite o nome da pessoa de quem você quer alterar o número: ')
        if nome in lista: #procura o nome da pessoa no 'cadastro'
            numNovo = input('Digite o número novo: ')
            lista[nome] = numNovo
            print('Aguarde alguns segundos')
            time.sleep(2.5) #utilizando o 'delay' para retornar a lista
        else: #caso essa pessoa não esteja no 'cadastro'
            print('Esse nome não possui um cadastro. Por favor cadastre-a')
            print('Aguarde alguns segundos')
            time.sleep(2.5) #utilizando o 'delay' para retornar a lista
    elif x == 5:
        print('Nomes cadastrados:')
        for nome in lista.keys():
            print(nome)
        print('Aguarde alguns segundos')
        time.sleep(2.5)  # utilizando o 'delay' para retornar a lista
