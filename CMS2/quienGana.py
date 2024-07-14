import sys

def quienGana(j1: str, j2: str) -> str : 
    
    ganador = "Jugador1"
    
    if (j1 == "Piedra"):
        if (j2 == "Papel"):
            ganador = "Jugador2"
        elif (j2 == "Piedra"):
            ganador = "Empate"
            
    elif (j1 == "Papel"):
        if (j2 == "Tijera"):
            ganador = "Jugador2"
        elif (j2 == "Papel"):
            ganador = "Empate"
    
    else:
        if (j2 == "Piedra"):
            ganador = "Jugador2"
        elif (j2 == "Tijera"):
            ganador = "Empate"

    return ganador

if __name__ == '__main__':
  x = input()
  jug = str.split(x)
  print(quienGana(jug[0], jug[1]))