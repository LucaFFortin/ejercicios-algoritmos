from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

# 13
"""
asumiendo que los nodos guardan la informacion de la siguiente manera
Nodo: {
    modelo: string,
    peliculas: array,
    estado: [dañado, impecable, destruido]
}
"""
# a
def hulkbuster_utilizado(pila):
    paux = Pila()
    usado = False
    while (not pila_vacia(pila)):
        modelo, peliculas, estado = desapilar(pila)

        if (modelo == "Mark XLIV"):
            usado = peliculas
        apilar(paux, x)

    while (not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)
    
    if (not usado): return "no fue utilizado"
    print("Fue utilizado en las siguientes peliculas: ")
    for pelicula in usado:
        print(pelicula)

# b
def modelos_dañados(pila):
    paux = Pila()
    dañados = []
    while (not pila_vacia(pila)):
        modelo , _, estado = desapilar(pila)
        if (estado == "dañado"):
            dañados.append(modelo)
        apilar(paux, x)

    while (not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)
    
    if (len(dañados) == 0): return "No hay modelos dañados"
    print("Estos son los modelos dañados: ")
    for modelo in dañados:
        print(modelo)

# c
def eliminar_modelos_dañados(pila):
    paux = Pila()
    while (not pila_vacia(pila)):
        modelo , _, estado = desapilar(pila)
        if (not estado == "dañado"):
            apilar(paux, x)
        print(f"Modelo destuido: {modelo}")

    while (not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x) 

# 14
def ingresar_ordenado(pila, numero):
    paux = Pila()
    while (not pila_vacia(pila)):
        num = desapilar(pila)
        if (num < numero):
            nodo = nodoPila()
            nodo.info = numero
            apilar(paux, nodo)
        apilar(paux, num)

    while (not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)

