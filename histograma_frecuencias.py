def frecuencia_letras(frase):
    letras = {}
    
    for letra in frase:
        if (letra not in letras.keys()):
            letras[letra] = 1
        else:
            letras[letra] += 1
            
    for k, v in letras.items():
        print(f"Letra {k}: {'#' * v}")

print("frecuencia de letras")
frecuencia_letras("manolo")