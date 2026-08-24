import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import limpiar
from validaciones import validar_numero

def suma_recursiva(numero):
    if (numero == 0):
        return numero
    else:
        return numero + suma_recursiva(numero - 1)

# -- main
limpiar()

input = validar_numero("Ingrese un numero para realizar la suma recursiva: ")

print(f"La suma recursiva de {input} es: {suma_recursiva(input)}")