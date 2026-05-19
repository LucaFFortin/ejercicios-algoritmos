def calcular_vampiros(v):
    list_v = list(str(v))
    combinaciones = [[]]

    if (len(list_v) < 4 or len(list_v) > 4):
        print(f"El numero debe tener 4 cifras, el ingresado fue tiene {len(list_v)} cifras")
        return
    
    for i, numero in enumerate(list_v):
            copia_list = list_v.copy()
            copia_list.pop(i)
            combinaciones[0] = [numero, copia_list[0]]
            copia_list.pop(0)
            rest = "".join(copia_list)
            print(combinaciones[0], rest)

        # print(caracter, i, list_v[i], )}

calcular_vampiros(1234)