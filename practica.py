import random


def display_board(board):
    """
    Función para mostrar el tablero de Tic-Tac-Toe en la consola.
    """
    print(f"""
    +-------+-------+-------+
    |       |       |       |
    |   {board[1]}   |   {board[2]}   |   {board[3]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[4]}   |   {board[5]}   |   {board[6]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[7]}   |   {board[8]}   |   {board[9]}   |
    |       |       |       |
    +-------+-------+-------+
    """)


def get_free_squares(board):
    """
    Devuelve una lista de los números de las casillas que están libres.
    """
    free_squares = []
    for i in range(1, 10):
        if board[i] != 'X' and board[i] != 'O':
            free_squares.append(i)
    return free_squares


def check_win(board, player):
    """
    Verifica si el jugador (player) ha ganado el juego.
    """
    # Combinaciones ganadoras (filas, columnas, diagonales)
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Filas
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columnas
        (1, 5, 9), (3, 5, 7)  # Diagonales
    ]

    for cond in win_conditions:
        if board[cond[0]] == player and board[cond[1]] == player and board[cond[2]] == player:
            return True  # El jugador ha ganado
    return False  # No hay ganador


def check_tie(board):
    """
    Verifica si el juego ha terminado en empate.
    (Si no hay ganador y no quedan casillas libres).
    """
    if not check_win(board, 'X') and not check_win(board, 'O') and len(get_free_squares(board)) == 0:
        return True
    return False


def user_move(board):
    """
    Pide al usuario su movimiento y lo valida.
    """
    while True:
        try:
            move = int(input("Ingresa tu movimiento (1-9): "))

            if move < 1 or move > 9:
                print("Error: El número debe ser entre 1 y 9.")
            elif board[move] in ['X', 'O']:
                print("Error: Esa casilla ya está ocupada.")
            else:
                board[move] = 'O'  # Coloca la 'O' del usuario
                break
        except ValueError:
            print("Error: Debes ingresar un número.")


def machine_move(board):
    """
    La máquina elige una casilla vacía al azar.
    """
    # 1. Obtener la lista de casillas libres
    free_squares = get_free_squares(board)

    # 2. Elegir una al azar
    move = random.choice(free_squares)

    # 3. Colocar la 'X' de la máquina
    board[move] = 'X'
    print(f"La máquina eligió la casilla {move}")


def play_game():
    """
    Función principal que ejecuta el juego.
    """
    print("¡Bienvenido al Tic-Tac-Toe!")

    # Creamos el tablero. Usamos 10 elementos para que el índice coincida con el número.
    # Llenamos con números (como strings) para que sea más fácil de ver.
    board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # --- REGLA 4: El primer movimiento es de la máquina en el centro ---
    print("La máquina (X) juega primero en el centro.")
    board[5] = 'X'
    display_board(board)

    # Bucle principal del juego
    while True:

        # --- TURNO DEL USUARIO (O) ---
        print("\n--- Es tu turno (O) ---")
        user_move(board)
        display_board(board)

        # Verificar estado del juego
        if check_win(board, 'O'):
            print("¡Felicidades, has ganado!")
            break
        if check_tie(board):
            print("¡El juego es un empate!")
            break

        # --- TURNO DE LA MÁQUINA (X) ---
        print("\n--- Turno de la máquina (X) ---")
        machine_move(board)
        display_board(board)

        # Verificar estado del juego
        if check_win(board, 'X'):
            print("¡La máquina ha ganado!")
            break
        if check_tie(board):
            print("¡El juego es un empate!")
            break


# --- Iniciar el juego ---
play_game()