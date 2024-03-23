# pdc_Reto_6
### Soy Rafael Santiago Chirivi Peña y pertenezco al grupo de "Fenomenoides", adelante se muestra nuestro logo 

<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>

### A continuacion, se muestran las soluciones propuestas a los distintos puntos de este reto

1. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/FKBsrHTV/IMG-20240322-WA0066.jpg" alt="IMG-20240322-WA0066"/></a><br/><br/>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el volumen y el área superficial.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

```python
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
```

2. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/FsLF9vSj/IMG-20240322-WA0067.jpg" alt="IMG-20240322-WA0067"/></a><br/><br/>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

```python
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
```

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
```python
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
```

4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a  3300 cada una y H huevos a  350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
```python
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
```

5. Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.
```python
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
```

6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
```python
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
```

7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número
```python
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
```

9. Consultar qué es y cómo funciona *pip* en python.
pip es el sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python.

10. Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.
