def cuadrado(ladoa):
    if ladoa <= 0:
        return "Solo puedes ingresar números positivos :-B"

    calculo_del_cuadrado = ladoa ** 2
    return f"El área del cuadrado es: {calculo_del_cuadrado:.2f}"

ladoa_del_cuadrado = float(input("Ingresa el primer lado del cuadrado: "))

resultado_del_cuadrado = cuadrado(ladoa_del_cuadrado)
print(resultado_del_cuadrado)
