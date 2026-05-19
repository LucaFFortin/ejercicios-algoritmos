def factorial(num):
    cont = 1
    for i in range(1, num+1):
        cont *= i

    print(cont)

# main
entrada = int(input("Ingrese el numero para a factorizar: "))
factorial(entrada)