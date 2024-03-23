t : float = 12
C : float = 100
I : float = 1

def tiempo (meses : int) -> float:
    temp = (meses / t)
    return temp
def interes (inversion : float, tasa_interes : float) -> float:
    interes = inversion * (I + (tasa_interes/C))
    return interes

if __name__ == "__main__":
    try:
        inversion : float = float(input("Por favor ingrese el valor de su inversion inicial: "))
        while inversion < 0:
            inversion : float = float(input("No es posible hacer una inversion negativa, por favor intentelo de nuevo: "))

        meses : int = int(input("Por favor ingrese el tiempo para este prestamo en meses: "))
        while meses < 0:
            meses : int = int(input("No existe tiempo negativo, por favor intentelo de nuevo: "))

        inter : float = float(input("ingrese el valor de la tasa de interes, sin el por ciento (%): "))
        while inter < 0:
            inter : float = float(input("No es valido un porcentaje negativo, ingrese el valor de la tasa de interes, sin el por ciento (%): "))
        total = interes (inversion, inter) ** tiempo(meses)
        print(f"El prestamo tendra como resultado ${total} durante un tiempo de {meses} meses")
        
    except ValueError:
        print("El valor ingresado no se trata de un numero real")