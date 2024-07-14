from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
#----------------------------------------------------------------------------------------------------------------------------#

def existeVueloDeOrigen (origen: str, vuelos: List[Tuple[str, str]]):
    
    salida = 0
    respuesta = False
    
    for vuelo in vuelos:
        if vuelo[salida] == origen:
            respuesta = True
    
    return respuesta


#----------------------------------------------------------------------------------------------------------------------------#

def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  
    salida = 0
    llegada = 1
  
    existeRuta = True

    #vuelosPorTomar = vuelos
    vuelosTomados = []
    ultimoVuelo = (None, origen)
    
    respuesta = 0
  
    while(existeRuta == True and ultimoVuelo[llegada] != destino):
      
        if existeVueloDeOrigen (ultimoVuelo[llegada], vuelos) and not existeVueloDeOrigen (ultimoVuelo[llegada], vuelosTomados):
          
            for vuelo in vuelos:
                if vuelo[salida] == ultimoVuelo[llegada]:
                    ultimoVuelo = vuelo
                    vuelosTomados.append(ultimoVuelo)
            
        else:
            existeRuta = False
    
    if (ultimoVuelo[llegada] == destino):
        respuesta = len(vuelosTomados)
    else:
        respuesta = -1
        
    return respuesta

#----------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))