--Guia 3 (Introduccion a Haskell)
--Ejercicio 1

f :: Integer -> Integer
f n | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16

g :: Integer -> Integer
g n | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

h :: Integer -> Integer
h n = f(g(n))

k :: Integer -> Integer
k n = g(f(n))


--Ejercicio 2

absoluto :: Integer -> Integer
absoluto n | n >= 0 = n
           | otherwise = (-n)

maximoabsoluto :: Integer -> Integer -> Integer
maximoabsoluto x y | absoluto x > absoluto y = absoluto x
                   | otherwise = absoluto y

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | x >= y && x >= z = x
              | y >= x && y >= z = y
              | z >= x && z >= y = z

algunoEs0 :: Float -> Float -> Bool
algunoEs0 x y = x == 0 || y == 0

algunoEs0PatternMatching :: Float -> Float -> Bool
algunoEs0PatternMatching 0 _ = True
algunoEs0PatternMatching _ 0 = True
algunoEs0PatternMatching _ _ = False

ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y = x == 0 && y == 0

ambosSon0PatternMatching :: Float -> Float -> Bool
ambosSon0PatternMatching 0 0 = True
ambosSon0PatternMatching _ _ = False

mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y = (x <= 3 && y <= 3) || (x > 3 && x <= 7 && y > 3 && y <= 7) || (x > 7 && y > 7)

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | x == y && y == z = x
                    | x == y = x + z
                    | x == z = x + y
                    | y == z = x + y
                    | otherwise = x + y + z

-- Deben ser naturales.
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y = mod x y == 0

-- Debe ser natural.
digitoUnidades :: Integer -> Integer
digitoUnidades x = mod x 10

-- Debe ser natural.
digitoDecenas :: Integer -> Integer
digitoDecenas x = digitoUnidades(div x 10)


--Ejercicio 3

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b = (mod (-a) b == 0) && (div (-a) b /= 0)


--Ejercicio 4

prodInt :: (Integer, Integer) -> (Integer, Integer) -> Integer
prodInt (a,b) (c,d) = a*c+b*d

todoMenor :: (Integer, Integer) -> (Integer, Integer) -> Bool
todoMenor (a,b) (c,d) = a < c && b < d

distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (a,b) (c,d) = sqrt ((a-c)^2 + (b-d)^2)

sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (a,b,c) = a + b + c

--N debe ser natural.
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) n | esMultiploDe a n && esMultiploDe b n && esMultiploDe c n = a + b + c
                             | esMultiploDe a n && esMultiploDe b n = a + b
                             | esMultiploDe a n && esMultiploDe c n = a + c
                             | esMultiploDe b n && esMultiploDe c n = b + c
                             | esMultiploDe a n = a
                             | esMultiploDe b n = b
                             | esMultiploDe c n = c
                             | otherwise = 0

posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (a,b,c) | (mod a 2 == 0) = 1
                     | (mod b 2 == 0) = 2
                     | (mod c 2 == 0) = 3
                     | otherwise = 4

crearPar :: t -> t -> (t,t)
crearPar a b = (a,b)

invertir :: (t,t) -> (t,t)
invertir (a,b) = (b,a)


--Ejercicio 5

todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (a,b,c) | (f5(a) > g5(a)) && (f5(b) > g5(b)) && (f5(c) > g5(c)) = True   
                     | otherwise = False

f5 :: Integer -> Integer
f5 n | n <= 7 = n^2
     | otherwise = 2*n-1

g5 :: Integer -> Integer
g5 n | mod n 2 == 0 = div n 2
     | otherwise = 3*n + 1


--Ejercicio 6

bisiesto :: Integer -> Bool
bisiesto n | (mod n 4 == 0 && mod n 100 /= 0) || (mod n 400 == 0) = True
           | otherwise = False


--Ejercicio 7

distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (a,b,c) (x,y,z) = absolutof(a-x) + absolutof(b-y) + absolutof(c-z)

absolutof :: Float -> Float
absolutof n | n >= 0 = n
           | otherwise = (-n)


--Ejercicio 8

comparar :: Integer -> Integer -> Integer
comparar a b | sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b) = 1
             | sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b) = -1
             | otherwise = 0

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos n = (mod n 10) + (mod (div n 10) 10)


-- Guia 4 (Recursion sobre enteros)
-- Ejercicio 1

fibonacci :: Integer -> Integer
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci (n-1) + fibonacci (n-2)


--Ejercicio 2

parteEntera :: Float -> Integer
parteEntera x | x >= 0 = floor x
              | otherwise = (floor x) + 1

parteEntera2 :: Float -> Integer
parteEntera2 x | x < 1 && x >= 0 = 0
               | x > -1 && x <= 0 = -1
               | x >= 1 = 1 + parteEntera2 (x-1)
               | otherwise = (-1) + parteEntera2 (x+1)


--Ejercicio 3

esDivisible :: Integer -> Integer -> Bool
esDivisible a b | b == 0 || b > a = False
                | b == a = True
                | otherwise = esDivisible (a-b) b


--Ejercicio 4

sumaImpares :: Integer -> Integer
sumaImpares n | n == 1 = 1
              | n > 1 = sumaImpares(n-1) + (2*n) - 1


--Ejercicio 5

medioFact :: Integer -> Integer
medioFact n | n == 1 = 1
            | n == 2 = 2
            | otherwise = medioFact (n-2) * n


--Ejercicio 6

sumaDigitos :: Integer -> Integer
sumaDigitos n | n < 10 = n
              | otherwise = sumaDigitos(div n 10) + mod n 10


--Ejercicio 7

-- En la practica creamos funciones para n = mod n 10 y n = div n 10
todosLosDigitosIguales :: Integer -> Bool
todosLosDigitosIguales x | mod x 10 == mod (div x 10) 10 = todosLosDigitosIguales(div x 10)
                         | x < 10 = True
                         | otherwise = False


--Ejercicio 8

--Requiere que la cantidad de digitos de n sea mayor o igual que i y que i sea mayor a 0
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | n < 10 = n
                 | cantDeDigitos(n) == i = mod n 10
                 | otherwise = iesimoDigito (div n 10) i

cantDeDigitos :: Integer -> Integer
cantDeDigitos n | n < 10 = 1
                | otherwise = cantDeDigitos(div n 10) + 1


--Ejercicio 9

--Funciona mal con numeros con ceros xq segun Haskell 04534 es 4534 lo cual tiene sentido pero no se como arreglar :(
esCapicua :: Integer -> Bool
esCapicua n | cantDeDigitos(n) == 1 = True
            | iesimoDigito n (cantDeDigitos(n)) == iesimoDigito n 1 = esCapicua(cortarHeadTail(n))
            | otherwise = False

cortarHeadTail :: Integer -> Integer
cortarHeadTail n = div (mod n (10 ^ (cantDeDigitos (n) - 1))) 10


--Ejercicio 10

f1a :: Integer -> Integer
f1a n | n == 0 = 1
      | otherwise = f1a (n-1) + 2 ^ n

f2b :: Integer -> Float -> Float
f2b n q | n == 1 = q
        | otherwise = f2b (n-1) q + q ^ n

f3c :: Integer -> Float -> Float
f3c n q | n == 1 = q
        | otherwise = f2b ((2 * n) - 1) q + q ^ (2 * n)

f4d :: Integer -> Float -> Float
f4d n q | n == 1 = q ^ (2 * n)
        | otherwise = f2b ((2 * n) - 1) q - f2b (n-1) q + q ^ (2 * n) 


--Ejercicio 11

eAprox :: Integer -> Float
eAprox n | n == 0 = 1
         | otherwise = eAprox (n-1) + 1/(fromIntegral(factorial(n)))

factorial :: Integer -> Integer
factorial n | n == 1 = 1
            | otherwise = factorial (n-1) * n

e :: Float
e = eAprox(10)


--Ejercicio 12

susRaizDe2Aprox :: Integer -> Float
susRaizDe2Aprox n | n == 1 = 2
                  | otherwise = 2 + 1/(susRaizDe2Aprox(n-1))

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = (susRaizDe2Aprox (n)) - 1

-- Guia 5 (Recursion sobre listas)
--Ejercicio 1

longitud :: [t] -> Integer
longitud a | null a = 0
           | otherwise = longitud(tail a) + 1

longitud2 :: [t] -> Integer
longitud2 [] = 0
longitud2 (x:xs) = longitud2(xs) + 1

ultimo :: [t] -> t
ultimo a | longitud a == 1 = head a
         | otherwise = ultimo(tail a)

principio :: [t] -> [t]
principio a | longitud a == 1 = []
            | otherwise = head a:principio (tail a)

reverso :: [t] -> [t]
reverso [] = []
reverso a | longitud a == 1 = (head a):[]
          | otherwise = ultimo a:reverso (principio a)


--Ejercicio 2

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece x [] = False
pertenece x a | x == head a = True
              | longitud a == 1 = False
              | otherwise = pertenece x (tail a)

todosIguales :: (Eq t) => [t] -> Bool
todosIguales a | longitud a == 1 = True
               | pertenece (head a) (tail a) = todosIguales(tail a)
               | otherwise = False

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos a | longitud a == 1 = True
                 | pertenece (head a) (tail a) = False
                 | otherwise = todosDistintos (tail a)

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos a | longitud a == 1 = False
               | pertenece (head a) (tail a) = True
               | otherwise = hayRepetidos (tail a)

quitar :: (Eq t) => t -> [t] -> [t]
quitar x [] = []
quitar x a | pertenece x a == False = a
           | head a == x = tail a
           | otherwise = head a:quitar x (tail a)

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos x [] = []
quitarTodos x a | pertenece x a == False = a
                | pertenece x (quitar x a) = quitarTodos x (quitar x a)
                | otherwise = quitar x a

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos a | hayRepetidos a == False = a
                    | longitud a == 1 = a
                    | otherwise = head a:eliminarRepetidos (quitarTodos (head a) (tail a))

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos a b = mismosElementosAux (eliminarRepetidos a) (eliminarRepetidos b)

mismosElementosAux :: (Eq t) => [t] -> [t] -> Bool
mismosElementosAux [] [] = True
mismosElementosAux a b | longitud a /= longitud b = False
                       | longitud a == 1 && head a == head b = True
                       | pertenece (head a) b == False = False
                       | otherwise = mismosElementosAux (tail a) (quitar (head a) b)

esCapicuaList :: (Eq t) => [t] -> Bool
esCapicuaList a | reverso a == a = True
                | otherwise = False


--Ejercicio 3

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria a | longitud a == 1 = head a
            | otherwise = sumatoria (tail a) + head a

productoria :: [Integer] -> Integer
productoria [] = 0
productoria a | longitud a == 1 = head a
              | otherwise = productoria (tail a) * head a

maximo :: [Integer] -> Integer
maximo a | longitud a == 1 = head a
         | head a >= head (tail a) = maximo (head a : tail (tail a))
         | otherwise = maximo (tail a)

sumarN :: Integer -> [Integer] -> [Integer]
sumarN x a | longitud a == 0 = []
           | otherwise = ((head a) + x) : sumarN x (tail a)

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero a = sumarN (head a) a

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo a = sumarN (ultimo a) a

pares :: [Integer] -> [Integer]
pares a | longitud a == 1 && mod (head a) 2 /= 0 = []
        | longitud a == 1 = a
        | mod (head a) 2 /= 0 = pares (tail a)
        | otherwise = head a : pares (tail a)

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n a | longitud a == 1 && mod (head a) n /= 0 = []
                 | longitud a == 1 = a
                 | mod (head a) n /= 0 = multiplosDeN n (tail a)
                 | otherwise = head a : multiplosDeN n (tail a)

ordenar :: [Integer] -> [Integer]
ordenar a = reverso (ordenarAux a)

ordenarAux :: [Integer] -> [Integer]
ordenarAux a | longitud a == 0 = []
             | otherwise = maximo a : ordenarAux (quitar (maximo a) a)


--Ejercicio 4

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos a | longitud a == 1 = a
                        | head a == ' ' && head (tail a) == ' ' = sacarBlancosRepetidos (tail a)
                        | otherwise = head a : sacarBlancosRepetidos(tail a)

contarPalabras :: [Char] -> Integer
contarPalabras a = contarPalabrasAux(sacarBlancosRepetidos a)

contarPalabrasAux :: [Char] -> Integer
contarPalabrasAux a | longitud a == 1 = 1
                    | head a == ' ' = contarPalabrasAux(tail a) + 1
                    | otherwise = contarPalabrasAux(tail a)

existeSecuenciaDeTuplas :: Integer -> Integer -> [(Integer, Integer)] -> Bool
existeSecuenciaDeTuplas a b (x:xs) | pertenece (a, b) (x:xs) = True
                                   | otherwise = existeSecuenciaDeTuplas a b (x:xs)

unirListas :: [t] -> [t] -> [t]
unirListas (x:xs) (y:ys) | longitud xs == 0 = x:(y:ys)
                         | otherwise = x : (unirListas xs (y:ys))

mcd :: Integer -> Integer -> Integer
mcd x y | x - y * div x y == 0 = y
        | otherwise = mcd y (x - y * (div x y))