"""
Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, 
de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, 
resolver las siguientes actividades:
a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra 'Python', si perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.
"""
import sys
from pathlib import Path
from datetime import datetime, time

sys.path.append(str(Path(__file__).resolve().parent.parent))

from validaciones import validar_numero, validar_string
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio

"""
notificacion: {
    recieved: {time object time(hh, mm)},
    app: string,
    message: string,
}
"""

def ingresar_notificacion(notificaciones):
    app = validar_string("Ingrese la aplicacion de donde proviene el mensaje: ")
    mensaje = validar_string("Ingrese el mensaje de la notificacion: ")

    hour = datetime.now().hour
    minutes = datetime.now().minute

    notificacion = {
        "recieved": time(hour, minutes),
        "app": app,
        "message": mensaje,
    }

    arribo(notificaciones, notificacion)
    barrido(notificaciones)

def eliminar_facebook(notificaciones):
    temp = Cola()
    while (not cola_vacia(notificaciones)):
        notificacion = atencion(notificaciones)
        if (notificacion["app"] != "facebook"):
            arribo(temp, notificacion)
    
    while (not cola_vacia(temp)):
        notificacion = atencion(temp)
        arribo(notificaciones, notificacion)


def imprimir_twitter(notificaciones):
    for i in range(tamanio(notificaciones)):
        notificacion = en_frente(notificaciones)
        if (notificacion["app"] == "twitter" and notificacion["message"].lower().find("python") != -1):
            print(f"Notificacion de Twitter a la hora: {notificacion["recieved"]}, con el mensaje: \"{notificacion["message"]}\".")
        mover_al_final(notificaciones)

def guardar_temporales(notificaciones):
    temp = Cola()
    for i in range(tamanio(notificaciones)):
        notificacion = en_frente(notificaciones)
        hora_recivido = notificacion.recieved
        if (hora_recivido >= time(11, 43) and hora_recivido <= time(15, 57)):
            arribo(temp, notificacion)
        mover_al_final(notificaciones)
    print(f"La cantidad de notificaciones recividas entre las 11:43 y las 15:57 son: {tamanio(temp)}")

notificaciones = Cola()
while (True):

    opcion = validar_numero("""Que operacion desea realizar: 
1 = ingresar una notificacion, 
2 = borrar notificaciones de Facebook, 
3 = imprimir notificaciones de twitter con el texto 'Python', 
4 = guardar mensajes recividos entre las 11:43 y las 15:57, 
0 = SALIR: """)

    if (opcion == 0): break
    elif (opcion == 1): ingresar_notificacion(notificaciones)
    elif (opcion == 2): eliminar_facebook(notificaciones)
    elif (opcion == 3): imprimir_twitter(notificaciones)
    elif (opcion == 4): guardar_temporales(notificaciones)
    else: print("Opcion no reconocida por el sistema.")