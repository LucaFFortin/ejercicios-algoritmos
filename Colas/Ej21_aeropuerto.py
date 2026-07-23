"""
21. Desarrollar un algoritmo que permita administrar los despegues y aterrizajes de un aeropuerto 
que tiene una pista, contemplando las siguientes actividades:

a. de cada vuelo se conoce el nombre de la empresa, hora salida, hora llegada, aeropuerto de 
origen, aeropuerto de destino y su tipo (pasajeros, negocios o carga).

b. utilizar una cola para administrar los despegues, se deben cargan ordenados por horario de 
salida. Otra para los aterrizajes, se deben agregan a medida que arriban al aeropuerto.

c. en la pista solo puede haber un avión realizando una maniobra de aterrizaje o despegue.

d. se debe permitir agregar vuelos tanto de aterrizaje como de despegue en ambas colas después de realizar una atención.

e. se debe atender siempre que se pueda a los elementos de la cola de aterrizaje -dado que son 
aviones que están sobrevolando en la zona de espera-, salvo que sea el horario de salida del 
primer avión de la cola de despegue, en ese caso se deberá atender dicho despegue.

f. cada tipo de avión tiene su tiempo de uso de la pista para la maniobra de despegue y aterrizaje 
-adaptados a segundo para los fines prácticos del ejercicio-:
I. pasajeros (aterrizaje = 10 segundos, despegue = 5 segundos);
II. negocios (aterrizaje = 5 segundos, despegue = 3 segundos);
III. carga (aterrizaje = 12 segundos, despegue = 9 segundos).

g. se debe poder cancelar vuelos de despegue y poder reprogramar un vuelo para más tarde 
cuando se lo atiende para despegar (en esta caso el horario de salida será mayor que el 
último de la cola)
"""
import sys
from pathlib import Path
import time
import os
from datetime import datetime

sys.path.append(str(Path(__file__).resolve().parent.parent))

from tda_colas import Cola, arribo, atencion, cola_vacia, en_frente, tamanio
from validaciones import validar_numero


TIEMPOS_PISTA = {
    "pasajeros": {"aterrizaje": 10, "despegue": 5},
    "negocios":  {"aterrizaje": 5,  "despegue": 3},
    "carga":     {"aterrizaje": 12, "despegue": 9}
}

TIPOS = {"1": "pasajeros", "2": "negocios", "3": "carga"}

# funciones auxiliares

# limpia la consola de comandos
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# pide y valida la hora en formato HH:MM
def validar_hora(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return datetime.strptime(entrada, "%H:%M")
        except ValueError:
            print("  Formato inválido. Use HH:MM (ej: 14:30)")

# pide un texto y valida que no este vacio unicamente
def validar_texto(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        print("  No puede quedar vacío.")

# pide y valida el tipo de avion
def validar_tipo():
    while True:
        print("  1 = Pasajeros  2 = Negocios  3 = Carga")
        op = input("  Tipo de vuelo:        ")
        if op in TIPOS:
            return TIPOS[op]
        print("  Opción inválida.")


# funciones de carga 

# pide informacion sobre un vuelo y lo retorna en forma de diccionario
def cargar_vuelo(es_despegue):
    """Solicita los datos del vuelo y retorna un diccionario."""
    modo = "despegue" if es_despegue else "aterrizaje"
    print(f"\n  ── Nuevo vuelo de {modo} ──")
    empresa      = validar_texto("  Empresa:              ")
    origen       = validar_texto("  Aeropuerto origen:    ")
    destino      = validar_texto("  Aeropuerto destino:   ")
    tipo_avion   = validar_tipo()
    hora_salida  = validar_hora ("  Hora salida  (HH:MM): ") if es_despegue  else None
    hora_llegada = validar_hora ("  Hora llegada (HH:MM): ") if not es_despegue else None

    return {
        "empresa":       empresa,
        "origen":        origen,
        "destino":       destino,
        "tipo":          tipo_avion,
        "hora_salida":   hora_salida,
        "hora_llegada":  hora_llegada,
    }

# inserta los despegues de manera ordenada por hora de salida
def insertar_despegue_ordenado(cola_despegues, vuelo):
    """Inserta en la cola de despegues ordenado por hora de salida."""
    cola_aux  = Cola()
    insertado = False

    while not cola_vacia(cola_despegues):
        actual = en_frente(cola_despegues)
        if not insertado and vuelo["hora_salida"] <= actual["hora_salida"]:
            arribo(cola_aux, vuelo)
            insertado = True
        arribo(cola_aux, atencion(cola_despegues))

    if not insertado:
        arribo(cola_aux, vuelo)

    while not cola_vacia(cola_aux):
        arribo(cola_despegues, atencion(cola_aux))

# retorna la ultima hora de salida para los despliegues
# se podria reformular como una funcion que retorna cola.final.info
def ultimo_horario(cola_despegues):
    """Retorna la hora de salida del último vuelo en la cola."""
    cola_aux = Cola()
    ultima   = None

    while not cola_vacia(cola_despegues):
        v      = atencion(cola_despegues)
        ultima = v["hora_salida"]
        arribo(cola_aux, v)

    while not cola_vacia(cola_aux):
        arribo(cola_despegues, atencion(cola_aux))

    return ultima

# funciones visuales para la consola de comandos

# pantalla para mostrar cantidad de vuelos por tipo y proximo vuelo
def mostrar_estado(cola_d, cola_a, hora_actual):
    limpiar()
    print("╔══════════════════════════════════════════════════╗")
    print(f"║     AEROPUERTO              Hora: {hora_actual.strftime('%H:%M')}          ║")
    print("╠══════════════════════════════════════════════════╣")

    print(f"║    Despegues   ({tamanio(cola_d):>2} vuelos )                      ║")
    cola_aux = Cola()
    while not cola_vacia(cola_d):
        v = atencion(cola_d)
        linea = f"    {v['empresa']:<18} {v['tipo']:<10} Salida: {v['hora_salida'].strftime('%H:%M')}"
        print(f"║{linea:<50}║")
        arribo(cola_aux, v)
    while not cola_vacia(cola_aux):
        arribo(cola_d, atencion(cola_aux))

    print("║──────────────────────────────────────────────────║")

    print(f"║    Aterrizajes ({tamanio(cola_a):>2} vuelos )                      ║")
    cola_aux = Cola()
    while not cola_vacia(cola_a):
        v = atencion(cola_a)
        linea = f"  {v['empresa']:<18} {v['tipo']:<10} Llegada: {v['hora_llegada'].strftime('%H:%M')}"
        print(f"║{linea:<50}║")
        arribo(cola_aux, v)
    while not cola_vacia(cola_aux):
        arribo(cola_a, atencion(cola_aux))

    print("╚══════════════════════════════════════════════════╝\n")

# Uso de pista 
def usar_pista(vuelo, operacion):
    """Ocupa la pista el tiempo correspondiente con countdown."""
    segundos = TIEMPOS_PISTA[vuelo["tipo"]][operacion]
    print(f"\n {operacion.upper()}: {vuelo['empresa']} ({vuelo['tipo']})")
    print(f"   {vuelo['origen']}  →  {vuelo['destino']}")
    print(f"   Pista ocupada — {segundos}s")

    for t in range(segundos, 0, -1):
        print(f"     {t:>2}s  ", end="\r")
        time.sleep(1)

    print("     Pista libre.          ")

# Atención de vuelos
def atender_aterrizaje(cola_aterrizajes):
    vuelo = atencion(cola_aterrizajes)
    usar_pista(vuelo, "aterrizaje")

def atender_despegue(cola_despegues):
    """Atiende el despegue del frente: proceder, cancelar o reprogramar."""
    vuelo = en_frente(cola_despegues)
    print(f"\n  DESPEGUE pendiente: {vuelo['empresa']} ({vuelo['tipo']})")
    print(f"   Salida: {vuelo['hora_salida'].strftime('%H:%M')}  │  "
          f"{vuelo['origen']} → {vuelo['destino']}")
    print("   1. Proceder   2. Cancelar   3. Reprogramar")

    op = validar_numero("   Opción: ")

    if op == 1:
        atencion(cola_despegues)
        usar_pista(vuelo, "despegue")

    elif op == 2:
        atencion(cola_despegues)
        print(f"     Vuelo de {vuelo['empresa']} cancelado.")

    elif op == 3:
        atencion(cola_despegues)              # saco el vuelo de la cola
        ultima = ultimo_horario(cola_despegues)

        if ultima:
            print(f"   Último horario en cola: {ultima.strftime('%H:%M')}")

        while True:
            nueva = validar_hora("   Nueva hora de salida (HH:MM): ")
            if ultima is None or nueva > ultima:
                break
            print(f"     Debe ser posterior a {ultima.strftime('%H:%M')}.")

        vuelo["hora_salida"] = nueva
        arribo(cola_despegues, vuelo)         # va al final → ya es el más tardío
        print(f"     Reprogramado para las {nueva.strftime('%H:%M')}.")

# Menú de carga posterior 
def menu_agregar(cola_despegues, cola_aterrizajes):
    while True:
        print("\n  ¿Agregar vuelos?  1 = Despegue  2 = Aterrizaje  0 = Continuar")
        op = validar_numero("  Opción: ")
        if op == 1:
            vuelo = cargar_vuelo(es_despegue=True)
            insertar_despegue_ordenado(cola_despegues, vuelo)
            print("  Vuelo de despegue agregado.")
        elif op == 2:
            vuelo = cargar_vuelo(es_despegue=False)
            arribo(cola_aterrizajes, vuelo)
            print("  Vuelo de aterrizaje agregado.")
        elif op == 0:
            break

# Logica de prioridad
def es_hora_despegue(cola_despegues, hora_actual):
    """True si la hora actual >= hora de salida del primer vuelo en cola."""
    if cola_vacia(cola_despegues):
        return False
    return hora_actual >= en_frente(cola_despegues)["hora_salida"]

# MAIN
cola_despegues   = Cola()
cola_aterrizajes = Cola()

print("SISTEMA DE GESTIÓN DE AEROPUERTO\n")
print("Cargue los vuelos iniciales:")
menu_agregar(cola_despegues, cola_aterrizajes)

hora_actual = validar_hora("\nHora de inicio de simulación (HH:MM): ")

while not (cola_vacia(cola_despegues) and cola_vacia(cola_aterrizajes)):

    mostrar_estado(cola_despegues, cola_aterrizajes, hora_actual)

    hay_despegue_urgente = es_hora_despegue(cola_despegues, hora_actual)
    hay_aterrizaje       = not cola_vacia(cola_aterrizajes)
    hay_despegue         = not cola_vacia(cola_despegues)

    if hay_despegue_urgente:
        # Prioridad de despegue programado 
        print("   Hora de despegue alcanzada — prioridad de pista.")
        atender_despegue(cola_despegues)

    elif hay_aterrizaje:
        # si no hay despliegue urgente entonces siempre atender aterrizajes 
        atender_aterrizaje(cola_aterrizajes)

    else:
        # Solo hay despegues y aún no es la hora, entonces saltamos a la hora del proximo evento
        primer = en_frente(cola_despegues)
        print(f"  Sin aterrizajes. Próximo despegue: "
              f"{primer['empresa']} a las {primer['hora_salida'].strftime('%H:%M')}")
        hora_actual = primer["hora_salida"]   
        continue

    # Después de cada operación: agregar vuelos y avanzar hora 
    menu_agregar(cola_despegues, cola_aterrizajes)
    hora_actual = validar_hora("\nHora actual (HH:MM): ")

limpiar()
print("  No quedan vuelos pendientes. Simulación finalizada.")