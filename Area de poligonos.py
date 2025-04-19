def calculo_de_poligonos(base,altura,lados):
    if base >= 0 or altura >= 0 or lados >= 0:
        print("No puede ser menor a 0, ingrese otro numero")
    poligonoa = base * altura / 2
    poligonob = poligonoa * lados
    return f"Area: {poligonob:.3f} "
    
base_poligono = float(input("Ingrese la base de un lado del poligono: "))
altura_poligono = float(input("Ingresa la altura de un lado del poligono: "))
numero_de_lados_poligono = float(input("Ingresa el numero de lados del poligono: "))

resultado_del_poligono = calculo_de_poligonos(base_poligono,altura_poligono,numero_de_lados_poligono)
print(resultado_del_poligono)