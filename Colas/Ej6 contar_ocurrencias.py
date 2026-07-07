"""
Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ningu
na estructura auxiliar
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from validaciones import validar_string
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio

cola = Cola()

# se pide un dato cualquiera y se ingresa en una cola
elemento = input("Ingrese un dato a guardar en la pila o precione enter sin ingresar nada para salir: ")
while (elemento != ""):
    arribo(cola, elemento)
    elemento = input("Ingrese un dato a guardar en la pila o presione enter sin ingresar nada para salir: ")

# se pide el dato a filtrar en la cola
filtro = input("Ingrese el dato a contabilizar en la cola: ")
# contamos las ocurrencias de ese dato
cont = 0
for i in range(0, tamanio(cola)):
    dato = en_frente(cola)
    if (dato == filtro): cont += 1
    mover_al_final(cola)

# imprimimos las ocurrencias del dato
print(f"La cantidad de apariciones del dato '{filtro}' en la cola es de: {cont} veces.")

# si desea ver la entrada y salida, lo imprimimos por pantalla
opcion = validar_string("Desea ver las colas de entrada y salida? SI = ver, NO = no ver: ")
if (opcion.lower() == "si"):
    print("cola de datos ingresados: ")
    barrido(cola)
    print(f"Ocurrencias de valor {filtro}: {cont}.")