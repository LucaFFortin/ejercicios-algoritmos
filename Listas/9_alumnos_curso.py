"""
Se tiene una lista de los alumnos de un curso, de los que se sabe nombre, apellido y legajo. 
Por otro lado se tienen las notas de los diferentes parciales que rindió cada uno de ellos con 
la siguiente información: materia que rindió, nota obtenida y fecha de parcial. Desarrollar un 
algoritmo que permita realizar la siguientes actividades:
a. mostrar los alumnos ordenados alfabéticamente por apellido; !
b. indicar los alumnos que no desaprobaron ningún parcial; !
c. determinar los alumnos que tienen promedio mayor a 8,89; !
d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L; !
e. mostrar el promedio de cada uno de los alumnos; !
f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”; !
g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;  !
h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”; !
i. mostrar todos los alumnos que rindieron en el año 2020; - otia
j. debe modificar el TDA para implementar lista de lista !

estructura:
alumno n: parciales -> [materia, nota, fecha]
"""
# agregar validacion de fechas en la estructura para hacerlo mas fiable

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from validaciones import validar_numero, validar_string
from utils import limpiar
from tda_listas import insertar, lista_vacia, eliminar, barrido, tamanio, buscar, criterio, buscar_criterio, insertar_criterio, eliminar_criterio, Lista, nodoLista

# clase de lista interna
class ListaInterna(object):
    """Clase lista simplemente enlazada"""
    
    def __init__(self):
        """Crea una lista Vacia"""
        self.inicio = None
        self.tamanio = 0
        self.sig = None
        self.info = None

# funcion para insertar lista interna ordenada por el primer campo que haya en lista_interna.info
def insertar_Lista(lista, lista_interna):
    """Insertar el dato pasado en la lista."""
    if (lista.inicio is None) or (lista.inicio.info[0] > lista_interna.info[0]):
        lista_interna.sig = lista.inicio
        lista.inicio = lista_interna
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while (act is not None and act.info[0] < lista_interna.info[0]):
            ant = ant.sig
            act = act.sig
        lista_interna.sig = act
        ant.sig = lista_interna
    lista.tamanio += 1

def barrido_lista_dinamica(lista):
    alumno = lista.inicio
    while(alumno is not None):
        print(alumno.info)
        parcial = alumno.inicio
        while(parcial is not None):
            print("", parcial.info)
            parcial = parcial.sig
        alumno = alumno.sig


# limpiamos todos los comandos anteriores
limpiar()

# ingreso de datos
lista = Lista()

# while (True):
#     opcion = validar_string("Desea ingresar un alumno a la lista?, Si para ingresar, No para salir: ").lower()

#     if (opcion == "no"): 
#         limpiar()
#         break
#     elif (opcion == "si"):
#         # solicitamos los datos del alumno
#         nombre = validar_string("Ingrese el nombre del estudiante: ")
#         apellido = validar_string("Ingrese el apellido del estudiante: ")
#         legajo = validar_numero("Ingrese el numero de legajo del estudiante: ")

#         # juntamos los datos en una lista
#         alumno = ListaInterna()
#         alumno.info = [apellido, nombre, legajo]

#         # insertamos al alumno dentro de la lista
#         insertar_Lista(lista, alumno)     

#         # cargamos los parciales de los alumnos
#         while (True):
#             opcion = validar_string("Desea registrar un parcial de este alumno?, Si para ingresar, No para salir: ").lower()

#             if (opcion == "no"): 
#                 limpiar()
#                 break
#             elif (opcion == "si"):
#                 materia = validar_string("Ingrese el nombre de la materia del parcial: ")
#                 nota = validar_numero("Ingrese la nota del parcial: ")
#                 fecha = validar_string("Ingrese la fecha del parcial: ")

#                 parcial = [materia, nota, fecha]

#                 insertar(alumno, parcial)        
#                 limpiar()
#             else:    
#                 limpiar()
#                 print("La opcion ingresada no esta dentro de las opciones listadas.")
#         limpiar()
#     else:    
#         limpiar()
#         print("La opcion ingresada no esta dentro de las opciones listadas.")

# simulacion
alumno = ListaInterna()
alumno.info = ["fortin", "luca", tamanio(lista) + 1]
insertar_Lista(lista, alumno)
parcial = ["algoritmos y estructura de datos", 7, "9/12/18"]
insertar(alumno, parcial)
parcial = ["bases de datos", 7, "9/12/18"]
insertar(alumno, parcial)
parcial = ["Algebra", 7, "9/12/18"]
insertar(alumno, parcial)

alumno = ListaInterna()
alumno.info = ["benitez", "nicolas", tamanio(lista) + 1]
insertar_Lista(lista, alumno)
parcial = ["algoritmos y estructura de datos", 10, "9/12/18"]
insertar(alumno, parcial)
parcial = ["bases de datos", 10, "9/12/18"]
insertar(alumno, parcial)
parcial = ["Algebra", 9, "9/12/18"]
insertar(alumno, parcial)

alumno = ListaInterna()
alumno.info = ["baragaño", "matias", tamanio(lista) + 1]
insertar_Lista(lista, alumno)
parcial = ["algoritmos y estructura de datos", 7, "9/12/18"]
insertar(alumno, parcial)
parcial = ["bases de datos", 7, "9/12/18"]
insertar(alumno, parcial)
parcial = ["Algebra", 7, "9/12/18"]
insertar(alumno, parcial)

alumno = ListaInterna()
alumno.info = ["becaccece", "gonzalo", tamanio(lista) + 1]
insertar_Lista(lista, alumno)
parcial = ["algoritmos y estructura de datos", 7, "9/12/20"]
insertar(alumno, parcial)
parcial = ["bases de datos", 7, "9/12/18"]
insertar(alumno, parcial)
parcial = ["Algebra", 7, "9/12/18"]
insertar(alumno, parcial)

alumno = ListaInterna()
alumno.info = ["Aquino", "Ramiro", tamanio(lista) + 1]
insertar_Lista(lista, alumno)
parcial = ["algoritmos y estructura de datos II", 7, "9/12/18"]
insertar(alumno, parcial)
parcial = ["bases de datos", 7, "9/12/18"]
insertar(alumno, parcial)
parcial = ["Algebra", 2, "9/12/18"]
insertar(alumno, parcial)

alumno = ListaInterna()
alumno.info = ["Luongo", "Mauro", tamanio(lista) + 1]
insertar_Lista(lista, alumno)
parcial = ["algoritmos y estructura de datos III", 1, "9/12/18"]
insertar(alumno, parcial)
parcial = ["bases de datos", 1, "9/12/2020"]
insertar(alumno, parcial)
parcial = ["Algebra", 1, "9/12/18"]
insertar(alumno, parcial)

# a
barrido_lista_dinamica(lista)

# b
print("Alumnos que aprobaron todas las materias:")
alumno = lista.inicio
while(alumno is not None):
    parcial = alumno.inicio
    aprobo_todo = True
    while(parcial is not None):
        if (parcial.info[1] < 4): 
            aprobo_todo = False
        parcial = parcial.sig
    if (aprobo_todo): print(alumno.info)
    alumno = alumno.sig

# c
print("Alumnos que tienen un promedio mayor a 8.89:")
alumno = lista.inicio
while(alumno is not None):
    parcial = alumno.inicio
    cont = 0.0
    acc = 0.0
    while(parcial is not None):
        cont += 1
        acc += parcial.info[1]
        parcial = parcial.sig
    if (acc/cont > 8.89): print(alumno.info)
    alumno = alumno.sig

# d
print("Alumnos cuyo apellido inicia con L:")
alumno = lista.inicio
while(alumno is not None):
    if (alumno.info[0][0] == "l" or alumno.info[0][0] == "L"):
        print(f"Alumno: {alumno.info[1]} {alumno.info[0]}, legajo: {alumno.info[2]}")
        parcial = alumno.inicio
        while(parcial is not None):
            print(f"Parcial de la materia {parcial.info[0]} con nota {parcial.info[1]} del dia {parcial.info[2]}.")
            parcial = parcial.sig
    alumno = alumno.sig

# e
print("Promedio de todos los alumnos")
alumno = lista.inicio
while(alumno is not None):
    parcial = alumno.inicio
    cont = 0.0
    acc = 0.0
    while(parcial is not None):
        cont += 1
        acc += parcial.info[1]
        parcial = parcial.sig
    promedio = acc/cont
    print(f"Alumno: {alumno.info[1]} {alumno.info[0]}, promedio: {promedio}.")
    alumno = alumno.sig

# f
print("Alumnos que rindieron la catedra de Algoritmos y estructura de datos: ")
alumno = lista.inicio
while(alumno is not None):
    parcial = alumno.inicio
    rindio = False
    while(parcial is not None):
        if (parcial.info[0] == "algoritmos y estructura de datos"): rindio = True
        parcial = parcial.sig
    if (rindio): print(f"Alumno: {alumno.info[1]} {alumno.info[0]}")
    alumno = alumno.sig

# g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario; 
print("Porcentaje de parciales aprobados del alumno ingresado: ")
legajo = validar_numero("Ingrese el legajo del alumno a mostrar: ")
alumno = lista.inicio
mostrado = False
while(alumno is not None):
    cont, total = 0, 0
    if (alumno.info[2] == legajo):
        mostrado = True
        parcial = alumno.inicio
        while(parcial is not None):
            total += 1
            if (parcial.info[1] >= 4): cont += 1
            parcial = parcial.sig
        print(f"El promedio de materias aprobadas del alumno {alumno.info[1]} {alumno.info[0]} es de {cont * 100 / total}%.")
    alumno = alumno.sig
if (not mostrado): print("El legajo ingresado no existe en la lista.")

# h
print("Alumnos que aprobaron la catedra de bases de datos: ")
alumno = lista.inicio
aprobados = 0
desaprobados = 0
while(alumno is not None):
    parcial = alumno.inicio
    rindio = False
    while(parcial is not None):
        if (parcial.info[0] == "bases de datos"):
            if (parcial.info[1] >= 4): aprobados += 1
            else: desaprobados += 1
        parcial = parcial.sig
    alumno = alumno.sig
print(f"Cantidad de alumnos aprobados: {aprobados}.")
print(f"Cantidad de alumnos desaprobados: {desaprobados}.")

# i. mostrar todos los alumnos que rindieron en el año 2020; 
print("Alumnos que rindieron en el año 2020: ")
alumno = lista.inicio
while(alumno is not None):
    mostrado = False
    parcial = alumno.inicio
    rindio = False
    while(parcial is not None):
        if ((parcial.info[2][-2:] == "20" or parcial.info[2][-4:] == "2020") and not mostrado): 
            mostrado = True
            print(f"Alumno {alumno.info[1]} {alumno.info[0]} rindio en el año 2020")
        parcial = parcial.sig
    alumno = alumno.sig
