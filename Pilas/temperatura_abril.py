"""
Dada una pila con los valores promedio de temperatura ambiente de cada día del mes de abril, 
obtener la siguiente información sin perder los datos:
a. determinar el rango de temperatura del mes, temperatura mínima y máxima;
b. calcular el promedio de temperatura (o media) del total de valores;
c. 
determinar la cantidad de valores por encima y por debajo de la media.
"""
from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

mayores = []
menores = []

def insertar_temperatura(pila, temperatura, dia):
    primero = True
    try:
        temperatura = float(temperatura)
    except:
        print("Ingrese un numero valido como temperatura.")

    if (primero):
        primero = False
        max = temperatura
        min = temperatura
    else:
        if (temperatura > max): max = temperatura
        elif (temperatura < min): min = temperatura
    
    cont += 1
    acc += temperatura

    apilar(pila, [temperatura, dia])

def determinar_valores():
    primero = True
    max = 0
    min = 0

    cont = 0
    acc = 0

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
    paux = Pila()
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        temperatura, dia = x
        if (temperatura > media): mayores.append([temperatura, dia])
        elif (temperatura < media): menores.append([temperatura, dia])
        apilar(paux, x)

    print(f"La cantidad de dias que estuvieron por encima de la media es de: {len(mayores)} dias.")
    print(f"La cantidad de dias que estuvieron por debajo de la media es de: {len(menores)} dias.")

    while (not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)

# main
pila = Pila()
while(True):
    dia = input("Ingrese el numero del dia de abril: ")
    temperatura = input("Ingrese la temperatura de ese dia: ")
    insertar_temperatura(pila, temperatura, dia)
    otro = input("Desea ingresar mas registros de temperatura, 1 para si, 0 para no: ")
    if (otro == "0"): break

[min, max, cont, acc] = determinar_valores()

media = acc / cont
rango = max - min

print(f"El rango de temperaturas es: {rango}°.")
print(f"La temperatura mas alta fue de: {max}°.")
print(f"La temperatura mas baja fue de: {min}°.")
print(f"La temperatura media fue de: {media}°.")
determinar_variaciones(pila)