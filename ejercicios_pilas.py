from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio,barrido
import random

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

# 1 
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

# 2
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

# 3 
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

# 4
# O(2n)
def invertir_pila(pila):
    lista = []
    while (not pila_vacia(pila)):
        elem = desapilar(pila)
        lista.append(elem)
    
    while (len(lista) > 0):
        elem = lista.pop(0)
        apilar(pila, elem)

    barrido(pila)

# print("antes")
# barrido(pila)
# print("invertido")
# invertir_pila(pila)

# 5
def lista_a_pila(lista, pila):
    for i in lista:
        nodo = nodoPila()
        nodo.info = i
        apilar(pila, nodo)

def es_palindromo(cadena):
    pila = Pila()
    pila2 = Pila()
    cadena = list(cadena)
    lista_a_pila(cadena, pila2)
    
    cadena.reverse()
    lista_a_pila(cadena, pila)

    palindromo = True
    while (not pila_vacia(pila) and not pila_vacia(pila2)):
        elem1 = desapilar(pila)
        elem2 = desapilar(pila2)
        
        if (not elem1.info == elem2.info): palindromo = False
    
    return palindromo
        
# print(es_palindromo("hola"))
# print(es_palindromo("oso"))
# print(es_palindromo("neuquen"))

# 6
def ver_palabra_inversa(cadena):
    lista = list(cadena)
    pila = Pila()
    lista_a_pila(lista, pila)
    lista = []
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        lista.append(x.info)
    print("".join(lista))
    
# ver_palabra_inversa("hola")

# 7
def borrar_elemento(pila, posicion):
    pos = 0
    paux = Pila()
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        pos += 1
        if (not pos == posicion):
            apilar(paux, x)

    while(not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)

# 8
cartas = Pila()
def agregar_carta(pila):
    numero = random.randrange(1, 11)
    palo = random.choice(["basto", "oro", "copa", "espada"])
    nodo = nodoPila()
    nodo.info = [numero, palo]
    apilar(pila, nodo)

def separar_palos(pila):
    p_copa = Pila()
    p_basto = Pila()
    p_oro = Pila()
    p_espada = Pila()

    while (not pila_vacia(pila)):
        carta = desapilar(pila)
        if (carta.info[1] == "basto"):
            apilar(p_basto, carta)
        if (carta.info[1] == "oro"):
            apilar(p_oro, carta)
        if (carta.info[1] == "copa"):
            apilar(p_copa, carta)
        if (carta.info[1] == "espada"):
            apilar(p_espada, carta)

    return [p_espada, p_basto, p_copa, p_oro]

def ordenar_palo(cartas):
    lista = []
    while (not pila_vacia(cartas)):
        x = desapilar(cartas)
        lista.append(x.info)
    lista.sort()
    while(len(lista) > 0):
        x = lista.pop()
        nodo = nodoPila()
        nodo.info = x
        apilar(cartas, nodo)

# 9
def factorial_pila(num):
    paux = Pila()
    for i in range(1, num + 1):
        nodo = nodoPila()
        nodo.info = i
        apilar(paux, nodo)

    acc = 1
    while (not pila_vacia(paux)):
        x = desapilar(paux)
        acc *= x.info

    return acc

# print(factorial_pila(4))
# print(factorial_pila(3))

# 10
def insertar_atenea(pila, pos):
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

# 11 
# se puede usar la funcion "en_cima" e iterar este, sin modificar la pila
def contar_vocales(pila):
    cont = 0
    paux = Pila()
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        if (x.info in ["a", "e", "i", "o", "u"]):
            cont += 1
        apilar(paux, x)

    while (not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)

    return cont

# 12
def encontrar_personajes(pila):
    paux = Pila()
    encontrado = False
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        if (x.info in ["Leia Organa", "Boba Fett"]):
            encontrado = True
        apilar(paux, x)

    while (not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)
    
    return encontrado

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

