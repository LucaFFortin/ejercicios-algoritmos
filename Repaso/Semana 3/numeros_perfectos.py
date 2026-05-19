def numeros_perfecto():
    suficiente = False
    numeros_perfectos = []
    num = 1
    while not suficiente:
        if len(numeros_perfectos) == 3:
            suficiente = True
            break;

        cont = 0
        for i in range(1, int(num/2) + 1):
            if num % i == 0:
                cont += i

        if num == cont:
            numeros_perfectos.append(num)
        num += 1

    for numero in numeros_perfectos:
        print(numero)

numeros_perfecto() # 6, 28 y 496