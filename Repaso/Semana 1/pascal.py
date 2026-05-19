"""
Función para calcular el triángulo de Pascal.
Dado un cierto nivel, calculará siempre y cuando
level sea un número entre 0 y 25.
"""
def pascal_triangle(level=2):
    # Validación de tipo
    if not isinstance(level, int):
        print("El parametro level tiene que ser un numero")
        return

    # Validación de rango
    if level <= 0:
        print("El nivel ingresado es imposible de calcular")
        return

    if level > 25:
        print("El nivel excede el limite de 25, la ejecucion se cancelo")
        return

    first_level = [1]
    second_level = [1, 1]

    prev_level = second_level

    print_level(first_level)

    if level <= 1:
        return

    print_level(second_level)

    if level <= 2:
        return

    # Generar los siguientes niveles
    for _ in range(level - 2):
        curr_level = calculate_level(prev_level)
        print_level(curr_level)
        prev_level = curr_level


# Imprime el nivel con números espaciados
def print_level(level):
    print(" ".join(map(str, level)))

# Calcula el siguiente nivel según el nivel previo
def calculate_level(prev_level):

    level = []

    for i in range(len(prev_level) + 1):

        curr = prev_level[i] if i < len(prev_level) else None
        prev = prev_level[i - 1] if i - 1 >= 0 else None

        # Primera iteración
        if prev is None:
            level.append(curr)

        # Última iteración
        elif curr is None:
            level.append(prev)

        # Suma de elementos intermedios
        else:
            level.append(curr + prev)

    return level

# main
size = int(input("Ingrese el tamaño que desea del triangulo: "))
pascal_triangle(size)