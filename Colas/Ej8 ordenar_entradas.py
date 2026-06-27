"""
Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, utilizando 
solo una cola como estructura auxiliar
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
from validaciones import validar_string, validar_numero
import re

cola = Cola()
# recibe un string, lo divide en partes numericas y de texto con una expresion regular
# retorna una lista donde el elemento esta desestructurado
def transformar_string(s):
    partes = re.split(r'(\d+)', s)
    return [int(p) if p.isdigit() else p.lower() for p in partes]

def es_mayor(actual, a_ingresar):
    return transformar_string(actual) > transformar_string(a_ingresar)


def ingresar_ordenado(cola, elemento_ingresar):
    caux = Cola()    
    ingresado = False
    if (cola_vacia(cola)):
        print("Entro:", elemento_ingresar)
        arribo(cola, elemento_ingresar)
    else:        
        while (not cola_vacia(cola)):
            elemento_cola = atencion(cola)
            print("Entro bucle:", elemento_cola)
            if (es_mayor(elemento_cola, elemento_ingresar) and not ingresado):
                arribo(caux, elemento_ingresar)
                arribo(caux, elemento_cola)
                ingresado = True
            else:
                arribo(caux, elemento_cola)
        
        # caso final donde no fue ingresado en el bucle y lo ingresamos manualmente
        if (not ingresado):
            arribo(caux, elemento_ingresar)
            ingresado = True

        while(not cola_vacia(caux)):
            elemento = atencion(caux)
            arribo(cola, elemento)

    print("COLA: ")
    barrido(cola)

while (True):
    numero = input("Ingrese un elemento para la cola: ")
    ingresar_ordenado(cola, numero)
    opcion = validar_string("Ingrese 'si' para ingresar otro numero, 'no' para salir: ")
    while (opcion.lower() not in ["si", "no"]):
        opcion = validar_string("solo puede ingresar los valores: 'si' para ingresar otro numero, 'no' para salir: ")
    if (opcion == "no"): break