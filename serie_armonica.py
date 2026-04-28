def serie_armonica(n):
    contador = 1
    acumulador = 0
    while (contador <= n):
        acumulador += 1/contador
        contador += 1
    return acumulador

print("serie armonica")
print("la serie con 1 pasos da", serie_armonica(1))
print("la serie con 10 pasos da", serie_armonica(10))
print("la serie con 20 pasos da", serie_armonica(20))
print("la serie con 100 pasos da", serie_armonica(100))