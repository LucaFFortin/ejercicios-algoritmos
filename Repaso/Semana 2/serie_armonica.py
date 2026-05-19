def serie_armonica(n):
    contador = 1
    acumulador = 0
    while (contador <= n):
        acumulador += 1/contador
        contador += 1
    return acumulador

# main
entrada = int(input("Ingrese el numero para la serie armonica: "))
print(serie_armonica(entrada))