from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

def borrar_elemento(pila, posicion):
    pos = 0

    if (posicion > pila.tamanio): 
        print("posicion incorrecta, es mayor al tamaño de la pila")
        return
    
    if (posicion < 0): 
        print("posicion incorrecta, debe ser mayor a 0")
        return

    paux = Pila()
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        pos += 1
        if (not pos == posicion):
            apilar(paux, x)

    while(not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)

# main
print("Ingrese los datos de la Pila:")
pila = Pila()
while(True):
    nodo = input("Ingrese el dato que quiere guardar en la pila: S para salir: ")
    if (nodo == "S"): break
    apilar(pila, nodo)

entrada = int(input("Ingrese la posicion del numero a eliminar: "))

print("Antes de borrar el elemento: ")
barrido(pila)

borrar_elemento(pila, entrada)

print("Despues de borrar el elemento: ")
barrido(pila)


