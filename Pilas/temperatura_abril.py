"""
Dada una pila con los valores promedio de temperatura ambiente de cada día del mes de abril, 
obtener la siguiente información sin perder los datos:
a. determinar el rango de temperatura del mes, temperatura mínima y máxima;
b. calcular el promedio de temperatura (o media) del total de valores;
c. 
determinar la cantidad de valores por encima y por debajo de la media.
"""
from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

mayores = Pila()
menores = Pila()
dias_registrados = Pila()


def insertar_temperatura(pila, temperatura, dia):
    try:
        temperatura = float(temperatura)
    except:
        print("Ingrese un numero valido como temperatura.")
        return
    
    try:
        dia = int(dia)
    except:
        print("El valor de dia tiene que ser un numero entero entre 1 y 31.")
        return
    
    dia_existe = False
    paux = Pila()
    while (not pila_vacia(dias_registrados)):
        dia_pila = desapilar(dias_registrados)
        if (dia_pila == dia): dia_existe = True
        apilar(paux, dia_pila)

    while(not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(dias_registrados, x)

    if (dia_existe):
        print("El dia ingresado ya fue registrado, ingrese otro dia.")
    else:
        apilar(dias_registrados, dia)
        apilar(pila, [temperatura, dia])

def determinar_valores(pila):
    primero = True
    max = 0
    min = 0

    cont = 0
    acc = 0

    if (pila_vacia(pila)):
        print("No hay datos para hacer el calculo")
        return

    paux = Pila()
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        temperatura, dia = x
        cont += 1
        acc += temperatura
        if (primero):
            primero = False
            max = temperatura
            min = temperatura
        else:
            if (temperatura > max): max = temperatura
            elif (temperatura < min): min = temperatura
        apilar(paux, x)

    while (not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)

    return [min, max, cont, acc]

def determinar_variaciones(pila):
    if (pila_vacia(pila)):
        print("No hay datos para calcular los dias superiores e inferiores a la media.")
        return

    paux = Pila()
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        temperatura, dia = x
        if (temperatura > media): apilar(mayores, [temperatura, dia])
        elif (temperatura < media): apilar(menores, [temperatura, dia])
        apilar(paux, x)

    if (tamanio(mayores) == 0):
        print("No hubieron dias mayores a la media")
    elif (tamanio(mayores) == 1):
        print(f"La cantidad de dias que estuvieron por encima de la media es de: {tamanio(mayores)} dia.")
    else:
        print(f"La cantidad de dias que estuvieron por encima de la media es de: {tamanio(mayores)} dias.")

    if (tamanio(menores) == 0):
        print("No hubieron dias menores a la media")
    elif (tamanio(menores) == 1):
        print(f"La cantidad de dias que estuvieron por debajo de la media es de: {tamanio(menores)} dia.")
    else:
        print(f"La cantidad de dias que estuvieron por debajo de la media es de: {tamanio(menores)} dias.")
    
    while (not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)

# main
pila = Pila()
while(True):
    dia = input("Ingrese el numero del dia de abril (1 a 31): ")
    temperatura = input("Ingrese la temperatura en forma numerica de ese dia: ") 
    insertar_temperatura(pila, temperatura, dia)
    otro = input("Desea ingresar mas registros de temperatura, 1 para si, 0 para no: ")
    if (otro == "0"): break

min, max, cont, acc = 0,0,0,0

if (not pila_vacia(pila)):
    [min, max, cont, acc] = determinar_valores(pila)

media = 0
if (cont != 0):
    media = acc / cont

rango = max - min

print(f"El rango de temperaturas es: {rango}°.")
print(f"La temperatura mas alta fue de: {max}°.")
print(f"La temperatura mas baja fue de: {min}°.")
print(f"La temperatura media fue de: {media}°.")
determinar_variaciones(pila)