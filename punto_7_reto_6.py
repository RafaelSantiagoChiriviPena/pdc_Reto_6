from  punto_7_reto_6_funciones import promedio, promedio_multiplicativo, orden_ascendente, orden_descendente, mayor_potencia_menor, raiz_cubica_menor, mediana

if __name__ == "__main__":
    try:
        num1 : float = float(input("Ingrese el primer numero real: "))
        num2 : float = float(input("Ingrese el segundo numero real: "))
        num3 : float = float(input("Ingrese el tercer numero real: "))
        num4 : float = float(input("Ingrese el cuarto numero real: "))
        num5 : float = float(input("Ingrese el quinto y ultimo numero real: "))
        prom = promedio (num1, num2, num3, num4, num5)
        prom_mult = promedio_multiplicativo (num1, num2, num3, num4, num5)
        descendente = orden_descendente (num1, num2, num3, num4, num5)
        ascendente = orden_ascendente (descendente)
        potencia = mayor_potencia_menor (ascendente)
        raiz = raiz_cubica_menor (ascendente)
        med = mediana (ascendente)
        print(f"el promedio de los numeros ingresados es de {prom}")
        print(f"la mediana, el termino de la 'mitad' se trata de {med}")
        print(f"el promedio multiplicativo de los valores ingresados es {prom_mult}")
        print(f"El orden de los datos ingresados de manera ascendente es de {ascendente}")
        print(f"El orden de los datos ingresados de manera descendente es de {descendente}")
        print(f"El resultado de elevar el termino mayor al termino menor de los datos es de {potencia}")
        print(f"El resultado de la raiz cubica del termino menor se trata de {raiz}")
    except ValueError:
        print("Los valores ingresados no corresponden a numeros reales")