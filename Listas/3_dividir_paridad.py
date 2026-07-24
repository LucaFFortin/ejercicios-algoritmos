"""
Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos, 
una que contenga los números pares y otra para los números impares.
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

# separacion de numeros
pares = Lista()
impares = Lista()

aux = lista.inicio
while (aux is not None):
    numero = aux.info
    if (numero % 2 != 0):
        insertar(impares, numero)
    else:
        insertar(pares, numero)
    aux = aux.sig

# imprimimos los datos de salida segun el caso
if (lista_vacia(lista)):
    print("No se ingresaron datos, por lo tanto no hay listas que mostrar.")
else:
    print("Lista de numeros pares: ")
    barrido(pares)

    print("Lista de numeros impares: ")
    barrido(impares)
