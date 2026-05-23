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
        1: [
            "python",
            r"Pilas\ocurrencias_valor.py"
        ],

        2: [
            "python",
            r"Pilas\eliminar_impares.py"
        ],

        3: [
            "python",
            r"Pilas\reemplazar_valor.py"
        ],

        4: [
            "python",
            r"Pilas\invertir_pila.py"
        ],

        5: [
            "python",
            r"Pilas\palindromo.py"
        ],

        6: [
            "python",
            r"Pilas\palabra_inversa.py"
        ],

        7: [
            "python",
            r"Pilas\eliminar_elemento.py"
        ],

        8: [
            "python",
            r"Pilas\cartas.py"
        ],

        9: [
            "python",
            r"Pilas\factorial.py"
        ],

        10: [
            "python",
            r"Pilas\insertar_atenea.py"
        ],

        11: [
            "python",
            r"Pilas\contar_vocales.py"
        ],

        12: [
            "python",
            r"Pilas\encontrar_personajes.py"
        ],

        13: [
            "python",
            r"Pilas\ironman.py"
        ],

        14: [
            "python",
            r"Pilas\insertar_ascendente.py"
        ],

        17: [
            "python",
            r"Pilas\separar_parrafo.py"
        ],
        
        18: [
            "python",
            r"Pilas\objetos_oficina.py"
        ],
        
        20: [
            "python",
            r"Pilas\pasos_robot.py"
        ],

        23: [
            "python",
            r"Pilas\temperatura_abril.py"
        ]
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

print("Bienvenido al sistema de ejercicios")
while (True):
    print("")
    opcion = input("Que ejercicios desea ver (Repaso o Pilas, 0 para salir): ").lower()
    if (opcion == "repaso"):
        print(lista_ejercicios_repaso)
        opcion = int(input("Escriba el numero del ejercicio que desea ejecutar: "))
        subprocess.run(ejercicios["Repaso"][opcion])
    elif (opcion == "pilas"):
        print(lista_ejercicios_pilas)
        opcion = int(input("Escriba el numero del ejercicio que desea ejecutar: "))
        subprocess.run(ejercicios["Pilas"][opcion])
    elif (opcion == "0"): break
        