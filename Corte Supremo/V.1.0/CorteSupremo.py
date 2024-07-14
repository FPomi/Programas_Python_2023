"""Se trata de escribir un programa que simule el proceso Cut & Choose iterado con información completa.

A partir de 4 componentes comestibles (1, 2, 3 y 4) que formarán parte de una "torta unidimensional",
se tiene una función f1 (o tabla) a valores reales no negativos que indica cuánto le gusta cada componente al primer jugador,
y otra f2 con lo mismo para el segundo jugador.

Leer enteros T y N. A partir de un arreglo de T elementos todos del conjunto {1,2,3,4} que representa la torta,
la función de valoración ui de un jugador se calcula simplemente en proporción a la cantidad de 1, de 2, de 3 y de 4
que contiene el arreglo, sumando los "gustos" del jugador, normalizado a 1. Es decir, para i=1,2,

    ui (p1...pt)   =   1/factor  Sumatoria j=1,...,t  fi (pj).

Conociendo las u1 y u2, el primer jugador divide la torta con un solo corte, y el segundo elige una de las dos mitades.
Así, se pide hacer una simulación que consiste en el Cut & Choose para arreglos de tamaño T creados aleatoriamente con
las componentes mencionadas (cantidades cualesquiera). El procedimiento debe ser “estratégico”, esto es,
el primer jugador al conocer u2 divide teniendo en cuenta esta información.
Debe dividir el arreglo en 2 mitades conexas (ambas de entre 0 y T elementos), luego el segundo jugador elegirá la mitad
que le convenga, quedando la otra para el primero. Y así ambos van sumando las ganancias dadas por las ui a lo largo de N
iteraciones.

Tener en cuenta que en cada paso el primer jugador, una vez vista la torta, debe cortarla pensando en su propio beneficio,
pero suponiendo cómo será la elección del segundo, de quien conoce sus "gustos". De ser necesario, explicar el criterio usado
para esto.

Hacer la simulación N veces para los mismos parámetros, imprimiendo los datos relevantes en cada paso.
(Opcionalmente, graficar.)

Concluir comentando los resultados para distintas opciones en las tablas de gustos, observando las ganancias de los
participantes.

Lenguaje: a elección. Entregar el programa y un informe de 1 a 3 páginas."""

import random
import time

#---------------------------------------------------------------------------------------------------------------------------#

def generarPorcentajes():
    
    u1 = []
    sumatoria = 0
    maxCantidadPorcentajes = 4
    
    for i in range(maxCantidadPorcentajes - 1):
        
        if (sumatoria != 1):
            
            u1.append( round(random.uniform(0,1 - sumatoria), 2))
        
            while (sumatoria + u1[i] > 1):
                u1[i] = round(random.uniform(0,1 - sumatoria), 2)
    
            sumatoria += u1[i]
        
    u1.append( round(1 - sumatoria, 2) )
    
    return u1

#---------------------------------------------------------------------------------------------------------------------------#

def dividirEnPartes (torta, porcentaje):
    
    parteIzquierda = []
    parteDerecha = []
    
    parte = 0
    partes = torta[parte]
    
    while (porcentaje > partes):
        parte += 1
        partes += torta[parte]
          
    for valor in range(parte):        
        porcentaje -= torta[valor]
        parteIzquierda.append(torta[valor])
        parteDerecha.append(0)
        
    parteIzquierda.append(round(porcentaje, 2))
    parteDerecha.append(round(torta[parte] - porcentaje,2))
    
    for valor in range(parte + 1, len(torta)):
        parteIzquierda.append(0)
        parteDerecha.append(torta[valor])
    
    return parteIzquierda, parteDerecha

#---------------------------------------------------------------------------------------------------------------------------#
def ganancia (parteTorta, f):
    
    ganancia = 0
    print("Partes Torta:", len(parteTorta))
    print("Partes f:", len(f))
        
    if len(f) < 4:
        print("f :", f)
        
    for porcion in range(len(parteTorta)):
        #print(porcion)
        ganancia += (parteTorta[porcion] * f[porcion])
    
    return round(ganancia,2)

#---------------------------------------------------------------------------------------------------------------------------#
def mejorParte (torta, f, porcentaje):
    
    parteIzquierda, parteDerecha = dividirEnPartes (torta, porcentaje)
    mejorParte = []
    
    gananciaIzquierda = ganancia (parteIzquierda, f)
    gananciaDerecha = ganancia (parteDerecha, f)
    
    if (gananciaIzquierda > gananciaDerecha):
        mejorParte = parteIzquierda
    else:
        mejorParte = parteDerecha
    
    return mejorParte

#---------------------------------------------------------------------------------------------------------------------------#

def corteSupremo ():
    
    #crear porcentajes de gustos y torta   
    f1 = generarPorcentajes()    
    f2 = generarPorcentajes()
    torta = generarPorcentajes()
    
    #PROBLEMA EN ESTE CASO, PORQUE?
    #f1 = [0.25, 0.25, 0.25, 0.25]   
    #f2 = [0.25, 0.24, 0.26, 0.25]
    #torta = [0.25, 0.25, 0.25, 0.25]
    
    #print("Gustos U1:", f1)
    #print("Gustos U2:", f2)
    #print("Torta:", torta)
    #print()
    
    #hacer que u1 analise la mejor forma de cortar
    #hacer analisis de a un porciento hasta completar el 100, sorescribiendo la mejor opcion
    mejorDivision = {"Usuario1":[], "Usuario2":[]}
    porcentaje = 0.01
    gananciaMaxF1 = -1.0
    
    while (porcentaje < 1):
        
        #print(parteIzquierda)
        #print(parteDerecha)
        #print()
        
        #revisar que la porcion de mayor ganancia para cada usuario sea de un lado diferente (u1: izq, u2:der) y si eso se cumple
        #   guardar en una varible y comparar si es que no hay otro valor con mayor ganancia para u1 que cumpla con lo anterior  
    
        if (mejorParte(torta, f1, porcentaje) != mejorParte(torta, f2, porcentaje)):
            
            if ganancia(mejorParte(torta, f1, porcentaje), f1) > gananciaMaxF1:
            
                mejorDivision["Usuario1"] = mejorParte(torta, f1, porcentaje)
                mejorDivision["Usuario2"] = mejorParte(torta, f2, porcentaje)
            
                gananciaMaxF1 = ganancia(mejorParte(torta, f1, porcentaje), f1) 
        else:
            
            parteIzquierda, parteDerecha = dividirEnPartes (torta, porcentaje)
            
            if ganancia(parteIzquierda, f1) == ganancia(parteDerecha, f2):
                
                mejorDivision["Usuario1"] = parteIzquierda
                mejorDivision["Usuario2"] = parteDerecha
                
                gananciaMaxF1 = ganancia(parteIzquierda, f1) 
            
            elif ganancia(parteDerecha, f1) == ganancia(parteIzquierda, f2):
                
                mejorDivision["Usuario1"] = parteDerecha
                mejorDivision["Usuario2"] = parteIzquierda
            
                gananciaMaxF1 = ganancia(parteDerecha, f1) 
                
        
        porcentaje += 0.01
    
    #mostrar ganancias
    """print("Porcion para U1:", mejorDivision["Usuario1"])
    print("Porcion para U2:", mejorDivision["Usuario2"])"""
    
    vacio = 0
    
    if mejorDivision["Usuario1"] == []:
        vacio += 1
    
    print(vacio)
    
    return 0

for i in range (0,50):
    corteSupremo()















