import math

def calculo_de_poligonos(base,altura,lados):
    if base <= 0 or altura <= 0 or lados <= 0:
        print("No puede ser menor a 0, ingrese otro numero")
    poligonoa = base * altura / 2
    poligonob = poligonoa * lados
    return f"Area: {poligonob:.3f} "
    
def rectangulo(ladoa, ladob):
    if ladoa <= 0 or ladob <= 0:
        return "Solo puedes ingresar números positivos :-B"

    calculo_del_rectangulo = ladoa * ladob
    return f"El área del rectangulo es: {calculo_del_rectangulo:.2f}"
 

def circulito(radio):
    if radio <= 0:
        return  " ingresa un numero positivo: :)"
    
    area_del_circulo = math.pi * radio ** 2
    diametro_del_circulo = 2 * math.pi * radio
    return f"Área: {area_del_circulo:.2f}, Perímetro: {diametro_del_circulo:.2f}"


def triangulo(base,altura):
    if base <= 0 or altura <= 0:
        print("Solo puedes usar numeros postivos :-)")
    
    calculo_triangulo = (base * altura) / 2
    return f"El área del triángulo es: {calculo_triangulo:.2f}"

#menu de los datos
print("Introdusca la opcion prsionando los numeros: ")
print("1.Poligonos(exagono.pentagono.etc...)")
print("2.Rectangulo")
print("3.Circulo")
print("4.Triangulo")
print("5.Cuadrado")

opcion = int(input("Elige una entre 1-4: "))

match opcion:
    
    case 1: #poligonos
        b = float(input("Ingresa la base de un lado del polígono: "))
        a = float(input("Ingresa la altura de un triángulo del polígono: "))
        l = int(input("Ingresa el número de lados del polígono: "))
        print(calculo_de_poligonos(b, a, l))
    
    case 2: #rectangulo
        b = float(input("Ingresa la base de el rectangulo: "))
        h = float(input("Ingresa la altura de el rectangulo: "))
        print(rectangulo(b, h))
    case 3: #circulo
        r = float(input("Ingresa el radio del circulo: "))
        print(circulito(r))
        
    case 4: #triangulo
        b = float(input("Ingresa la base del triangulo: "))
        h = float(input("Ingresa la altura del triangulo: "))
        print(triangulo(b, h))
        
        