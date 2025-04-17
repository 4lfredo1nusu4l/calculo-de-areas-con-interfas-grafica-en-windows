def triangulo(base,altura):
    if base <= 0 or altura <= 0:
        print("Solo puedes usar numeros postivos :-)")
    
    calculo_triangulo = (base * altura) / 2
    return f"El área del triángulo es: {calculo_triangulo:.2f}"


base_del_triangulo = float(input("Ingresa la base del triangulo: "))
altura_del_triangulo = float(input("Ingresa la altura del triangulo: "))

resultado_del_triangulo = triangulo(base_del_triangulo, altura_del_triangulo)
print(resultado_del_triangulo)