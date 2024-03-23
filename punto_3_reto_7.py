def kilos_aves (gallinas : int, gallos : int, pollitos : int) -> int:
    return (gallinas * 6) + (gallos * 7) + (pollitos)
if __name__ == "__main__":
    try:
        gallinas = int(input("Ingrese el numero de gallinas: "))
        while gallinas < 0:
            gallinas = int(input("La cantidad ingresada no es valida, digite un valor NO negativo"))
        gallos = int(input("Ingrese el numero de gallos: "))
        while gallos < 0:
            gallos = int(input("La cantidad ingresada no es valida, digite un valor NO negativo"))
        pollitos = int(input("Ingrese el numero de pollitos: "))
        while pollitos < 0:
            pollitos = int(input("La cantidad ingresada no es valida, digite un valor NO negativo"))
        kilos_carne = kilos_aves(gallinas, gallos, pollitos)
        print("Los kilos de carne resultantes de " ,gallinas, " gallinas, " ,gallos, " gallos y " ,pollitos, " pollitos es de " ,kilos_carne, " kg")
    except ValueError:
        print("Lo ingresado no se trata de un numero entero")