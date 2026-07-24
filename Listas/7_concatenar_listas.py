"""
Implementar los algoritmos necesarios para resolver las siguientes tareas:
a. concatenar dos listas, una atrás de la otra;
b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from validaciones import validar_numero
from utils import limpiar
from tda_listas import insertar, lista_vacia, eliminar, barrido, tamanio, buscar, criterio, buscar_criterio, insertar_criterio, eliminar_criterio, Lista, nodoLista

# limpiamos todos los comandos anteriores
limpiar()

# ingreso de datos
lista = Lista()
lista_secundaria = Lista()

while (True):
    opcion = input("Desea ingresar un dato a la primera lista?, Si para ingresar, No para salir: ").lower()

    if (opcion == "no"): 
        limpiar()
        break
    elif (opcion == "si"):
        numero = input("Ingrese el numero que quiere guardar: ")
        insertar(lista, numero)        
        limpiar()
    else:    
        limpiar()
        print("La opcion ingresada no esta dentro de las opciones listadas.")

while (True):
    opcion = input("Desea ingresar un dato a la segunda lista?, Si para ingresar, No para salir: ").lower()

    if (opcion == "no"): 
        limpiar()
        break
    elif (opcion == "si"):
        numero = input("Ingrese el numero que quiere guardar: ")
        insertar(lista_secundaria, numero)        
        limpiar()
    else:    
        limpiar()
        print("La opcion ingresada no esta dentro de las opciones listadas.")

# caso si ambas listas estan vacias, imprimimos un mensaje por pantalla
if (lista_vacia(lista) and lista_vacia(lista_secundaria)): print("Ambas listas estan vacias, se cancela la ejecucion del programa.")

# funcion para insertar un elemento detras de otro
# la misma que insertar pero sin la logica donde se evalua el dato a ingresar
def insertar_seguido(lista, dato):
    """Insertar el dato ingresado en la lista de manera secuencial."""
    nodo = nodoLista()
    nodo.info = dato
    if (lista.inicio is None):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while (act is not None):
            ant = ant.sig
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamanio += 1

# funcion para concatenar las 2 listas de manera secuencial
def concatenar_secuencial(list1, list2, newList):
    aux = list1.inicio
    while (aux is not None):
        insertar(newList, aux.info)
        aux = aux.sig

    aux = list2.inicio
    while (aux is not None):
        insertar(newList, aux.info)
        aux = aux.sig

# concatena las 2 listas en 1 sola obviando los elementos repetidos
# al encontrar un elemento repetido evita ingresarlo a la lista final y aumenta un contador en 1
# devuelve un contador con la cantidad de elementos repetidos
def concatenar_set(list1, list2, newList):
    contador_repetidos = 0

    aux = list1.inicio
    while (aux is not None):
        if (buscar(newList, aux.info) is None):
            insertar(newList, aux.info)
        else:
            contador_repetidos += 1
        aux = aux.sig

    aux = list2.inicio
    while (aux is not None):
        if (buscar(newList, aux.info) is None):
            insertar(newList, aux.info)
        else:
            contador_repetidos += 1
        aux = aux.sig

    return contador_repetidos

def eliminar_contenido(lista):
    while (lista.inicio is not None):
        print(f"El elemento '{lista.inicio.info}' fue eliminado.")
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1

# concatenacion secuencial
print("Concatenacion de las listas de manera secuencial.")
nueva_lista = Lista()
concatenar_secuencial(lista, lista_secundaria, nueva_lista)
barrido(nueva_lista)

# concatenacion como set
print("Concatenacion de las listas de sin repetir datos.")
nueva_lista = Lista()
repetidos = concatenar_set(lista, lista_secundaria, nueva_lista)
barrido(nueva_lista)

# cantidad de elementos repetidos
print(f"La cantidad de elementos repetidos es de {repetidos} elementos repetidos.")

# eliminar contenido de una lista
print(f"El tamaño de las listas antes de eliminar su contenido son de: lista 1: {tamanio(lista)} elementos, Lista 2: {tamanio(lista_secundaria)} elementos y Lista final: {tamanio(nueva_lista)} elementos.")

eliminar_contenido(lista)
eliminar_contenido(lista_secundaria)
eliminar_contenido(nueva_lista)

print(f"El tamaño de las listas despues de eliminar su contenido son de: lista 1: {tamanio(lista)} elementos, Lista 2: {tamanio(lista_secundaria)} elementos y Lista final: {tamanio(nueva_lista)} elementos.")
