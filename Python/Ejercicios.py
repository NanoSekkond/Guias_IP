from math import *

#Ejercicio 1
#Ejercicio 1.1
def raizDe2() -> float:
    x: float = sqrt(2)
    x = round(x,4)
    return x

#Ejercicio 1.2
def imprimirHola():
    print ("hola")

#Ejercicio 1.3
def imprimir_un_verso():
    print ("As branches swayed in the autumn breeze \nOur ember eyes met between the leaves \nAnd somehow every sound around me \nHad broken into harmony \nI'd never heard a sweeter melody")

#Ejercicio 1.4
def factorial_de_dos() -> int:
    x: int = factorial(2)
    return x

#Ejercicio 1.5
def factorial_de_tres() -> int:
    x: int = factorial(3)
    return x

#Ejercicio 1.6
def factorial_de_cuatro() -> int:
    x: int = factorial(4)
    return x

#Ejercicio 1.7
def factorial_de_cinco() -> int:
    x: int = factorial(5)
    return x

#Ejercicio 2
#Ejercicio 2.1
def imprimirSaludo(nombre: str):
    print ("Hola " + nombre)

#Ejercicio 2.2
def raiz_cuadrada_de(x: float) -> float:
    x = sqrt(x)
    return x

#Ejercicio 2.3
def imprimir_dos_veces(estribillo: str):
    estribillo *= 2
    return estribillo

    print(imprimir_dos_veces("And I've been thinking for some time \nHow to spend all these nine lives \nI guess just maybe I could spend one on you"))

#Ejercicio 2.4
def es_multiplo_de(n: int, m: int) -> bool:
    if (n%m == 0):
        return True
    else:
        return False

print (es_multiplo_de(9, 3))

#Ejercicio 2.5
def es_par(n: int) -> bool:
    if (es_multiplo_de(n, 2)):
        return True
    else:
        return False

print (es_par(8))

#Ejercicio 2.6
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    x: int = ceil(comensales*min_cant_de_porciones/8)
    return x

print(cantidad_de_pizzas(4,5))

#Ejercicio 3
#Ejercicio 3.1
def alguno_es_0(n1: int, n2: int) -> bool:
    res: bool = n1 == 0 or n2 == 0
    return res

print(alguno_es_0(0,4))

#Ejercicio 3.2
def ambos_son_0(n1: int, n2: int) -> bool:
    res: bool = n1 == 0 and n2 == 0
    return res

#Ejercicio 3.3
def es_nombre_largo(nombre: str) -> bool:
    res: bool = len(nombre) >= 3 and len(nombre) <= 8
    return res

print(es_nombre_largo("emiliano"))

#Ejercicio 3.4
def es_bisiesto(x: int) -> bool:
    res: bool = (x % 400 == 0) or (x % 4 == 0 and x % 100 != 0)
    return res

print(es_bisiesto(2012))

#Ejercicio 4
#Ejercicio 4.1
def peso_pino(h: float) -> float:
    p: float = 0
    if (h <= 3):
        p = h * 3 * 100
    else:
        p = 3 * 3 * 100 + 2 * 100 * (h-3)

    return p

#Ejercicio 4.2
def es_peso_util(p: float) -> bool:
    res: bool = max(p, 1000) == 1000 and min(p, 400) == 400
    return res

#Ejercicio 4.3
def sirve_pino (h: float) -> bool:
    res: bool = es_peso_util(peso_pino(h))
    return res

print(sirve_pino(3))

#Ejercicio 5
#Ejercicio 5.1
def devolver_el_doble_si_es_par (n: int) -> int:
    if(es_par(n)):
        n *= 2

    return n

#Ejercicio 5.2
def devolver_valor_si_es_par_sino_el_que_sigue(n: int) -> int:
    if(not(es_par(n))):
        n += 1

    return n

#Ejercicio 5.3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n: int) -> int:
    if (es_multiplo_de(n, 9)):
        n *= 3
    elif (es_multiplo_de(n, 3)):
        n *= 2

    return n

#Ejercicio 5.4
def nombre_largo(x: int) -> str:
    res: str = ""
    if (len(x) >= 5):
        res = "Tu nombre tiene muchas letras!"
    else:
        res = "Tu nombre tiene menos de 5 caracteres"

    return res

#Ejercicio 5.5
def vacaciones_o_pala(s: chr, e: int):
    res: str = ""
    if (e < 18 or e > 65 or (e > 60 and s == "f")):
        res = "Andá de vacaciones"
    else:
        res = "Agarrá la pala"

    print(res)

vacaciones_o_pala("m", 19)

#Ejercicio 6
#Ejercicio 6.1
def imprimir_1_10():
    i: int = 1
    while (i <= 10):
        print(i)
        i += 1

#Ejercicio 6.2
def imprimir_pares_10_40():
    i: int = 10
    while (i <= 40):
        print(i)
        i += 2

#Ejercicio 6.3
def eco_10():
    i: int = 1
    while (i <= 10):
        print("eco")
        i += 1

#Ejercicio 6.4
def despegue(s: int):
    while (s > 0):
        print (s)
        s -= 1
    print ("Despegue")

#Ejercicio 6.5
def viaje_en_el_tiempo(ap: int, al: int):
    año: int = ap
    while (año >= al):
        año -= 1
        print("Viajó un año al pasado, estamos en el año " + str(año))

#Ejercicio 6.6
def viaje_a_Aristoteles(ap: int):
    año: int = ap
    while (año >= -384):
        año -= 20
        if (año >= 0):
            print ("Viajó veinte años al pasado, estamos en el año " + str(año) + " d.C.")
        else:
            print ("Viajó veinte años al pasado, estamos en el año " + str(abs(año)) + " a.C.")

#Ejercicio 7
#Ejercicio 7.1
def imprimir_1_10_for():
    for i in range(1,11):
        print (i)

#Ejercicio 7.2
def imprimir_pares_10_40_for():
    for i in range(10,41,2):
        print (i)

#Ejercicio 7.3
def eco_10_for():
    for i in range (1,11):
        print("eco")

#Ejercicio 7.4
def despegue_for(s: int):
    for i in range(s, 0, -1):
        print(i)
        print("Despegue")

#Ejercicio 7.5
def viaje_en_el_tiempo_for(ap: int, al: int):
    for i in range(ap-1, al-1, -1):
        print("Viajó un año al pasado, estamos en el año " + str(i))

#Ejercicio 7.6
def viaje_a_Aristoteles_for(ap: int):
    for i in range(ap-1, -385, -20):
        if (i >= 0):
            print ("Viajó veinte años al pasado, estamos en el año " + str(i) + " d.C.")
        else:
            print ("Viajó veinte años al pasado, estamos en el año " + str(abs(i)) + " a.C.")