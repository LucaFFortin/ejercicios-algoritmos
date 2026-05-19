def es_simetrica(matriz):
    es_simetrica = True
    for i, valorI in enumerate(matriz):
        for j, valorJ in enumerate(valorI):
            if (matriz[i][j] != matriz[j][i]):
                es_simetrica = False
                
    if (es_simetrica):
        print("La matriz ingresada es simetrica")
    else:
        print("La matriz ingresada no es simetrica")

print("Matriz simetrica")
es_simetrica([[1,2,3],[2,1,2],[3,2,1]])
es_simetrica([[1,2,3],[2,1,2],[3,50,1]])
es_simetrica([[1,1,1],[1,1,1],[1,1,1]])