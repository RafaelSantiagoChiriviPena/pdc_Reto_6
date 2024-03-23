from math import pi 
def volumen_figura1 (radio1 : float , radio2 : float , altura : float) -> float:
    return ((4/3) * pi * (radio1**3)) + (pi * altura * (radio2**2))/3
def area_figura1 (radio1 : float , radio2 : float , altura : float) -> float:
    return 4 * pi * (radio1**2) + pi * radio2 * (radio2 + ((radio2**2 + altura**2)**0.5))
if __name__ == "__main__":
    try:
        radio1 = float(input("Por favor ingrese el radio de la esfera (cm): "))
        while radio1 < 0:
            radio1 = float(input("El valor ingresado no es valido, por favor ingrese un valor NO negativo"))
        radio2 = float(input("Por favor ingrese el radio de la base del cono (cm): "))
        while radio2 < 0:
            radio2 = float(input("El valor ingresado no es valido, por favor ingrese un valor NO negativo"))
        altura = float(input("Por favor ingrese la altura del cono (cm): "))
        while altura < 0:
            altura = float(input("El valor ingresado no es valido, por favor ingrese un valor NO negativo"))
        volumen = volumen_figura1 (radio1, radio2, altura)
        area = area_figura1 (radio1, radio2, altura)
        print("El volumen de la figura basada en los datos ingresados es de " ,volumen, " cm")
        print("Además, el área superficial de la figura es de " ,area, " cm")
    except ValueError:
        print("Lo ingresado no se trata de un numero real")