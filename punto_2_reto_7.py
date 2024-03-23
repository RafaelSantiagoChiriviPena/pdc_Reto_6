from math import pi 
def area_figura2 (radio : float, base : float, alto : float) -> float :
    return 2*(pi * (radio**2)) + (base * alto)
def perimetro_figura2 (radio : float, base : float, alto : float) -> float:
    return 2(2 * pi * radio) + (2 * base + 2 * alto)
if __name__ == "__main__":
    try:
        radio = float(input("Por favor ingrese el radio de los circulos (cm):"))
        while radio < 0:
            radio = float(input("El valor ingresado no es valido, por favor ingrese un valor NO negativo"))
        base = float(input("Por favor ingrese la base del rectangulo (cm):"))
        while base < 0:
            base = float(input("El valor ingresado no es valido, por favor ingrese un valor NO negativo"))
        alto = float(input("Por favor ingrese la altura del rectangulo (cm):"))
        while alto < 0:
            alto = float(input("El valor ingresado no es valido, por favor ingrese un valor NO negativo"))
        area = area_figura2(radio, base, alto)
        perimetro = perimetro_figura2(radio, base, alto)
        print("El area de la figura basada en los datos ingresados es de " ,area, " cm")
        print("Además. el perímetro de la figura es de " ,perimetro, " cm")
    except ValueError:
        print("Lo ingresado no se trata de un numero real")