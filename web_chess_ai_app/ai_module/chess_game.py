import chess
import chess.svg
import chess.engine
import chess_ai



def get_player_input():
    """
    Interfaces with GUI modules to get player input and return a move
    """
    # Get move from player
    print('Make a move')
    from_square = input('From_square: ')
    to_square = input('To_square: ')

    # Parse move into square indices
    square_indices = get_move_squares(from_square.lower(), to_square.lower())

    # Generate move from indices
    move = chess.Move(from_square=square_indices[0], to_square=square_indices[1])
    return move

def get_move_squares(from_square, to_square):
    try:
        squares = [from_square, to_square] # list to hold int values of squares as# defined in the py-chess docs.
        indices = []
        file_index = 0
        rank_index = 0

        for square in squares:
            for file in chess.FILE_NAMES:
                if file == square[0]:  # if file matches input
                    file_index = chess.FILE_NAMES.index(file)
                    break

            rank_index = int(square[1]) - 1 
        
            square_int = chess.square(file_index=file_index, rank_index=rank_index)
            indices.append(square_int)

        return indices

    except Exception as e:
        print('Invalid input. Enter a file-rank pairs e.g. A2 or b5 \n')
        move = get_player_input()
        indices = [move.from_square, move.to_square]

        return indices


def game_over(turn, result):
    """
    Display winner using GUI.
    Give option to restart game.
    if restart:
        initialize game
    """
    winner = change_turns(turn)
    print('Results \n' + result)
    response = input('Play Again? Y or N : ')
    # response = user_input from GUI
    if response == 'Y':
        run_game()


def change_turns(turn):
    if turn == chess.WHITE:
        turn = chess.BLACK
    elif turn == chess.BLACK:
        turn = chess.WHITE

    return turn


def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if depth ==0 or board.is_game_over():
        return chess_ai.evaluate_board(board), None

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth - 3, alpha, beta, False)[0]
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if alpha >= beta:
                break
        return max_eval, best_move

    else:
        min_eval = float('inf')
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth + 3, alpha, beta, True)[0]
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if alpha >= beta:
                break
        return min_eval, best_move


def run_game():
    """
    Main game loop
    """
    board = chess.Board()
    turn = chess.WHITE
    while not board.is_game_over():
        if turn == chess.WHITE:
            move = get_player_input()
            if move in board.legal_moves:
                board.push(move)
                turn = change_turns(turn)
            else:
                print('Illegal move')
       
#start
run_game()









