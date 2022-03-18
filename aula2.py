altura, largura, paredes, balde = float(input("Digite sua altura da parede: ")), float(input("Digite a largura da parede: ")), int(input("Quantas paredes você quer pintar? ")), float(300)
paredeM2 = altura * largura
totalParede = paredes * paredeM2
baldes = totalParede / balde
print("Baseado na altura {} e na largura de {} das paredes, são {}m2, você irá precisar de {:.2f} baldes.".format(altura, largura, paredeM2, baldes))
