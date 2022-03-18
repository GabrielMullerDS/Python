# pedindo as medidas
print("Digite as 3 medidas da forma geométrica:")
print("Caso não tenha uma medida digite 0 (zero)")
L1 = float(input(""))
L2 = float(input(""))
L3 = float(input(""))
if L1 <= 0 or L2 <= 0 or L3 <= 0:
    if L1 <= 0 and L2 <= 0 and L3 <= 0:
        print("Não existem medidas")
    elif L1 <= 0 and L2 <= 0 or L2 <= 0 and L3 <= 0 or L3 <= 0 and L1 <= 0:
        print("Perante a apenas uma medida apresentada, isso seria uma reta")
    else:
        print("Perante a apenas duas medias apresentadas, isso seria um segmento de reta")
elif L1 == L2 and L1 == L3:
    print("Perante as medidas declaradas {}, {} e {} esse triangulo é um triangulo equilátero.".format(L1, L2, L3))
elif L1 == L2 or L2 == L3 or L3 == L1:
    print("Perante as medidas declaradas {}, {} e {} esse triangulo é um triangulo isóceles.".format(L1, L2, L3))
elif L1 != L2 or L2 != L3 or L3 != L1:
    print("Perante as medidas declaradas {}, {} e {} esse triangulo é um triangulo escaléno.".format(L1, L2, L3))
