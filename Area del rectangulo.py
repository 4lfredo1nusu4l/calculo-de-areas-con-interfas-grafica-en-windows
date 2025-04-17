def rectangulo(ladoa, ladob):
    if ladoa <= 0 or ladob <= 0:
        return "Solo puedes ingresar números positivos :-B"

    calculo_del_rectangulo = ladoa * ladob
    return f"El área del rectangulo es: {calculo_del_rectangulo:.2f}"

# Pedir datos al usuario
ladoa_del_rectangulo = float(input("Ingresa la base del rectangulo: "))
ladob_del_rectangulo = float(input("Ingresa la altura del rectangulo: "))

# Llamar la función
resultado_del_rectangulo = rectangulo(ladoa_del_rectangulo, ladob_del_rectangulo)
print(resultado_del_rectangulo)
 