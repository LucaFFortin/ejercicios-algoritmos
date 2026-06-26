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
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio

empleados = Cola()
staff = Cola()
gerentes = Cola()
documentos_en_cola = 0

def ingresar_documento(cargo, documento):
    if (cargo.lower() == "empleado"): arribo(empleados, documento)
    elif (cargo.lower() == "staff"): arribo(staff, documento)
    elif (cargo.lower() == "gerente"): arribo(gerentes, documento)
    else: print("Cargo no reconocido, debe ingresar una de las siguientes opciones: 'Empleados', 'Staff' o 'Gerente'.")

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


simular_situacion()