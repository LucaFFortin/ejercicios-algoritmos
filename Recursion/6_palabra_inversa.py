import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import limpiar
from validaciones import validar_string

def invertir_palabra_recursivo(palabra: str):
    if (len(palabra) == 1): return palabra
    else: return palabra[-1] + invertir_palabra_recursivo(palabra[:-1])

# main

palabra = validar_string("Ingrese la palabra a invertir: ")

print(f"{palabra} quedo como {invertir_palabra_recursivo(palabra=palabra)}")