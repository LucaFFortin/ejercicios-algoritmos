import os
import subprocess
import math

def limpiar():
    """limpia la pantalla utilizando el comando 'clear' segun el sistema operativo."""
    subprocess.run(['cmd', '/c', 'cls'] if os.name == 'nt' else ['clear'])

def es_primo(n):
    """Calcula si un numero es primo y retorna un booleano que indica si es o no es."""
    if (n == 1): return False
    
    base = math.sqrt(n)
    contador = math.floor(base)
    
    while (contador >= 2):
        if (n % contador == 0):
            return False
        contador -= 1
    return True