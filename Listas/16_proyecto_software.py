"""
16. Se deben administrar las actividades de un proyecto de software, de estas se conoce su costo, 
tiempo de ejecución, fecha de inicio, fecha de fin estimada, fecha de fin efectiva y persona a 
cargo. Desarrollar un algoritmo que realice las siguientes actividades:
a. tiempo promedio de tareas;
b. costo total del proyecto;
c. actividades realizadas por una determinada persona;
d. mostrar la información de las tareas a realizar entre dos fechas dadas;
e. mostrar las tareas finalizadas en tiempo y las finalizadas fuera de tiempo;
f. indicar cuántas tareas le quedan pendientes a una determinada persona, indicada por el usuario.
"""
import sys
from pathlib import Path
import datetime, time

sys.path.append(str(Path(__file__).resolve().parent.parent))

from validaciones import validar_string, validar_numero_flotante, validar_numero, validar_fecha
from utils import limpiar
from tda_listas import insertar, lista_vacia, eliminar, barrido, tamanio, buscar, criterio, buscar_criterio, insertar_criterio, eliminar_criterio, Lista, nodoLista

def buscar_por_indice(lista, valor_buscado, indice):
    aux = lista.inicio
    while aux is not None and aux.info[indice] != valor_buscado:
        aux = aux.sig
    return aux

empleados = Lista()
tareas = Lista()

# menu
while True:
    print("Menu de administracion de proyectos")
    opcion = validar_numero("""Opciones: 
    1 - Añadir personal
    2 - Añadir tarea
    3 - Calcular tiempo promedio de las tareas
    4 - Calcular coste total del proyecto
    5 - Mostrar tareas realizadas de una persona
    6 - Tareas a realizar entre 2 fechas
    7 - Mostrar tareas realizadas a tiempo y fuera de tiempo
    8 - Mostrar tareas pendientes de una persona
    0 - Salir
Ingrese una opcion: """)

    limpiar()

    # ingreso de empleado
    if (opcion == 1):
        nombre = validar_string("Ingrese el nombre del empleado: ")
        id = validar_numero("Ingrese el identificador del empleado: ")

        while (buscar_por_indice(empleados, id, 1) is not None):
            print("El ID ingresado ya fue asignado a otro empleado.")
            id = validar_numero("Ingrese el identificador del empleado: ")
            
        insertar(empleados, [nombre, id])
    # ingreso de tarea
    elif (opcion == 2):
        costo = validar_numero_flotante("Ingrese el costo de la tarea: ")
        while (costo <= 0):
            print("El costo debe ser un numero positivo.")
            costo = validar_numero_flotante("Ingrese el costo de la tarea: ")

        tiempo_ejecucion = validar_numero("Ingrese el tiempo de ejecucion de la tarea (en horas): ")
        while (tiempo_ejecucion <= 0):
            print("El tiempo de ejecución debe ser mayor a 0.")
            tiempo_ejecucion = validar_numero("Ingrese el tiempo de ejecucion de la tarea (en horas): ")

        fecha_inicio = validar_fecha("Ingrese la fecha de inicio de la tarea (DD-MM-YYYY): ")
        while (fecha_inicio is None):
            print("La fecha de inicio no puede quedar vacia.")
            fecha_inicio = validar_fecha("Ingrese la fecha de inicio de la tarea (DD-MM-YYYY): ")

        fecha_estimada = validar_fecha("Ingrese la fecha estimada de finalizacion de la tarea (DD-MM-YYYY): ")
        while (fecha_estimada is None or fecha_estimada < fecha_inicio):
            print("La fecha estimada es invalida, debe ser mayor o igual a la fecha de inicio.")
            fecha_estimada = validar_fecha("Ingrese la fecha de inicio de la tarea (DD-MM-YYYY): ")

        fecha_real = validar_fecha("Ingrese la fecha real de finalizacion de la tarea (DD-MM-YYYY) o deje en blanco si no ha finalizado: ")
        persona_cargo = validar_numero("Ingrese el identificador del empleado a cargo de la tarea: ")

        # Validar que el id del empleado exista
        empleado_encontrado = buscar_por_indice(empleados, persona_cargo, 1)

        while empleado_encontrado is None:
            print(f"No se encontró un empleado con el ID {persona_cargo}. La tarea no se añadirá.")
            persona_cargo = validar_numero("Ingrese un ID de empleado válido: ")
            empleado_encontrado = buscar_por_indice(empleados, persona_cargo, 1)

        insertar(tareas, [costo, tiempo_ejecucion, fecha_inicio, fecha_estimada, fecha_real, persona_cargo])
    # calculo de tiempo promedio de tareas
    elif (opcion == 3):
        total_tiempo = 0
        total_tareas = tamanio(tareas)
        aux = tareas.inicio
        while aux is not None:
            total_tiempo += aux.info[1]  # tiempo_ejecucion
            aux = aux.sig
        if total_tareas > 0:
            promedio_tiempo = total_tiempo / total_tareas
            print(f"El tiempo promedio de las tareas es: {promedio_tiempo} horas.")
        else:
            print("No hay tareas registradas para calcular el tiempo promedio.")
    # calculo de costo total del proyecto
    elif (opcion == 4):
        total_costo = 0
        aux = tareas.inicio
        while aux is not None:
            total_costo += aux.info[0]  # costo
            aux = aux.sig
        print(f"El costo total del proyecto es: {total_costo}.")
    # mostrar tareas realizadas de una persona
    elif (opcion == 5):
        id_persona = validar_numero("Ingrese el identificador del empleado: ")

        # Validar que el id del empleado exista
        empleado_encontrado = buscar_por_indice(empleados, id_persona, 1)
        if empleado_encontrado is None:
            print(f"No se encontró un empleado con el ID {id_persona}. La tarea no se añadirá.")
        else:
            aux = tareas.inicio
            tareas_persona = []
            while aux is not None:
                if aux.info[5] == id_persona and aux.info[4] is not None:  # persona_cargo y fecha_real
                    tareas_persona.append(aux.info)
                aux = aux.sig
            if tareas_persona:
                print(f"Tareas realizadas por el empleado con ID {id_persona}:")
                for tarea in tareas_persona:
                    print(tarea)
            else:
                print(f"No se encontraron tareas realizadas por el empleado con ID {id_persona}.")
    # mostrar tareas a realizar entre 2 fechas
    elif (opcion == 6):
        fecha_inicio = validar_fecha("Ingrese la fecha de inicio del rango (DD-MM-YYYY): ")
        fecha_fin = validar_fecha("Ingrese la fecha de fin del rango (DD-MM-YYYY): ")

        aux = tareas.inicio
        tareas_en_rango = []
        while aux is not None:
            if fecha_inicio <= aux.info[2] <= fecha_fin:  # fecha_inicio de la tarea
                tareas_en_rango.append(aux.info)
            aux = aux.sig
        if tareas_en_rango:
            print(f"Tareas a realizar entre {fecha_inicio} y {fecha_fin}:")
            for tarea in tareas_en_rango:
                print(tarea)
        else:
            print(f"No se encontraron tareas a realizar entre {fecha_inicio} y {fecha_fin}.")
    # mostrar tareas realizadas a tiempo y fuera de tiempo
    elif (opcion == 7):
        tareas_en_tiempo = []
        tareas_fuera_tiempo = []
        aux = tareas.inicio
        while aux is not None:
            if aux.info[4] <= aux.info[3]:  # fecha_real <= fecha_estimada
                tareas_en_tiempo.append(aux.info)
            else:
                tareas_fuera_tiempo.append(aux.info)
            aux = aux.sig
        if (tareas_en_tiempo):
            print("Tareas finalizadas a tiempo:")
            for tarea in tareas_en_tiempo:
                print(tarea)
        else:
            print("No se encontraron tareas finalizadas a tiempo.")
        if (tareas_fuera_tiempo):
                
            print("Tareas finalizadas fuera de tiempo:")
            for tarea in tareas_fuera_tiempo:
                print(tarea)
        else:
            print("No se encontraron tareas finalizadas fuera de tiempo.")
    # mostrar tareas pendientes de una persona
    elif (opcion == 8):
        id_persona = validar_numero("Ingrese el identificador del empleado: ")
        
        # Validar que el id del empleado exista
        empleado_encontrado = buscar_por_indice(empleados, id_persona, 1)
        if empleado_encontrado is None:
            print(f"No se encontró un empleado con el ID {id_persona}. La tarea no se añadirá.")
        else:
            aux = tareas.inicio
            tareas_pendientes = []
            while aux is not None:
                if aux.info[5] == id_persona and aux.info[4] is None:  # persona_cargo y fecha_real
                    tareas_pendientes.append(aux.info)
                aux = aux.sig
            if tareas_pendientes:
                print(f"Tareas pendientes del empleado con ID {id_persona}:")
                for tarea in tareas_pendientes:
                    print(tarea)
            else:
                print(f"No se encontraron tareas pendientes para el empleado con ID {id_persona}.")
    # condicion de salida
    elif (opcion == 0):
        break
    # opcion invalida
    else:
        print("Opción no válida. Por favor, intente de nuevo.")