import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import limpiar
from validaciones import validar_numero

def serie_recursiva(numero):
    if (numero < 0): numero = abs(numero)
    if (numero > 100): return "Valor maximo excedido, solo puede ingresar un numero menor o igual a 100"
    if (numero <= 1): return numero
    else: return serie_recursiva(numero - 1) + 1 / numero

# main
limpiar()

numero = validar_numero("Ingrese el valor final de la serie armonica: ")

print(f"Con el valor final {numero}, la serie armonica queda asi: {serie_recursiva(numero=numero)}.")
