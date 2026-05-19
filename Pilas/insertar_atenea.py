from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

def insertar_atenea(pila, pos):
    if (pos > pila.tamanio): 
        print("posicion incorrecta, es mayor al tamaño de la pila")
        return
    
    if (pos < 0): 
        print("posicion incorrecta, debe ser mayor a 0")
        return
    
    posicion = 0
    paux = Pila()
    while (not pila_vacia(pila)):
        posicion += 1
        if (pos == posicion):
            nodo = nodoPila()
            nodo.info = "Atenea"
            apilar(paux, nodo)
        x = desapilar(pila)
        apilar(paux, x)

    while (not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)

# main
print("Ingrese los datos de la Pila:")
pila = Pila()
while(True):
    nodo = nodoPila()
    nodo.info = input("Ingrese el dato que quiere guardar en la pila: S para salir: ")
    if (nodo.info == "S"): break
    apilar(pila, nodo)

entrada = int(input("Ingrese la posicion a insertar a Atenea: "))
print("Pila sin atenea")
barrido(pila)

insertar_atenea(pila, entrada)

print("Pila con Atenea")
barrido(pila)