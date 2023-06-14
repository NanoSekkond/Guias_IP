from math import *
import random as random
from queue import LifoQueue as Pila

#Guia 7
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

#Ejercicio Extra
def MCD(x: int, y: int) -> int:
    while (x % y != 0):
        z = y
        y = x % y
        x = z
    return y

print(MCD(350, 125))

#Guía 8

#Ejercicio 1
#Ejercicio 1.1
#Ejercicio 1.1.1
def pertenece1(s: list, n: int) -> bool:
    res: bool = False
    for e in s:
        if (n == e):
            res = True

    return res

#Ejercicio 1.1.2
def pertenece2(s: list, n: int) -> bool:
    res: bool = False
    i: int = 0
    while (i < len(s)):
        if (n == s[i]):
            res = True
        i += 1

    return res

#Ejercicio 1.1.3
def pertenece3(s: list, n: int) -> bool:
    res: bool = False
    for i in range(0, len(s), 1):
        if (n == s[i]):
            res = True

    return res

#Ejercicio 1.2
def divideATodos(s: list, n: int) -> bool:
    res: bool = True
    for e in s:
        if (e % n != 0):
            res = False
    
    return res

#Ejercicio 1.3
def sumaTotal(s: list) -> int:
    res: int = 0
    for n in s:
        res += n

    return res

#Ejericio 1.4
def ordenados(s: list) -> bool:
    res: bool = True
    i: int = 0
    while (i < len(s)-1):
        if (s[i] > s[i+1]):
            res = False
        i += 1
    
    return res

#Ejercicio 1.5
def alguna_palabra_larga(s: list) -> bool:
    res: bool = False
    for p in s:
        if (len(p) > 7):
            res = True

    return res

#Ejercicio 1.6
def palindromo(a: str) -> bool:
    res: bool = True
    i: int = 0
    while (i < len(a)-1):
        if (a[i] != a[len(a)-1-i]):
            res = False
        
        i += 1

    return res

#Ejercicio 1.7
def seguridad_contrasena(a: str) -> str:
    res: str = ""
    if (len(a) < 5):
        res = "ROJA"
    elif (len(a) > 8 and hay_mayus(a) and hay_minus(a) and hay_num(a)):
        res = "VERDE"
    else:
        res = "AMARILLA"

    return res

def hay_mayus(a:str) -> bool:
    res: bool = False
    for c in a:
        if (c.isupper()):
            res = True
    
    return res

def hay_minus(a: str) -> bool:
    res: bool = False
    for c in a:
        if (c.islower()):
            res = True

    return res

def hay_num(a: str) -> bool:
    res: bool = True
    for c in a:
        if(c.isnumeric()):
            res = True

    return res

#Ejercicio 1.8
def banco(s: list) -> int:
    saldo: int = 0
    monto: int = 0
    for t in s:
        monto = t[1]
        if (t[0] == "R"):
            monto = -monto
        
        saldo += monto
    
    return saldo

#Ejercicio 1.9
def tres_vocales(a: str) -> bool:
    res: bool = False
    vocales: list[str] = ['a', 'e', 'i', 'o', 'u']
    for c in a:
        if (pertenece1(vocales, c)):
            vocales.remove(c)
    
    if (len(vocales) < 3):
        res = True

    return res

#Ejercicio 2
#Ejercicio 2.1
listaN: list = [3,4,5,6,7,8]

def cero_por_par_inout(s: list) -> list:
    for i in range(0, len(s), 1):
        if (s[i] % 2 == 0):
            s[i] = 0

    return s

#Ejercicio 2.2
def cero_por_par_in(s: list) -> list:
    s2: list = s.copy()
    for i in range(0, len(s2), 1):
        if (s2[i] % 2 == 0):
            s2[i] = 0

    return s2

print(listaN)
cero_por_par_in(listaN)
print(listaN)
print(cero_por_par_in(listaN))

#Ejercicio 2.3
def no_vowels(s: str) -> str:
    vocales: list = ["a", "e", "i", "o", "u"]
    res: str = ""
    for c in s:
        if not(pertenece1(vocales, c)):
            res += c

    return res

palabra: str = "macucas"
print(palabra)
no_vowels(palabra)
print(palabra)
print(no_vowels(palabra))

#Ejercicio 2.4
def no_vowels_space(s: str) -> str:
    vocales: list = ["a", "e", "i", "o", "u"]
    res: str = ""
    for c in s:
        if (pertenece1(vocales, c)):
            res += "_"
        else:
            res += c

    return res

print(palabra)
no_vowels_space(palabra)
print(palabra)
print(no_vowels_space(palabra))

#Ejercicio 2.5
def da_vuelta_str(s: str) -> str:
    res: str = ""
    for i in range(len(s)-1, -1, -1):
        res += s[i]

    return res

print(palabra)
da_vuelta_str(palabra)
print(palabra)
print(da_vuelta_str(palabra))

#Ejercicio 3
#Ejercicio 3.1
def lista_de_estudiantes() -> list:
    res: list = []
    estudiante = str(input())
    while (estudiante != "listo"):
        res.append(estudiante)
        estudiante = str(input())

    return res

#Ejercicio 3.2
def historial_sube() -> list:
    res: list = []
    operacion: str = ""
    monto: int = ""
    while (operacion != "X"):
        print("Seleccionar operacion (C - Cargar, D - Descontar, X - Finalizar)")
        operacion = str(input())
        if (operacion != "X"):
            print("Ingresar monto:")
            monto = int(input())
            res.append((operacion, monto))

    return res

#Ejercicio 3.3
def siete_y_medio() -> list:
    print ("Jugar al siete y medio? Y/N")
    check: str = ""
    check = str(input())
    if (check == "N"):
        print("Ortiva >:(")
        return
    res: list = []
    respuesta: str = ""
    carta: int = 0
    acumulado: float = 0
    while (respuesta != "N"):
        carta = random.choice([1,2,3,4,5,6,7,10,11,12])
        res.append(carta)
        if (carta < 10):
            acumulado += carta
        else:
            acumulado += 0.5
        if (acumulado > 7.5):
            break
        print("Sacaste un " + str(carta) + ". Tenés " + str(acumulado) + " puntos. Sacar otra carta o plantarse? Y/N")
        respuesta = str(input())
    if (acumulado > 7.5):
        print("Perdiste D:")

    print ("Tu puntaje fue " + str(acumulado) + " y tus cartas fueron " + str(res))

#siete_y_medio()

#Ejercicio 4
#Ejercicio 4.1
def pertenece_a_cada_uno(s: list, e: int) -> list:
    res: list = []
    for lista in s:
        res.append((pertenece1(lista, e)))

    return res

print(pertenece_a_cada_uno([[3,4,5,2,5],[2,6,5,4],[2,4,5,3,1,3]], 3))

#Ejercicio 4.2
def es_matriz(s: list) -> bool:
    res: bool = True
    longitud: int = len(s[0])
    for lista in s:
        if (len(lista) != longitud):
            res = False
            break

    return res

print(es_matriz([[3,4,5],[1,2,3],[4,7,5]]))

#Ejercicio 4.3
def filas_ordenadas(m: list) -> list:
    res: list = []
    for lista in m:
        res.append((ordenados(lista)))

    return res

print(filas_ordenadas([[3,4,5],[1,2,3],[4,7,5]]))

#Ejercicio 4.4

#Guia 10
#Ejercicio 1
#Ejercicio 1.1
def contarlineas(nombre: str) -> int:
    res: int = 0
    archivo = open(nombre, "r")
    res = len(archivo.readlines())
    archivo.close()
    return res

print(contarlineas("Python\hewwo.txt"))

#Ejercicio 1.2
def existePalabra(palabra: str, nombre: str) -> bool:
    res: bool = False
    curr: str = ""
    archivo = open(nombre, "r")
    for c in archivo.read():
        if (c == " " or c == "\n"):
            if (palabra == curr):
                res = True
                break
            curr = ""
        else:
            curr += c
    if (palabra == curr):
        res = True
    archivo.close()
    return res

print(existePalabra("nano", "Python\hewwo.txt"))

#Ejercicio 1.3
def cantidadApariciones(palabra: str, nombre: str) -> int:
    res: int = 0
    curr: str = ""
    archivo = open(nombre, "r")
    for c in (archivo.read()):
        if (c == " " or c == "\n"):
            if (palabra == curr):
                res += 1
            curr = ""
        else:
            curr += c
    if (curr == palabra):
        res += 1
    archivo.close()
    return res

print(cantidadApariciones("nano", "Python\hewwo.txt"))

"""
#Ejercicio 2
def clonarSinComentarios(nombre: str):
    archivo = open(nombre, "r")
    clon = open(nombre + "_sin_comentarios", "w")
    for line in archivo.readlines():
        for c in line:
            if (c != " " and c != "#"):
                clon.write(line)
                break
            if (c == "#"):
                break
    archivo.close()
    clon.close()

clonarSinComentarios("Python\hewwo.txt")

#Ejercicio 3
def invertirLineas(nombre: str):
    archivo = open(nombre, "r")
    reverso = open(nombre + "_reverso", "w")
    for line in archivo.readlines()[::-1]:
        reverso.write(line)
    archivo.close()
    reverso.close()

invertirLineas("Python\hewwo.txt")

#Ejercicio 4
def agregarLineaFinal(nombre: str, frase: str):
    archivo = open(nombre, "a")
    archivo.write("\n" + frase)
    archivo.close()

agregarLineaFinal("Python\hewwo.txt", "a veces pienso")
"""

#Ejercicio 8
def generarNrosAlAzar(n: int, desde: int, hasta: int) -> list:
    res: list = []
    for i in range(0, n, 1):
        res.append(random.randint(desde, hasta))
    return res

#Ejercicio 9
def pilaDeNumeros(l: list) -> Pila:
    res: Pila = Pila()
    for e in l:
        res.put(e)
    return res

#Ejercicio 10
def cantidadElementos(pila: Pila) -> int:
    res: int = 0
    while (not pila.empty()):
        pila.get()
        res += 1
    return res

print(cantidadElementos(pilaDeNumeros(generarNrosAlAzar(10, 1, 10))))

#Ejercicio 11
def buscarElMaximo(pila: Pila) -> int:
    res: int = 0
    while(not pila.empty()):
        e = pila.get()
        if (e > res):
            res = e
    return res

print(buscarElMaximo(pilaDeNumeros([3,5,4,2,4,5,6,7,8])))
    
#Ejercicio 12
def estaBienBalanceada(s: str) -> bool:
    res: bool = True
    acumulado: list = []
    for c in s:
        if (c == "("):
            acumulado.append(c)
        elif(c == ")"):
            if ("(" not in acumulado):
                res = False
                break
            else:
                acumulado.remove("(")
    if (len(acumulado) != 0):
        res = False
    return res

print(estaBienBalanceada("(3x + y)() * (2,3) = 24"))

#Ejercicio 18
def agruparPorLongitud(nombre: str) -> dict:
    res: dict = {}
    lon: int = 0
    archivo = open(nombre, "r")
    for c in archivo.read():
        if (c == " " or c == "\n"):
            if (lon in res):
                res[lon] += 1
            else:
                res[lon] = 1
            lon = 0
        else:
            lon += 1
    del res[0]
    return res

print(agruparPorLongitud("Python\hewwo.txt"))