from queue import Queue

VACIA = 0

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
def avanzarFila(fila: Queue, min: int):
  
  min_salida_caja_1 = 0
  min_salida_caja_2 = 0
  min_salida_caja_3 = 0

  min_llegada_fila = -1

  min_actual = 0

  nuevo_numero = fila.qsize()

  cajas = {"Caja 1" : 0, "Caja 2" : 0, "Caja 3" : 0}

  for min_actual in range (min + 1):
    
    if min_actual % 4 == 0:
      nuevo_numero += 1 
      fila.put(nuevo_numero)

    if min_actual == min_llegada_fila:
      fila.put(persona_volviendo)

    if not fila.empty():

      if cajas["Caja 1"] == VACIA and min_actual >= 1:
        cajas["Caja 1"] = fila.get()
        min_salida_caja_1 = min_actual + 10
    
      elif cajas["Caja 2"] == VACIA and min_actual >= 3:
        cajas["Caja 2"] = fila.get()
        min_salida_caja_2 = min_actual + 4

      elif cajas["Caja 3"] == VACIA and min_actual >= 2:
        cajas["Caja 3"] = fila.get()
        min_salida_caja_3 = min_actual + 4
        persona_volviendo = cajas["Caja 3"]
        min_llegada_fila = min_actual + 3

    if min_actual == min_salida_caja_1:
      cajas["Caja 1"] = VACIA
    
    if min_actual == min_salida_caja_2:
      cajas["Caja 2"] = VACIA

    if min_actual == min_salida_caja_3:
      cajas["Caja 3"] = VACIA
    
    
if __name__ == '__main__':
  fila: Queue = Queue()
  fila_inicial: int = int(input())
  for numero in range(1, fila_inicial+1):
    fila.put(numero)
  min: int = int(input())
  avanzarFila(fila, min)
  res = []
  for i in range(0, fila.qsize()):
    res.append(fila.get())
  print(res)

# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)

