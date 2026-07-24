"""
Dada una lista de números enteros eliminar de estas los números primos
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from validaciones import validar_numero
from utils import limpiar, es_primo
from tda_listas import insertar, lista_vacia, eliminar, barrido, tamanio, buscar, criterio, buscar_criterio, insertar_criterio, eliminar_criterio, Lista, nodoLista

# limpiamos todos los comandos anteriores
limpiar()

# ingreso de datos
lista = Lista()

while (True):
    opcion = input("Desea ingresar un numero a la lista?, Si para ingresar, No para salir: ").lower()

    if (opcion == "no"): 
        limpiar()
        break
    elif (opcion == "si"):
        numero = validar_numero("Ingrese el numero que quiere guardar: ")
        insertar(lista, numero)        
        limpiar()
    else:    
        limpiar()
        print("La opcion ingresada no esta dentro de las opciones listadas.")


# separacion de listas
lista_no_primos = Lista()

aux = lista.inicio
while (aux is not None):
    if (not es_primo(aux.info)):
        insertar(lista_no_primos, aux.info)
    aux = aux.sig

if (lista_vacia(lista)):
    print("No se ingresaron datos, por lo tanto no hay listas que mostrar.")
else:
    print("Lista Original: ")
    barrido(lista)

    print("Lista sin numeros primos: ")
    barrido(lista_no_primos)