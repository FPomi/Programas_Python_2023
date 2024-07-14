"""
Sean los enteros positivos n1, n2, n3, r1, r2, r3, con n1 <= n2 <= n3 y r1 < r2 < r3. 
Considerar el siguiente juego por turnos de información perfecta para los jugadores L y R. 
Hay 3 pilas, de n1, n2 y n3 objetos, respectivamente. Cada jugador a su turno debe quitar r1, r2 o r3 
objetos de una misma pila. Comienza el jugador L. Gana quien juega último.

Escribir un programa que, dadas estas variables de entrada, calcule los conjuntos de P-posiciones 
y N-posiciones, y que incluya además una función que, dada una posición para el jugador L, 
devuelva la resultante de hacer una jugada óptima. Si la posición original no fuese ganadora para L, 
se deberá "dificultar" la decisión al jugador R en su siguiente turno si fuera posible. 
Opcionalmente, hacer también el cálculo de P-posiciones y N-posiciones para la versión en 
que pierde quien juega último.
"""

def calculate_P_positions(n1, n2, n3, r1, r2, r3):
    max_n = max(n1, n2, n3)
    p_positions = set()
    n_positions = set()

    # Base cases for dynamic programming
    p_positions.add((0, 0, 0))
    n_positions.add((0, 0, 0))

    # Dynamic programming to calculate P-positions and N-positions
    for n in range(1, max_n + 1):
        for a in range(n1 + 1):
            for b in range(n2 + 1):
                for c in range(n3 + 1):
                    if a >= r1 and (a - r1, b, c) in n_positions:
                        p_positions.add((a, b, c))
                    if b >= r2 and (a, b - r2, c) in n_positions:
                        p_positions.add((a, b, c))
                    if c >= r3 and (a, b, c - r3) in n_positions:
                        p_positions.add((a, b, c))
                    if (a, b, c) not in p_positions:
                        n_positions.add((a, b, c))

    return p_positions, n_positions


def optimal_move(L_pos, p_positions, r1, r2, r3):
    # Check if the current position is winning for L
    if L_pos not in p_positions:
        return None

    # Check each possible move for L and choose the optimal one
    possible_moves = [(r1, 0, 0), (0, r2, 0), (0, 0, r3)]
    for move in possible_moves:
        next_pos = tuple(L_pos[i] - move[i] for i in range(3))
        if next_pos in p_positions:
            return move

    # If no optimal move found, choose any move that leads to an N-position
    for move in possible_moves:
        next_pos = tuple(L_pos[i] - move[i] for i in range(3))
        if next_pos in n_positions:
            return move

    # If no N-position found, choose any move (this should not happen for a winning position)
    return possible_moves[0]


# Example usage:
if __name__ == "__main__":
    n1, n2, n3 = 3, 5, 7
    r1, r2, r3 = 1, 2, 3

    p_positions, n_positions = calculate_P_positions(n1, n2, n3, r1, r2, r3)
    print("P-positions:", p_positions)
    print("N-positions:", n_positions)

    L_position = (3, 5, 7)
    optimal_move_L = optimal_move(L_position, p_positions, r1, r2, r3)
    print("Optimal move for L:", optimal_move_L)