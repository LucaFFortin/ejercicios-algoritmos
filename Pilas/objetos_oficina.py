""" 
Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso (por ejem
plo monitor 1 kg, teclado 0.25 kg, silla 7 kg, etc.), ordenar dicha pila de acuerdo a su peso –del 
objeto más liviano al más pesado-. Solo pueden utilizar pilas auxiliares como estructuras ex
tras, no se pueden utilizar métodos de ordenamiento.
"""

from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

def insertar_objeto_ordenado(pila, nombre_objeto, peso_objeto):
    try:
        peso_objeto = float(peso_objeto)
    except:
        print("El peso del objeto debe ser un numero valido.")
        return
    
    if (peso_objeto <= 0):
        print("El peso del objeto debe ser mayor a 0.")
        return

    paux = Pila()

    if (pila_vacia(pila)): 
        apilar(pila, [nombre_objeto, peso_objeto]) 
        return
    
    ingresado = False
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        nombre, peso = x
        # si se cambia de orientacion el signo de mayor que, la pila pasa a ser descendente
        if (peso > peso_objeto and not ingresado):
            ingresado = True
            apilar(paux, [nombre_objeto, peso_objeto])
        apilar(paux, [nombre, peso])

    if (not ingresado): apilar(paux, [nombre_objeto, peso_objeto])

    while(not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)

"""
al insertar un dato, revisamos todos los elementos y lo insertamos cuando encontremos que el elemento actual es menor al dato
"""
pila = Pila()

# main
while (True):
    nombre = input("Ingrese el nombre del objeto: ")
    peso = input("Ingrese el peso del objeto: ")
    insertar_objeto_ordenado(pila, nombre, peso)
    opcion = input("Desea ingresar otro objeto: 1 para si, o 0 para no: ").lower()
    if (opcion == "0"): break

barrido(pila)