"""
Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from validaciones import validar_caracter
from utils import limpiar
from tda_listas import insertar, lista_vacia, eliminar, barrido, tamanio, buscar, criterio, buscar_criterio, insertar_criterio, eliminar_criterio, Lista, nodoLista

# limpiamos todos los comandos anteriores
limpiar()

# ingreso de datos
lista = Lista()

while (True):
    opcion = input("Desea ingresar un caracter a la lista?, Si para ingresar, No para salir: ").lower()

    if (opcion == "no"): 
        limpiar()
        break
    elif (opcion == "si"):
        dato = validar_caracter("Ingrese el caracter que quiere guardar: ")
        insertar(lista, dato)        
        limpiar()
    else:    
        limpiar()
        print("La opcion ingresada no esta dentro de las opciones listadas.")

# separacion de caracteres
lista_no_vocales = Lista()

aux = lista.inicio
while (aux is not None):
    if (aux.info.lower() not in ["a", "e", "i", "o", "u"]):
        insertar(lista_no_vocales, aux.info)
    aux = aux.sig

if (lista_vacia(lista)):
    print("No se ingresaron datos, por lo tanto no hay listas que mostrar.")
else:
    print("Lista Original: ")
    barrido(lista)

    print("Lista sin caracteres: ")
    barrido(lista_no_vocales)