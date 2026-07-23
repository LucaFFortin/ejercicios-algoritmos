"""
Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
siguiente situación:
a. cargue tres documentos de empleados (cada documento se representa solamente con
un nombre).
b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
c. cargue dos documentos del staff de TI.
d. cargue un documento del gerente.
e. imprima los dos primeros documentos de la cola.
f. cargue dos documentos de empleados y uno de gerente.
g. imprima todos los documentos de la cola de impresión.
"""
import math
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
from validaciones import validar_numero_flotante, validar_string, validar_numero

# creamos 3 colas especificas para cada tipo de trabajo
empleados = Cola()
staff = Cola()
gerentes = Cola()
documentos_en_cola = 0

# ingresamos el documento en la cola correspondiente al cargo ingresado o indicamos que el cargo es incorrecto
def ingresar_documento(cargo, documento):
    if (cargo.lower() == "empleado"): arribo(empleados, documento)
    elif (cargo.lower() == "staff"): arribo(staff, documento)
    elif (cargo.lower() == "gerente"): arribo(gerentes, documento)
    else: print("Cargo no reconocido, debe ingresar una de las siguientes opciones: 'Empleados', 'Staff' o 'Gerente'.")

# imprimimos el documeno priorizando empleados primero, staff segundo y gerentes tercero
# si no hay le indicamos a traves de un mensaje que no es posible imprimir
def imprimir_documento():
    if (tamanio(empleados) >= 1):
        documento = atencion(empleados)
        print(documento)
    elif (tamanio(staff) >= 1):
        documento = atencion(staff)
        print(documento)
    elif (tamanio(gerentes) >= 1):
        documento = atencion(gerentes)
        print(documento)
    else:
        print("No hay documentos en la cola de impresión.")
    
# simulamos la situacion planteada en el enunciado
def simular_situacion():
    # 1er paso
    ingresar_documento("empleado", "empleado 1")
    ingresar_documento("empleado", "empleado 2")
    ingresar_documento("empleado", "empleado 3")

    # 2do paso
    imprimir_documento()

    # 3er paso
    ingresar_documento("staff", "staff 1")
    ingresar_documento("staff", "staff 2")

    # 4to paso
    ingresar_documento("gerente", "gerente 1")

    # 5to paso
    imprimir_documento()
    imprimir_documento()

    # 6to paso
    ingresar_documento("empleado", "empleado 4")
    ingresar_documento("empleado", "empleado 5")
    ingresar_documento("gerente", "gerente 2")

    while (tamanio(empleados) + tamanio(staff) + tamanio(gerentes) > 0):
        imprimir_documento()


# punto de acceso a la aplicacion
opcion = validar_string("Desea ingresar documentos? 1 para ingresar, 2 para imprimir, 3 para ejecutar simulacion, 0 para salir: ")
while (True):
    if (opcion == "1"):
        cargo = validar_string("ingrese el cargo que necesita el documento [empleado, staff, gerente]: ")
        documento = validar_string("Ingrese el contenido del documento a imprimir")
        ingresar_documento(cargo, documento)
    elif (opcion == "2"):
        imprimir_documento()
    elif(opcion == "3"):
        simular_situacion()
    elif (opcion == "0"):
        break
    else:
        print("Opcion no reconocida.")
    opcion = validar_string("Desea ingresar mas documentos? 1 para ingresar, 2 para imprimir, 3 para ejecutar simulacion, 0 para salir: ")