import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import limpiar
from validaciones import validar_string, validar_numero


def sucesion_recursiva(num):
    if (num == 1): return 3
    else:
        return sucesion_recursiva(num - 1) + (2 * num)


# main
limpiar()

numero = validar_numero("Ingrese un numero para calcular la sucesion: ")

print(f"La sucesion recursiva de {numero} es igual a: {sucesion_recursiva(numero)}")