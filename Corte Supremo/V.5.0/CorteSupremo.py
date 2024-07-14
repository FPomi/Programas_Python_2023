import random
import time

#---------------------------------------------------------------------------------------------------------------------------#

def generarPorcentajes():
    
    f = []
    sumatoria = 0
    maxCantidadPorcentajes = 4
    
    for i in range(maxCantidadPorcentajes - 1):
        
        if (sumatoria != 100):
            
            f.append(random.randrange(100 - sumatoria))
        
            while (sumatoria + f[i] > 100):
                f[i] = random.randrange(100 - sumatoria)
    
            sumatoria += f[i]
        
        else:
            f.append(0)
        
    f.append(100 - sumatoria)
    
    return f

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
        
    parteIzquierda.append(porcentaje)
    parteDerecha.append(torta[parte] - porcentaje)
    
    for valor in range(parte + 1, len(torta)):
        parteIzquierda.append(0)
        parteDerecha.append(torta[valor])
    
    return parteIzquierda, parteDerecha

#---------------------------------------------------------------------------------------------------------------------------#
def ganancia (parteTorta, torta, f):
    
    ganancia = 0
    
    for porcion in range(len(parteTorta)):
        
        if torta[porcion] > 0:
            porcentajeDelGusto = parteTorta[porcion] / torta[porcion]
            ganancia += porcentajeDelGusto * f[porcion]
    
    return round(ganancia/100, 2)

#---------------------------------------------------------------------------------------------------------------------------#
def mejorParte (parteIzquierda, parteDerecha, torta, f):
    
    mejorParte = []
    
    gananciaIzquierda = ganancia (parteIzquierda, torta, f)
    gananciaDerecha = ganancia (parteDerecha, torta, f)
    
    if (gananciaIzquierda > gananciaDerecha):
        mejorParte = parteIzquierda
    else:
        mejorParte = parteDerecha
    
    return mejorParte

#---------------------------------------------------------------------------------------------------------------------------#

def corteDeU1(f1, f2, torta):
      
    corte = {"Izquierda":[], "Derecha":[]}
    porcentaje = 0
    precision = 0.1 # precision del 0.1%
    gananciaMaxF1 = 0
    
    while (porcentaje < 100):
        
        parteIzquierda, parteDerecha = dividirEnPartes (torta, porcentaje)
        
        if (mejorParte(parteIzquierda, parteDerecha, torta, f1) != mejorParte(parteIzquierda, parteDerecha, torta, f2)
        or ganancia(parteIzquierda, torta, f1) == ganancia(parteDerecha, torta, f1)):
            
            if ganancia(mejorParte(parteIzquierda, parteDerecha, torta, f1), torta, f1) > gananciaMaxF1:
        
                corte["Izquierda"] = parteIzquierda
                corte["Derecha"] = parteDerecha
            
                gananciaMaxF1 = ganancia(mejorParte(parteIzquierda, parteDerecha, torta, f1), torta, f1)
                
        elif(ganancia(parteIzquierda, torta, f2) == ganancia(parteDerecha, torta, f2)):
            
            if ganancia(mejorParte(parteIzquierda, parteDerecha, torta, f1), torta, f1) > gananciaMaxF1:
                
                if mejorParte(parteIzquierda, parteDerecha, torta, f1) == parteIzquierda:
                    parteIzquierda, parteDerecha = dividirEnPartes (torta, porcentaje - precision)
                    
                elif (porcentaje < 100):
                    parteIzquierda, parteDerecha = dividirEnPartes (torta, porcentaje + precision)
                
                corte["Izquierda"] = parteIzquierda
                corte["Derecha"] = parteDerecha
            
                gananciaMaxF1 = ganancia(mejorParte(parteIzquierda, parteDerecha, torta, f1), torta, f1)
                
        porcentaje += precision
    
    return corte

#---------------------------------------------------------------------------------------------------------------------------#

def eleccionDeU2 (corte, torta, f2):
    
    partes = {}
    
    if ganancia(corte["Izquierda"], torta, f2) > ganancia(corte["Derecha"], torta, f2):
        partes = {"Usuario1":[corte["Derecha"]], "Usuario2": [corte["Izquierda"]]}
    else:
        partes = {"Usuario1":[corte["Izquierda"]], "Usuario2": [corte["Derecha"]]}

    return partes

#---------------------------------------------------------------------------------------------------------------------------#

def corteSupremo ():
    
    n = 100
    
    for i in range(n):
    
        partes = {}
        
        f1 = generarPorcentajes()    
        f2 = generarPorcentajes()
        torta = generarPorcentajes()

        partes = eleccionDeU2 (corteDeU1(f1, f2, torta), torta, f2)
        
        print(partes)

#---------------------------------------------------------------------------------------------------------------------------#

corteSupremo()













