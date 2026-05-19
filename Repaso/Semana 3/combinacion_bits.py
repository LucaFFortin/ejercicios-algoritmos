def combinaciones_bits():
    combinaciones = []

    for i in range(16):
        combinaciones.append(str(bin(i)))

    for combinacion in combinaciones:
        combinacion_formateada = combinacion.replace("0b", "")
        if (len(combinacion_formateada) < 4):
            # print(type(combinacion_formateada))
            combinacion_formateada = combinacion_formateada.zfill(4)
        print(combinacion_formateada)

combinaciones_bits()