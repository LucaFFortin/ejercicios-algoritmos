from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio,barrido

pila = Pila()
nodo = nodoPila()
nodo.info = 1
apilar(pila, nodo)
nodo = nodoPila()
nodo.info = 1
apilar(pila, nodo)
nodo = nodoPila()
nodo.info = 2
apilar(pila, nodo)
nodo = nodoPila()
nodo.info = 3
apilar(pila, nodo)

# remueve los objetos de la pila original
def ocurrencias_valor(pila, valor):
    copia_pila = pila
    cont_ocurrencias = 0
    while (not pila_vacia(copia_pila)):
        dato = desapilar(copia_pila)
        if (dato.info == valor):
            cont_ocurrencias += 1
    print(f"Ocurrencias del valor {valor} es de: {cont_ocurrencias}")

# ocurrencias_valor(pila, 1) // 2

def eliminar_impares(pila):
    paux = Pila()
    while (not pila_vacia(pila)):
        dato = desapilar(pila)
        if (dato.info % 2 == 0):
            apilar(paux, dato)
            
    print("Datos que quedaron en la pila")
    while (not pila_vacia(paux)):
        dato = desapilar(paux)
        print(dato.info)
        apilar(pila, dato)

# eliminar_impares(pila) # queda 2

def reemplazar_valor(pila, valor, nuevo_valor):
    paux = Pila()
    while (not pila_vacia(pila)):
        dato = desapilar(pila)
        if (dato.info == valor):
            dato.info = nuevo_valor
        apilar(paux, dato)
            
    print("Datos que quedaron en la pila")
    while (not pila_vacia(paux)):
        dato = desapilar(paux)
        print(dato.info)
        apilar(pila, dato)

# reemplazar_valor(pila, 1, 10) 
