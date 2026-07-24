"""
Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.
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

while (True):
    opcion = input("Desea ingresar un dato a la lista?, Si para ingresar, No para salir: ").lower()

    if (opcion == "no"): 
        limpiar()
        break
    elif (opcion == "si"):
        numero = input("Ingrese el dato que quiere guardar: ")
        insertar(lista, numero)        
        limpiar()
    else:    
        limpiar()
        print("La opcion ingresada no esta dentro de las opciones listadas.")

print("Antes")
barrido(lista)

# Logica de insercion de elementos
posicion = validar_numero("Ingrese el indice donde desea ingresar el dato: ")

# validamos que la posicion ingresada este dentro del rango de la lista
while (posicion < 0 or posicion > tamanio(lista)):
    # limpiamos los comandos anteriores
    limpiar()

    print(f"La posicion ingresada esta fuera del rango aceptado, ingrese otra que este dentro del rango (de 0 a {tamanio(lista)}).")
    posicion = validar_numero("Ingrese el indice donde desea ingresar el dato: ")

dato_ingresar = input("Ingrese el dato a ingresar: ")

# realizamos la insercion del elemento
aux = lista.inicio
indice = 0
while (aux is not None):
    numero = aux.info

    # si se desea ingresar un dato en la primera posicion se ejecuta esta logica
    # se guarda el elemento en la primera posicion, se actualiza el puntero del inicio de la lista para que apunte al nuevo nodo
    # y por ultimo el nodo nuevo apunta al nodo que anteriormente era el inicio de la lista 
    if (posicion == 0 and indice == 0):
        act = lista.inicio

        nodo = nodoLista()
        nodo.info = dato_ingresar

        lista.inicio = nodo
        nodo.sig = act
        
    indice += 1

    # si se ingresa en otro indice que no sea el primer indice, 
    # se guarda el elemento actual como "nodo actual" y el siguiente como "nodo siguiente"
    # hacemos que el siguiente elemento del "nodo actual" sea el nuevo nodo y que este apunte al "nodo siguiente"
    if (indice == posicion):
        act = aux
        sig = aux.sig

        nodo = nodoLista()
        nodo.info = dato_ingresar

        act.sig = nodo
        nodo.sig = sig

    aux = aux.sig


print("Despues")
barrido(lista)