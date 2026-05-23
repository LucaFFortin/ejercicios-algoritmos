def separar_parrafo(parrafo):
    cont_vocales = 0
    cont_consonantes = 0
    cont_simbolos = 0
    cont_espacios = 0
    cont_numeros = 0

    vocales = [
        'a', 'e', 'i', 'o', 'u',
        'A', 'E', 'I', 'O', 'U',
        'á', 'é', 'í', 'ó', 'ú',
        'Á', 'É', 'Í', 'Ó', 'Ú',
        'ü', 'Ü'
    ]
    
    consonantes = [
        'b','c','d','f','g','h','j','k','l','m',
        'n','ñ','p','q','r','s','t','v','w','x','y','z',
        'B','C','D','F','G','H','J','K','L','M',
        'N','Ñ','P','Q','R','S','T','V','W','X','Y','Z'
    ]

    simbolos = [
        ' ', '.', ',', ';', ':',
        '¿', '?', '¡', '!',
        '(', ')', '[', ']', '{', '}',
        '-', '_', '"', "'",
        '/', '\\', '@', '#', '$', '%',
        '&', '*', '+', '=',
        '<', '>', '|', '~', '^',
        '`', '\n', '\t'
    ]

    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    for caracter in parrafo:
        if (caracter in vocales): cont_vocales += 1
        elif (caracter in consonantes): cont_consonantes += 1
        if (caracter in simbolos): cont_simbolos += 1
        if (caracter == " "): cont_espacios += 1
        elif (caracter in numeros): 
            cont_numeros += 1
            print("caracter: ",caracter)
    
    print(f"La cantidad de vocales es de {cont_vocales} vocales")
    print(f"La cantidad de consonantes es de {cont_consonantes} consonantes")
    print(f"La cantidad de simbolos es de {cont_simbolos} simbolos")
    print(f"La cantidad de espacios es de {cont_espacios} espacios")
    porcentaje_vocales = cont_vocales/cont_consonantes * 100
    print(f"El porcentaje de vocales con respecto a las consonantes es de {porcentaje_vocales}%")
    print(f"La cantidad de numeros es de {cont_espacios} numeros")

separar_parrafo("hola soy luca")