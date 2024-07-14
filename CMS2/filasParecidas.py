from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

#----------------------------------------------------------------------------------------------------------------------------#

def compararParecidoFilas(l1: List[int], l2: List[int], n: int) -> bool:
    
    valoresParecidos = 0
    respuesta = True
    
    for posicion in range(len(l1)):
        if l1[posicion] == l2[posicion] + n:
            valoresParecidos += 1
    
    if valoresParecidos == len(l1):
        repuesta = True
    else:
        respuesta = False
    
    return respuesta

#----------------------------------------------------------------------------------------------------------------------------#

def filasParecidas(matriz: List[List[int]]) -> bool :
    
    filasParecidas = False
    filaAnterior = 0
    filaActual = 1
    n = 0
    
    while (filaActual < len(matriz) and (matriz[1][0] >= matriz[0][0] + n or matriz[1][0] <= matriz[0][0] - n)):
        
        filaAnterior = 0
        filaActual = 1
        
        while (filaActual < len(matriz) and (compararParecidoFilas(matriz[filaActual], matriz[filaAnterior], n) or compararParecidoFilas(matriz[filaActual], matriz[filaAnterior], (-n)))):
            filaActual += 1
            filaAnterior += 1
        
        n += 1
    
    if (filaActual == len(matriz)):
        filasParecidas = True
    
    return filasParecidas

#----------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))