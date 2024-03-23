def contagiados (dias : int , enfermos : int) -> int:
    return enfermos * (2 ** dias)
if __name__ == "__main__":
    try:
        enfermos = int(input("¿Cuantos enfermos de covid-19 hay actualmente en Nuncalandia?"))
        dias = int(input("¿Cuantos dias pasaran?"))
        while dias < 0:
            dias = int(input("La cantidad de dias ingresados no es valida, por favor ingrese un valor positivo"))
        estimacion_enfermos = contagiados(dias, enfermos)
        print("Pasados " ,dias, " dias, la cantidad de enfermos habra pasado de " ,enfermos, " a " ,estimacion_enfermos,)
    except ValueError:
        print("El valor ingresado no es un numero entero")