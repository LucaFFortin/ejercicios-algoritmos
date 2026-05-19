def lectorMatriz(matriz):
    dimensiones = [0, 0]
    mayor = [matriz[0][0], 0, 0]
    menor = [matriz[0][0], 0, 0]
    
    for i, valorI in enumerate(matriz):
        dimensiones.insert(0, i + 1)
        for j, valorJ in enumerate(valorI):
            dimensiones.insert(1, j + 1)
            if (valorJ > mayor[0]):
                mayor = [matriz[i][j], i, j]
            if (valorJ < menor[0]):
                menor = [matriz[i][j], i, j]
                
    print(f"dimensiones: {dimensiones[0]}x{dimensiones[1]}")
    print(f"numero mayor: {mayor[0]}, fila: {mayor[1] + 1}, columna: {mayor[2] + 1}")
    print(f"numero menor: {menor[0]}, fila: {menor[1] + 1}, columna: {menor[2] + 1}")

print("Lector de matriz")
lectorMatriz([[1,2],[3,4]])