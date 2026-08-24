import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import limpiar
from validaciones import validar_numero


def potencia_recursiva(base, exp):
    if (exp == 0): return 1
    elif (exp == 1): return base
    else:
        return base * potencia_recursiva(base, exp - 1)

# main

limpiar()

base = validar_numero("Ingrese el numero base: ")
exponente = validar_numero("Ingrese el exponente de la base: ")

print(f"El valor de {base} elevado {exponente} es: {potencia_recursiva(base=base, exp=exponente)}")