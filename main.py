import subprocess

ejercicios = {
    "Repaso": {

        1: [
            "python",
            r"Repaso\Semana 1\pascal.py"
        ],

        2: [
            "python",
            r"Repaso\Semana 2\alquiler_automoviles.py"
        ],

        3: [
            "python",
            r"Repaso\Semana 2\convertidor_temperatura.py"
        ],

        4: [
            "python",
            r"Repaso\Semana 2\primo_compuesto.py"
        ],

        5: [
            "python",
            r"Repaso\Semana 2\serie_armonica.py"
        ],

        6: [
            "python",
            r"Repaso\Semana 3\combinacion_bits.py"
        ],

        7: [
            "python",
            r"Repaso\Semana 3\combinacion_letras.py"
        ],

        8: [
            "python",
            r"Repaso\Semana 3\factorial.py"
        ],

        9: [
            "python",
            r"Repaso\Semana 3\numeros_perfectos.py"
        ],

        10: [
            "python",
            r"Repaso\Semana 4\histograma_frecuencias.py"
        ],

        11: [
            "python",
            r"Repaso\Semana 4\lector_matriz.py"
        ],

        12: [
            "python",
            r"Repaso\Semana 4\matriz_simetrica.py"
        ],

        13: [
            "python",
            r"Repaso\Semana 4\numeros_vampiros.py"
        ]
    },
    "Pilas": {
        1: ["python",r"Pilas\ocurrencias_valor.py"],

        2: ["python",r"Pilas\eliminar_impares.py"],

        3: ["python",r"Pilas\reemplazar_valor.py"],

        4: ["python",r"Pilas\invertir_pila.py"],

        5: ["python",r"Pilas\palindromo.py"],

        6: ["python",r"Pilas\palabra_inversa.py"],

        7: ["python",r"Pilas\eliminar_elemento.py"],

        8: ["python",r"Pilas\cartas.py"],

        9: ["python",r"Pilas\factorial.py"],

        10: ["python",r"Pilas\insertar_atenea.py"],

        11: ["python",r"Pilas\contar_vocales.py"],

        12: ["python",r"Pilas\encontrar_personajes.py"],

        13: ["python",r"Pilas\ironman.py"],

        14: ["python",r"Pilas\insertar_ascendente.py"],

        17: ["python",r"Pilas\separar_parrafo.py"],
    
        18: ["python",r"Pilas\objetos_oficina.py"],

        20: ["python",r"Pilas\pasos_robot.py"],

        23: ["python", r"Pilas\temperatura_abril.py"]
    },
    "Colas": {
        1:  ["python", r"Colas\Ej1 eliminar_vocales.py"],
        2:  ["python", r"Colas\Ej2 invertir_cola.py"],
        3:  ["python", r"Colas\Ej3 palindromo.py"],
        4:  ["python", r"Colas\Ej4 primos.py"],
        5:  ["python", r"Colas\Ej5 invertir_pila.py"],
        6:  ["python", r"Colas\Ej6 contar_ocurrencias.py"],
        7:  ["python", r"Colas\Ej7 eliminar_iesimo.py"],
        8:  ["python", r"Colas\Ej8 ordenar_entradas.py"],
        9:  ["python", r"Colas\Ej9_rango_enteros.py"],
        10: ["python", r"Colas\Ej10_notificaciones.py"],
        12: ["python", r"Colas\Ej12_combinar_colas.py"],
        13: ["python", r"Colas\Ej13_caracteres.py"],
        14: ["python", r"Colas\Ej14_semaforos.py"],
        15: ["python", r"Colas\Ej15_coordenadas_base.py"],
        16: ["python", r"Colas\Ej16_cola_prioritaria.py"],
        18: ["python", r"Colas\Ej18_turnos.py"],
        19: ["python", r"Colas\Ej19_cola_circular.py"],
        20: ["python", r"Colas\Ej20_puesto_peaje.py"],
        21: ["python", r"Colas\Ej21_aeropuerto.py"],
    }
}

lista_ejercicios_repaso = """A continuacion se listaran los ejercicios disponibles

SEMANA 1
1: Triangulo de pascal

SEMANA 2
2: Alquiler automoviles
3: Convertidor temperatura
4: Primo compuesto
5: Serie armonica

SEMANA 3
6: Combinacion bits
7: Combinacion letras
8: Factorial
9: Numeros perfectos

SEMANA 4
10: Histograma frecuencias
11: Lector matriz
12: Matriz simetrica
13: Numeros vampiros"""

lista_ejercicios_pilas = """
1:  Ocurrencias de un elemento
2:  Eliminar elementos impares
3:  Reemplazar ocurrencias de un elemento
4:  Invertir una pila
5:  Palíndromo
6:  Palabra inversa
7:  Eliminar elemento i-ésimo
8:  Pila de cartas
9:  Factorial con pila
10: Insertar Atenea en posición i
11: Contar vocales
12: Encontrar personajes de Star Wars
13: Trajes de Iron Man
14: insertar ordenado
17: separar parrafo
18: Insertar elementos ordenados
20: Movimientos de robot
23: Temperaturas de abril
"""

lista_ejercicios_colas = """
1:  Eliminar vocales
2:  Invertir una cola
3:  Palíndromo
4:  Números primos
5:  Invertir pila con cola
6:  Contar ocurrencias
7:  Eliminar elemento i-ésimo
8:  Ordenar entradas
9:  Rango de enteros
10: Notificaciones
12: Combinar colas
13: Caracteres
14: Semáforos
15: Coordenadas base
16: Cola prioritaria
18: Turnos
19: Cola circular
20: Puesto de peaje
21: Aeropuerto
"""

print("Bienvenido al sistema de ejercicios\n")
while (True):
    opcion = input("Que ejercicios desea ver (Repaso, Pilas o Colas, 0 para salir): ").lower()
    if (opcion == "repaso"):
        print(lista_ejercicios_repaso)
        opcion = int(input("Escriba el numero del ejercicio que desea ejecutar: "))
        if (opcion in range(14)):
            subprocess.run(ejercicios["Repaso"][opcion])
        else:
            print("El programa seleccionado no existe.")
    elif (opcion == "pilas"):
        print(lista_ejercicios_pilas)
        opcion = int(input("Escriba el numero del ejercicio que desea ejecutar: "))
        if (opcion in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17, 18, 20, 23]):
            subprocess.run(ejercicios["Pilas"][opcion])
        else:
            print("El programa seleccionado no existe.")
    elif (opcion == "colas"):
        print(lista_ejercicios_colas)
        opcion = int(input("Escriba el numero del ejercicio que desea ejecutar: "))
        if (opcion in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21]):
            subprocess.run(ejercicios["Colas"][opcion])
        else:
            print("El programa seleccionado no existe.")
    elif (opcion == "0"): break
    else:
        print("Opcion invalida, seleccione una de las opciones listadas.")