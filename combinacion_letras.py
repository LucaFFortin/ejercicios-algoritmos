def combinaciones_letras():
    combinaciones = []

    diccionario = {
        0: "a",
        1: "A",
        2: "b",
        3: "B",
        4: "c",
        5: "C",
    }

    combinacion = ["", "", ""]
    for i in range(0, 6):
        combinacion[0] = diccionario[i]
        for j in range(0, 6):
            combinacion[1] = diccionario[j]
            for k in range(0, 6):
                if diccionario[k] != combinacion[2]:
                    combinacion[2] = diccionario[k]
                    combinaciones.append("".join(combinacion))
            if diccionario[j] != combinacion[1]:
                combinacion[1] = diccionario[j]
                combinaciones.append("".join(combinacion))
        if diccionario[i] != combinacion[0]:
            combinacion[0] = diccionario[i]
            combinaciones.append("".join(combinacion))

    for combinacion in combinaciones:
        print(combinacion)
combinaciones_letras()