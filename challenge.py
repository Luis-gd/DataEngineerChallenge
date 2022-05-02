import numpy as np


class World:

# not_self_intersection: funcion que comprueba la no intersección de 
# la serpiente con ella misma. Recibe una serpiente.
    def not_self_intersection(self, snake):
        iterator = 0
        different = True
        while iterator < snake.shape[0] and different:
            for i in snake[:iterator]:
                if i[0] == snake[iterator][0] and i[1] == snake[iterator][1]: 
                    different = False

            for i in snake[iterator+1:]:
                if i[0] == snake[iterator][0] and i[1] == snake[iterator][1]: 
                    different = False
            iterator += 1
        return different
# not_crossing_board: funcion que comprueba que no se salga la serpiente
# del tablero. Recibe una serpiente y un tablero.
    def not_crossing_board(self, snake, board):
        return np.all([ 0 <= item[0] < board[0] and 
            0 <= item[1] < board[1] for item in snake])


# valid_board: Función que se asegura de que se cumplen los criterios
# indicados del tablero. Recibe un rablero.
    def valid_board(self, board):
        valid = True
        if not isinstance(board, list):
            valid = False

        elif len(board) != 2:
            valid = False
        
        elif not all([ 1 <= item <= 10 for item in board]):
            valid = False
        
        return valid


# consecutives 
    def consecutives(self, snake):
        iterator = 0
        consecutive_couples = True
        while iterator < snake.shape[0]-1 and consecutive_couples:
            # Se comprueba que sean consecutivos horizontalmente (eje x)
            horizontal_consecutive = (snake[iterator][1] == snake[iterator+1][1]
            and snake[iterator+1][0] in range(snake[iterator][0]-1
                ,snake[iterator+1][0]+1))
            # Se comprueba que sean consecutivos verticalmente (eje y)
            vertical_consecutive = (snake[iterator][0] == 
                snake[iterator+1][0] and snake[iterator+1][1] in 
                range(snake[iterator][1]-1,snake[iterator+1][1]+1))
            if not horizontal_consecutive and not vertical_consecutive:
                consecutive_couples = False
            
            iterator += 1
        return consecutive_couples

# valid_snake: Función que se asegura de que se cumplen los criterios
# indicados de la serpiente. Recibe un rablero.
    def valid_snake(self, snake):
        valid = True
        if not isinstance(snake, np.ndarray):
            valid = False

        elif not (3 <= len(snake) <= 7):
            valid = False

        elif not self.not_crossing_board(snake, self.board):
            valid = False
        
        elif not consecutives(snake):
            valid = False

        return valid

    def valid_depth(self, depth):
        valid = True
        if not isinstance(depth, int):
            valid = False

        elif not (1 <= depth <= 20):
            valid = False
        
        return valid

# Inicializa el objeto mundo, el cual contiene a la serpiente y al tablero
    def __init__(self, snake, board, depth):
        if self.valid_board(board):
            self.board = board
        else:
            print("El tablero introducido no cumple los requisitos.")
        if  self.valid_snake(snake):
            self.snake = snake
        else: 
            print("La serpiente introducida no cumple los requisitos.")
        if self.valid_depth(depth):
            self.depth = depth
        else:
            print("La profundidad de los pasos no cumple los requisitos.")

    
        
    