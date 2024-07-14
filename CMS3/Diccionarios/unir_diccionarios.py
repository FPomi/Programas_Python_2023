from typing import List
from typing import Dict
import json

def unir_diccionarios(a_unir: List[Dict[str,str]]) -> Dict[str,List[str]]:
  
  diccionarios_unidos = {}

  for diccionario in a_unir:
    for clave in diccionario.keys():
      if clave in diccionarios_unidos.keys():
        diccionarios_unidos[clave].append(diccionario[clave])
      else:
        diccionarios_unidos[clave] = [diccionario[clave]]

  return diccionarios_unidos

if __name__ == '__main__':
  x = json.loads(input()) # Ejemplo de input: [{"a":2},{"b":3,"a":1}]
  print(unir_diccionarios(x))

