"""
Eliminar el i-ésimo elemento después del frente de la cola
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from validaciones import validar_numero
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio

cola = Cola()
cola_aux = Cola()

# se pide un dato cualquiera y se ingresa en una cola
elemento = input("Ingrese un dato a guardar en la pila o precione enter sin ingresar nada para salir: ")
while (elemento != ""):
    arribo(cola, elemento)
    elemento = input("Ingrese un dato a guardar en la pila o presione enter sin ingresar nada para salir: ")

# se pide el indice del dato a eliminar en la cola
filtro = validar_numero("Ingrese el indice del dato a eliminar (formato numero): ")
tamanio_cola = tamanio(cola)

# si el indice ingresado esta fuera de los limites de la cola, evitamos la ejecucion
if (filtro > tamanio_cola or filtro < 0): 
    print("El indice ingresado esta fuera del rango de la cola, ejecucion abortada.")
else:
    # se imprime la cola antes de eliminar el elemento
    print("Antes de eliminar el elemento: ")
    barrido(cola)

    for i in range(0, tamanio_cola):
        dato = en_frente(cola)
        if (i != filtro):
            arribo(cola_aux, dato)
        mover_al_final(cola)

    # se imprime la cola despues de eliminar el elemento
    print("Despues de eliminar el elemento: ")
    barrido(cola_aux)