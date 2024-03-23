def promedio (num1 : float, num2 : float, num3 : float, num4 : float, num5 : float) -> float:
    return (num1 + num2 + num3 + num4 + num5) / 5



def promedio_multiplicativo (num1 : float, num2 : float, num3 : float, num4 : float, num5 : float) -> float:
    return (num1 * num2 * num3 * num4 * num5) ** 0.5


def orden_descendente (num1 : float, num2 : float, num3 : float, num4 : float, num5 : float) -> list:
    lista_numerica = []
    if num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5 or num2 == num3 or num2 == num4 or num2 == num5 or num3 == num4 or num3 == num5 or num4 == num5:
        lista_numerica = ['Los valores no pueden ser iguales entre si, intentelo de nuevo']
    if num1 > num2 > num3 > num4 > num5:
        lista_numerica = [num1, num2, num3, num4, num5]
    if num1 > num2 > num3 > num5 > num4:
        lista_numerica = [num1, num3, num2, num5, num4]
    if num1 > num2 > num4 > num3 > num5:
        lista_numerica = [num1, num2, num4, num3, num5]
    if num1 > num2 > num4 > num5 > num3:
        lista_numerica = [num1, num5, num3, num4, num2]
    if num1 > num2 > num5 > num3 > num4:
        lista_numerica = [num1, num2, num5, num3, num4]
    if num1 > num2 > num3 > num4 > num5:
        lista_numerica = [num1, num2, num3, num4, num5]
    if num1 > num3 > num2 > num4 > num5:
        lista_numerica = [num1, num3, num2, num4, num5]
    if num1 > num3 > num2 > num5 > num4:
        lista_numerica = [num1, num3, num2, num5, num4]
    if num1 > num3 > num4 > num2 > num5:
        lista_numerica = [num1, num3, num4, num2, num5]
    if num1 > num3 > num4 > num5 > num2:
        lista_numerica = [num1, num3, num4, num5, num2]
    if num1 > num3 > num5 > num2 > num4:
        lista_numerica = [num1, num3, num5, num2, num4]
    if num1 > num3 > num5 > num4 > num2:
        lista_numerica = [num1, num3, num5, num2, num4]
    if num1 > num4 > num2 > num3 > num5:
        lista_numerica = [num1, num4, num2, num3, num5]
    if num1 > num4 > num2 > num5 > num3:
        lista_numerica = [num1, num4, num2, num5, num3]
    if num1 > num4 > num3 > num2 > num5:
        lista_numerica = [num1, num4, num3, num2, num5]
    if num1 > num4 > num3 > num5 > num2:
        lista_numerica = [num1, num4, num3, num5, num2]
    if num1 > num4 > num5 > num2 > num3:
        lista_numerica = [num1, num4, num5, num2, num3]
    if num1 > num4 > num5 > num3 > num2:
        lista_numerica = [num1, num4, num5, num3, num2]
    if num1 > num5 > num2 > num3 > num4:
        lista_numerica = [num1, num5, num2, num3, num4]
    if num1 > num5 > num2 > num4 > num3:
        lista_numerica = [num1, num5, num2, num4, num3]
    if num1 > num5 > num3 > num2 > num4:
        lista_numerica = [num1, num5, num3, num2, num4]
    if num1 > num5 > num3 > num4 > num2:
        lista_numerica = [num1, num5, num3, num4, num2]
    if num1 > num5 > num4 > num2 > num3:
        lista_numerica = [num1, num5, num4, num2, num3]
    if num1 > num5 > num4 > num3 > num2:
        lista_numerica = [num1, num5, num4, num3, num2] 
    if num2 > num1 > num3 > num4 > num5:
        lista_numerica = [num2, num1, num3, num4, num5]
    if num2 > num1 > num3 > num5 > num4:
        lista_numerica = [num2, num1, num3, num5, num4]
    if num2 > num1 > num4 > num3 > num5:
        lista_numerica = [num2, num1, num4, num3, num5]
    if num2 > num1 > num4 > num5 > num3:
        lista_numerica = [num2, num1, num4, num5, num3]
    if num2 > num1 > num5 > num3 > num4:
        lista_numerica = [num2, num1, num5, num3, num4]
    if num2 > num1 > num5 > num4 > num3:
        lista_numerica = [num2, num1, num5, num4, num3]
    if num2 > num3 > num1 > num4 > num5:
        lista_numerica = [num2, num3, num1, num4, num5]
    if num2 > num3 > num1 > num5 > num4:
        lista_numerica = [num2, num3, num1, num5, num4]
    if num2 > num3 > num4 > num1 > num5:
        lista_numerica = [num2, num3, num4, num1, num5]
    if num2 > num3 > num4 > num5 > num1:
        lista_numerica = [num2, num3, num4, num5, num1]
    if num2 > num3 > num5 > num1 > num4:
        lista_numerica = [num2, num3, num5, num1, num4]
    if num2 > num3 > num5 > num4 > num1:
        lista_numerica = [num2, num3, num5, num4, num1]
    if num2 > num4 > num1 > num3 > num5:
        lista_numerica = [num2, num4, num1, num3, num5]
    if num2 > num4 > num1 > num5 > num3:
        lista_numerica = [num2, num4, num1, num5, num3]
    if num2 > num4 > num3 > num1 > num5:
        lista_numerica = [num2, num4, num3, num1, num5]
    if num2 > num4 > num3 > num5 > num1:
        lista_numerica = [num2, num4, num3, num5, num1]
    if num2 > num4 > num5 > num1 > num3:
        lista_numerica = [num2, num4, num5, num1, num3]
    if num2 > num4 > num5 > num3 > num1:
        lista_numerica = [num2, num4, num5, num3, num1]
    if num2 > num5 > num1 > num3 > num4:
        lista_numerica = [num2, num5, num1, num3, num4]
    if num2 > num5 > num1 > num4 > num3:
        lista_numerica = [num2, num5, num1, num4, num3]
    if num2 > num5 > num3 > num1 > num4:
        lista_numerica = [num2, num5, num3, num1, num4]
    if num2 > num5 > num3 > num4 > num1:
        lista_numerica = [num2, num5, num1, num3, num4]
    if num2 > num5 > num4 > num1 > num3:
        lista_numerica = [num2, num5, num4, num1, num3]
    if num2 > num5 > num4 > num3 > num1:
        lista_numerica = [num2, num5, num4, num3, num1]
    if num3 > num1 > num2 > num4 > num5:
        lista_numerica = [num3, num1, num2, num4, num5]
    if num3 > num1 > num2 > num5 > num4:
        lista_numerica = [num3, num1, num2, num5, num4]
    if num3 > num1 > num4 > num2 > num5:
        lista_numerica = [num3, num1, num4, num2, num5]
    if num3 > num1 > num4 > num5 > num2:
        lista_numerica = [num3, num1, num4, num5, num2]
    if num3 > num1 > num5 > num2 > num4:
        lista_numerica = [num3, num1, num5, num2, num4]
    if num3 > num1 > num5 > num4 > num2:
        lista_numerica = [num3, num1, num5, num4, num2]   
    if num3 > num2 > num1 > num4 > num5:
        lista_numerica = [num3, num2, num1, num4, num5]
    if num3 > num2 > num1 > num5 > num4:
        lista_numerica = [num3, num2, num1, num5, num4]
    if num3 > num2 > num4 > num1 > num5:
        lista_numerica = [num3, num2, num4, num1, num5]        
    if num3 > num2 > num4 > num5 > num1:
        lista_numerica = [num3, num2, num4, num5, num1]
    if num3 > num2 > num5 > num1 > num4:
        lista_numerica = [num3, num2, num5, num1, num4]
    if num3 > num2 > num5 > num4 > num1:
        lista_numerica = [num3, num2, num5, num4, num1]  
    if num3 > num4 > num1 > num2 > num5:
        lista_numerica = [num3, num4, num1, num2, num5]  
    if num3 > num4 > num1 > num5 > num2:
        lista_numerica = [num3, num4, num1, num5, num2]
    if num3 > num4 > num2 > num5 > num1:
        lista_numerica = [num3, num4, num2, num5, num1] 
    if num3 > num4 > num2 > num1 > num5:
        lista_numerica = [num3, num4, num2, num1, num5] 
    if num3 > num4 > num5 > num1 > num2:
        lista_numerica = [num3, num4, num5, num1, num2] 
    if num3 > num4 > num5 > num2 > num1:
        lista_numerica = [num3, num4, num5, num2, num1] 
    if num3 > num5 > num1 > num2 > num4:
        lista_numerica = [num3, num5, num1, num2, num4]
    if num3 > num5 > num1 > num4 > num2:
        lista_numerica = [num3, num5, num1, num4, num2]
    if num3 > num5 > num2 > num1 > num4:
        lista_numerica = [num3, num5, num2, num1, num4]
    if num3 > num5 > num2 > num4 > num1:
        lista_numerica = [num3, num5, num1, num2, num4]
    if num3 > num5 > num4 > num1 > num2:
        lista_numerica = [num3, num5, num4, num1, num2]
    if num3 > num5 > num4 > num2 > num1:
        lista_numerica = [num3, num5, num4, num2, num1]
    if num4 > num1 > num2 > num3 > num5:
        lista_numerica = [num4, num1, num2, num3, num5]
    if num4 > num1 > num2 > num5 > num3:
        lista_numerica = [num4, num1, num2, num5, num3]
    if num4 > num1 > num3 > num2 > num5:
        lista_numerica = [num4, num1, num3, num2, num5]
    if num4 > num1 > num3 > num5 > num2:
        lista_numerica = [num4, num1, num3, num5, num2]
    if num4 > num1 > num5 > num2 > num3:
        lista_numerica = [num4, num1, num5, num2, num3]
    if num4 > num1 > num5 > num3 > num2:
        lista_numerica = [num4, num1, num5, num3, num2]
    if num4 > num2 > num1 > num3 > num5:
        lista_numerica = [num4, num2, num1, num3, num5]
    if num4 > num2 > num1 > num5 > num3:
        lista_numerica = [num4, num2, num1, num5, num3]
    if num4 > num2 > num3 > num1 > num5:
        lista_numerica = [num4, num2, num3, num1, num5]
    if num4 > num2 > num3 > num5 > num1:
        lista_numerica = [num4, num2, num1, num3, num5]
    if num4 > num2 > num5 > num1 > num3:
        lista_numerica = [num4, num2, num5, num1, num3]
    if num4 > num2 > num5 > num3 > num1:
        lista_numerica = [num4, num2, num5, num3, num1]
    if num4 > num3 > num1 > num2 > num5:
        lista_numerica = [num4, num3, num1, num2, num5]
    if num4 > num3 > num1 > num5 > num2:
        lista_numerica = [num4, num3, num1, num5, num2]
    if num4 > num3 > num2 > num1 > num5:
        lista_numerica = [num4, num3, num2, num1, num5]
    if num4 > num3 > num2 > num5 > num1:
        lista_numerica = [num4, num3, num2, num5, num1]
    if num4 > num3 > num5 > num1 > num2:
        lista_numerica = [num4, num3, num5, num1, num2]
    if num4 > num3 > num5 > num2 > num1:
        lista_numerica = [num4, num3, num5, num2, num1]
    if num4 > num5 > num1 > num2 > num3:
        lista_numerica = [num4, num5, num1, num2, num3]
    if num4 > num5 > num1 > num3 > num2:
        lista_numerica = [num4, num5, num1, num3, num2]
    if num4 > num5 > num2 > num1 > num3:
        lista_numerica = [num4, num5, num2, num1, num3]
    if num4 > num5 > num2 > num3 > num1:
        lista_numerica = [num4, num5, num2, num3, num1]
    if num4 > num5 > num3 > num1 > num2:
        lista_numerica = [num4, num5, num3, num1, num2]
    if num4 > num5 > num3 > num2 > num1:
        lista_numerica = [num4, num5, num3, num2, num1]
    if num5 > num1 > num2 > num3 > num4:
        lista_numerica = [num5, num1, num2, num3, num4]
    if num5 > num1 > num2 > num4 > num3:
        lista_numerica = [num5, num1, num2, num4, num3]
    if num5 > num1 > num3 > num2 > num4:
        lista_numerica = [num5, num1, num3, num2, num4]
    if num5 > num1 > num3 > num4 > num2:
        lista_numerica = [num5, num1, num3, num4, num2]
    if num5 > num1 > num4 > num2 > num3:
        lista_numerica = [num5, num1, num4, num2, num3]
    if num5 > num1 > num4 > num3 > num2:
        lista_numerica = [num5, num1, num4, num3, num2]
    if num5 > num2 > num1 > num3 > num4:
        lista_numerica = [num5, num2, num1, num3, num4]
    if num5 > num2 > num1 > num4 > num3:
        lista_numerica = [num5, num2, num1, num4, num3]
    if num5 > num2 > num3 > num1 > num4:
        lista_numerica = [num5, num2, num3, num1, num4]
    if num5 > num2 > num3 > num4 > num1:
        lista_numerica = [num5, num2, num3, num4, num1]
    if num5 > num2 > num4 > num1 > num3:
        lista_numerica = [num5, num2, num4, num1, num3]
    if num5 > num2 > num4 > num3 > num1:
        lista_numerica = [num5, num2, num4, num3, num1]  
    if num5 > num3 > num1 > num2 > num4:
        lista_numerica = [num5, num3, num1, num2, num4] 
    if num5 > num3 > num1 > num4 > num2:
        lista_numerica = [num5, num3, num1, num4, num2]
    if num5 > num3 > num2 > num1 > num4:
        lista_numerica = [num5, num3, num2, num1, num4]  
    if num5 > num3 > num2 > num4 > num1:
        lista_numerica = [num5, num3, num2, num4, num1]
    if num5 > num3 > num4 > num1 > num2:
        lista_numerica = [num5, num3, num4, num1, num2] 
    if num5 > num3 > num3 > num2 > num1:
        lista_numerica = [num5, num3, num4, num2, num1] 
    if num5 > num4 > num1 > num2 > num3:
        lista_numerica = [num5, num4, num1, num2, num3]
    if num5 > num4 > num1 > num3 > num2:
        lista_numerica = [num5, num4, num1, num3, num2]
    if num5 > num4 > num2 > num1 > num3:
        lista_numerica = [num5, num4, num2, num1, num3]  
    if num5 > num4 > num2 > num3 > num1:
        lista_numerica = [num5, num4, num2, num3, num1]
    if num5 > num4 > num3 > num1 > num2:
        lista_numerica = [num5, num4, num3, num1, num2]
    if num5 > num4 > num3 > num2 > num1:
        lista_numerica = [num5, num4, num3, num2, num1]   
    return lista_numerica



def orden_ascendente (lista_numerica : list) -> list:
    lista_numerica = lista_numerica [::-1]
    return lista_numerica

def mediana (lista_numeritca : list) -> float:
    med = float(lista_numeritca[2])
    return med


def mayor_potencia_menor (lista_numerica : list) -> float:
    potencia = float(lista_numerica[4]) ** float(lista_numerica[0])
    return potencia

def raiz_cubica_menor (lista_numerica : list) -> float:
    raiz_cubica = float(lista_numerica[0]) ** (1/3)
    return raiz_cubica
    