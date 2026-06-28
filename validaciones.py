"""
MÓDULO TDA: Validaciones Artesanales de Entrada de Datos
Este módulo provee funciones de abstracción para controlar las entradas por teclado,
asegurando tipos de datos y formatos específicos sin romper la ejecución del programa.
"""

def validar_numero(mensaje):    
    """
    ABSTRACCIÓN: Solicita y devuelve un número entero válido.
    - Entrada: Un string con el mensaje para el usuario (ej: "Ingrese edad: ").
    - Salida: Un valor de tipo INT puro. No retorna hasta que la entrada sea válida.
    """
    while True:
        entrada = input(mensaje)
        try:
            # se aplica float para que no rechace valores como 3.0
            return int(float(entrada))
        except ValueError:
            print("Error: Debe ingresar un número entero válido (1, 10, -1, 0).")

def validar_numero_flotante(mensaje):
    """
    ABSTRACCIÓN: Solicita y devuelve un número flotante válido.
    - Entrada: Un string con el mensaje para el usuario (ej: "Ingrese precio: ").
    - Salida: Un valor de tipo FLOAT puro. No retorna hasta que la entrada sea válida.
    """
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print("Error: Debe ingresar un número decimal válido (ej: 3.14 o -2.5).")


def validar_caracter_especial(mensaje):
    """
    ABSTRACCIÓN: Solicita y devuelve un único carácter que sea especial.
    - Entrada: Un string con el mensaje para el usuario.
    - Salida: Un string de longitud 1 que NO contiene letras ni números.
    """
    while True:
        entrada = input(mensaje)
        largo = 0
        for _ in entrada:
            largo += 1
            
        if largo != 1:
            print("Error: Debe ingresar exactamente UN solo carácter.")
            continue
            
        caracter = entrada
        es_numero = '0' <= caracter <= '9'
        es_minuscula = 'a' <= caracter <= 'z'
        es_mayuscula = 'A' <= caracter <= 'Z'
        
        if not (es_numero or es_minuscula or es_mayuscula):
            return caracter
        else:
            print("Error: El carácter ingresado no es especial (es una letra o un número).")


def validar_string(mensaje):
    """
    ABSTRACCIÓN: Solicita y devuelve una cadena de texto alfabética.
    - Entrada: Un string con el mensaje para el usuario.
    - Salida: Un string que solo contiene letras y/o espacios (no vacío).
    """
    while True:
        entrada = input(mensaje)
        if entrada == "":
            print("Error: El campo no puede quedar vacío.")
            continue
            
        es_texto_puro = True
        solo_espacios = True
        
        for caracter in entrada:
            es_letra = ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z')
            es_espacio = (caracter == ' ')
            
            if not es_espacio:
                solo_espacios = False
                
            if not (es_letra or es_espacio):
                es_texto_puro = False
                break
                
        if solo_espacios:
            print("Error: El campo no puede contener únicamente espacios vacíos.")
            continue
            
        if es_texto_puro:
            return entrada
        else:
            print("Error: El texto solo debe contener letras y espacios.")


def validar_contrasenia(mensaje):
    """
    ABSTRACCIÓN: Solicita y devuelve una clave con un patrón de seguridad estricto.
    - Entrada: Un string con el mensaje para el usuario.
    - Salida: Un string de exactamente 8 caracteres que cumple con:
              4 letras (1 de ellas mayúscula), 3 números y 1 carácter especial.
    """
    while True:
        clave = input(mensaje)
        largo = 0
        for _ in clave:
            largo += 1
            
        if largo != 8:
            print("Error: La contraseña debe tener exactamente 8 caracteres.")
            continue
            
        cant_mayusculas = 0
        cant_letras = 0
        cant_numeros = 0
        cant_especiales = 0
        
        for caracter in clave:
            if '0' <= caracter <= '9':
                cant_numeros += 1
            elif 'a' <= caracter <= 'z':
                cant_letras += 1
            elif 'A' <= caracter <= 'Z':
                cant_letras += 1
                cant_mayusculas += 1
            else:
                cant_especiales += 1
                
        # --- CONTROL DE LAS NUEVAS DIMENSIONES ---
        if cant_letras != 4:
            print(f"Error: Debe tener exactamente 4 letras (detectadas: {cant_letras}).")
            continue
        if cant_mayusculas != 1:
            print(f"Error: Debe tener exactamente 1 letra mayúscula (detectadas: {cant_mayusculas}).")
            continue
            
        # CORREGIDO: Ahora evalúa que sean exactamente 3 números
        if cant_numeros != 3:
            print(f"Error: Debe tener exactamente 3 números (detectados: {cant_numeros}).")
            continue
            
        if cant_especiales != 1:
            print(f"Error: Debe tener exactamente 1 carácter especial (detectados: {cant_especiales}).")
            continue
            
        return clave