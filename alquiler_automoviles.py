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

print("facturas")
print("si se facturan 0 kilometros entonces se emite:", factura_auto(0))
print("si se facturan 200 kilometros entonces se emite:", factura_auto(200))
print("si se facturan 400 kilometros entonces se emite:", factura_auto(400))
print("si se facturan 1000 kilometros entonces se emite:", factura_auto(1000))
print("si se facturan 1500 kilometros entonces se emite:", factura_auto(1500))