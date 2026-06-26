from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

direcciones = ["norte", "sur", "este", "oeste", "noreste", "suroeste", "noroeste", "sureste" ]

def registrar_movimiento(pila, pasos, direccion):
    try:
        pasos = int(pasos)
    except:
        print("Ingrese un numero valido para los pasos del robot.")
        return
    
    if (direccion not in direcciones):
        print("La direccion es incorrecta, solo puede ser: norte, sur, este, oeste, noreste, noroeste, sureste suroeste")
        return
    
    if (pasos <= 0):
        print("Debe ingresar 1 paso o mas, valores como 0 o negativos son incorrectos.")
        return
    
    apilar(pila, [pasos, direccion])

def movimientos_contrarios(pila):
    paux = Pila()
    paux_contraria = Pila()
    
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        pasos, direccion = x
        direccion_contraria = ""
        apilar(paux, x)
        for i, v in enumerate(direcciones):
            if (direccion == v):
                if (i % 2 == 0):
                    direccion_contraria = direcciones[i + 1]
                else:
                    direccion_contraria = direcciones[i - 1]      
        apilar(paux_contraria, [pasos, direccion_contraria])
    
    while (not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)

    return paux_contraria

# main
pila = Pila()
pila_contraria = Pila()
while(True):
    pasos = input("Ingrese la cantidad de pasos: ")
    direccion = input("Ingrese la direccion: ")
    registrar_movimiento(pila, pasos, direccion)
    otro = input("Desea ingresar otro movimiento, 1 para si, 0 para no: ")
    if (otro == "0"): break

if (not pila_vacia(pila)):
    pila_contraria = movimientos_contrarios(pila)
else:
    print("La pila esta vacia, por lo tanto no se puede calcular pasos contrarios.")

print("Movimientos que realizo el robot: ")
barrido(pila)
print("Movimientos contrarios que lo dejarian en su posicion original: ")
barrido(pila_contraria)
