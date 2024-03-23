def precio_mandado (panes : int, bolsas_leche : int, huevos : int) -> int:
    precio = (300 * panes) + (3300 * bolsas_leche) + (350 * huevos)
    return precio
def vueltas_mandado (precio : int, plata : int) -> str:
    if plata - precio > 0:
        return print("Las vueltas son de $ " ,plata - precio)
    elif plata - precio == 0:
        return print("No ha sobrado dinero")
    else:
        return print("Queda debiendo $ " ,plata-precio)
if __name__ == "__main__":
    try:
        panes = int(input("¿Cuantos panes hay que comprar?: "))
        while panes < 0:
            panes = int(input("La cantidad ingresada no es valida, digite un valor NO negativo"))
        bolsas_leche = int(input("¿Cuantas bolsas de leche hay que comprar?: "))
        while bolsas_leche < 0:
            bolsas_leche = int(input("La cantidad ingresada no es valida, digite un valor NO negativo"))
        huevos = int(input("¿Cuantos huevos hay que comprar?: "))
        while huevos < 0:
            huevos = int(input("La cantidad ingresada no es valida, digite un valor NO negativo"))
        precio = precio_mandado(panes, bolsas_leche, huevos)
        print("El precio total del mandado es de $" ,precio, ", ¿Con cuánto paga?")
        plata = int(input("¿Con cuanto dinero cancela?"))
        vueltas = vueltas_mandado(precio, plata)
        print(vueltas)
    except ValueError:
        print("Lo ingresado no se trata de un numero entero")