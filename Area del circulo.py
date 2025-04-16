import math

def circulito(radio):
    if radio <= 0:
        return  " ingresa un numero positivo: :)"
    
    area_del_circulo = math.pi * radio ** 2
    diametro_del_circulo = 2 * math.pi * radio
    return f"Área: {area_del_circulo:.2f}, Perímetro: {diametro_del_circulo:.2f}"


radio_usuario = float(input("Teclea el radio de tu circulo: "))
resultado_del_circulo = circulito(radio_usuario)
print(resultado_del_circulo)