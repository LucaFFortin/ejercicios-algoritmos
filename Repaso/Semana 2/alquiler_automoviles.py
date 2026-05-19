def factura_auto(kilometros):
    if (kilometros <= 0):
        return "Cantidad de kilometros erronea"
    elif (kilometros > 0 and kilometros < 300):
        return 5000
    elif (kilometros > 300 and kilometros <= 1000):
        # Error corregido: el código original usa kilometros_extra
        kilometros_extra = kilometros - 300
        return 5000 + (30 * kilometros_extra)
    elif (kilometros > 1000):
        kilometros_a_facturar = kilometros - 300
        kilometros_segundo_tramo = kilometros_a_facturar - 700
        kilometros_primer_tramo = kilometros_a_facturar - kilometros_segundo_tramo
        return 5000 + (kilometros_primer_tramo * 30) + (kilometros_segundo_tramo * 50)

# main
entrada = int(input("Ingrese la cantidad de kilometros a facturar: "))
print(factura_auto(entrada))