from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

def insertar_ascendente(pila, dato):
    paux = Pila()

    if (pila_vacia(pila)): 
        apilar(pila, dato)
        return
    
    ingresado = False
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        # si se cambia de orientacion el signo de mayor que, la pila pasa a ser descendente
        if (dato < x and not ingresado):
            ingresado = True
            apilar(paux, dato)
        apilar(paux, x)

    if (pila.tamanio == 0 and not ingresado): apilar(paux, dato)

    while(not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)

"""
al insertar un dato, revisamos todos los elementos y lo insertamos cuando encontremos que el elemento actual es menor al dato
"""
pila = Pila()

# main
while (True):
    opcion = input("Ingrese un numero o S para salir: ").lower()
    if (opcion == "s"):
        break
    opcion = int(opcion)
    insertar_ascendente(pila, opcion)

barrido(pila)