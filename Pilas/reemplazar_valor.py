from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, barrido

def reemplazar_valor(pila, valor, nuevo_valor):
    paux = Pila()
    while (not pila_vacia(pila)):
        dato = desapilar(pila)
        if (dato == valor):
            dato = nuevo_valor
        apilar(paux, dato)
    
    while (not pila_vacia(paux)):
        dato = desapilar(paux)
        apilar(pila, dato)

    print("Datos que quedaron en la pila")
    barrido(pila)

def existe_valor(pila, valor):
    existe = False
    paux = Pila()
    while (not pila_vacia(pila)):
        dato = desapilar(pila)
        if (dato == valor):
            existe = True
        apilar(paux, dato)
    
    while (not pila_vacia(paux)):
        dato = desapilar(paux)
        apilar(pila, dato)

    return existe

# main
print("Ingrese los datos de la Pila:")
pila = Pila()
while(True):
    nodo = input("Ingrese el dato que quiere guardar en la pila: S para salir: ")
    if (nodo == "S"): break
    apilar(pila, nodo)

valor_a_cambiar = input("Ingrese el valor a cambiar: ")
if (existe_valor(pila, valor_a_cambiar)):

    valor_nuevo = input("Ingrese el nuevo valor: ")

    print("Pila antes de cambiar el valor: ")
    barrido(pila)

    reemplazar_valor(pila, valor_a_cambiar, valor_nuevo)
else:
    print("El valor ingresado no esta en la pila")