#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
# Ejercicio N8

import random

def generarNrosAlAzar (n : int, desde : int, hasta : int) :
    
    numerosAlAzar = []

    for i in range (n):
        numero = random.randrange(desde, hasta)
        numerosAlAzar.append(numero)

    return numerosAlAzar

print("Numeros al azar: ", generarNrosAlAzar (5, 1, 10))
print("Numeros al azar: ", generarNrosAlAzar (5, 5, 30))
print()

#-------------------------------------------------------------------------#
# Ejercicio N9

from queue import LifoQueue as Pila

def generarPilaConNrosAlAzar (n : int, desde : int, hasta : int) :
    pila = Pila()
    numerosParaApilar = generarNrosAlAzar (n, desde, hasta)

    for numero in numerosParaApilar:
        pila.put (numero) 

    return pila

print("Pila al azar: ", generarPilaConNrosAlAzar (5, 1, 10))

pila = generarPilaConNrosAlAzar (5, 1, 10)

for i in range(pila.qsize()):
    print("Pila ", pila.qsize(), " -> ", pila.get())

print()

#-------------------------------------------------------------------------#
# Ejercicio N10

def cantidadElementos(pila : Pila):
    return pila.qsize()

pila = generarPilaConNrosAlAzar (5, 1, 10)

print("La pila tiene ", cantidadElementos(pila)," elementos")
print()

#-------------------------------------------------------------------------#
# Ejercicio N11

def buscarElMaximo(pila : Pila):
    
    maximo = 0

    for i in range(cantidadElementos(pila)):

        elemento = pila.get()
        
        print("Pila ", (pila.qsize() + 1), " -> ", elemento)

        if elemento > maximo:
            maximo = elemento
    
    return maximo

print("Maximo: ", buscarElMaximo(pila))
print()

#-------------------------------------------------------------------------#
# Ejercicio N12 <NO QUIERO HACERLO>
"""def estaBienBalanceada(texto : str):
    
    estaBienBalanceada = True
    

    
    return estaBienBalanceada

print("10 * ( 1 + ( 2 * ( -1))), esta balanceada? ",estaBienBalanceada("10 * ( 1 + ( 2 * ( -1)))"))
"""
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
# Ejercicio N13

from queue import Queue as Cola

def generarColaConNrosAlAzar (n : int, desde : int, hasta : int) :
    cola = Cola()
    numerosParaApilar = generarNrosAlAzar (n, desde, hasta)

    for numero in numerosParaApilar:
        cola.put (numero) 

    return cola

print("Cola al azar: ", generarPilaConNrosAlAzar (5, 1, 10))

cola = generarPilaConNrosAlAzar (5, 1, 10)

for i in range(cola.qsize()):
    print("Pila ", (i + 1), " -> ", cola.get())

print()

#-------------------------------------------------------------------------#
# Ejercicio N14

def cantidadElementos(cola : Cola):
    return cola.qsize()

cola = generarPilaConNrosAlAzar (5, 1, 10)

print("La cola tiene ", cantidadElementos(cola)," elementos")
print()

#-------------------------------------------------------------------------#
# Ejercicio N15

def buscarElMaximo(cola : Cola):
    
    maximo = 0

    for i in range(cantidadElementos(cola)):

        elemento = cola.get()
        
        print("Cola ", (i + 1), " -> ", elemento)

        if elemento > maximo:
            maximo = elemento
    
    return maximo

print("Maximo: ", buscarElMaximo(cola))
print()

#-------------------------------------------------------------------------#
# Ejercicio N16
def armarSecuenciaDeBingo():

    secuenciaDeBingo = Cola()
    numeros = list(range(100))
    random.shuffle(numeros)

    for numero in numeros:    
        secuenciaDeBingo.put (numero)

    #for i in range(secuenciaDeBingo.qsize()):
    #    print("Cola ", secuenciaDeBingo.qsize(), " -> ", secuenciaDeBingo.get())

    return secuenciaDeBingo

def armarCartonDeBingo():
    
    cartonDeBingo = []
    
    for i in range(12):
        
        numero  = random.randrange(100)

        while numero in cartonDeBingo:
            numero  = random.randrange(100)

        cartonDeBingo.append(numero)
    
    return cartonDeBingo


def jugarCartonDeBingo( carton : list[int], bolillero : Cola):
    cantidadDeJugadas = 0

    while(len(carton) > 0):

        numero = bolillero.get()

        if numero in carton:
            carton.remove(numero)

        cantidadDeJugadas += 1

    return cantidadDeJugadas

print("Se necesitaron", jugarCartonDeBingo(armarCartonDeBingo(), armarSecuenciaDeBingo()), "para hacer Bingo")
print()

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
# Ejercicio N18

def agruparPorLongitud(frase : str):
    palabrasPorLongitud = {}

    contador = 0

    for letra in frase:
        
        if letra == " ":
            if str(contador) in palabrasPorLongitud:
                palabrasPorLongitud[str(contador)] += 1
            else:
                palabrasPorLongitud[str(contador)] = 1
            contador = 0
        else:
            contador += 1

    return palabrasPorLongitud

print(agruparPorLongitud("Hola mi nombre es Franco "))
