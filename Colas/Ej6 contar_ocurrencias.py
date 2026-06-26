"""
Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ningu
na estructura auxiliar
"""
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio

cola = Cola()

elemento = input("Ingrese un dato a guardar en la pila o precione enter sin ingresar nada para salir: ")
while (elemento != ""):
    arribo(cola, elemento)
    elemento = input("Ingrese un dato a guardar en la pila o presione enter sin ingresar nada para salir: ")

filtro = input("Ingrese el dato a contabilizar en la cola: ")
cont = 0
for i in range(0, tamanio(cola)):
    dato = en_frente(cola)
    if (dato == filtro): cont += 1
    mover_al_final(cola)

print(f"La cantidad de apariciones del dato '{filtro}' en la cola es de: {cont} veces.")