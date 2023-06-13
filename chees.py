import chess 
import time
import numpy as np
# تعريف دالة تقييم الوضع الحالي

def evaluate_board(board):
    # تحديد القيم لكل قطعة
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }
    score = 0
    # حساب ميزان المواد
    for square, piece in board.piece_map().items():
        value = piece_values[piece.piece_type]
        if piece.color == chess.WHITE:
            score += value
        else:
            score -= value
    # إضافة مكافآت/عقوبات استنادًا إلى مواقع القطع
    for square, piece in board.piece_map().items():
        if piece.color == chess.WHITE:
            if piece.piece_type == chess.PAWN:
                score += 10 + (7 - chess.square_distance(square, chess.E2))
            elif piece.piece_type == chess.KNIGHT:
                score += 30 + len(board.attacks(square))
            elif piece.piece_type == chess.BISHOP:
                score += 30 + len(board.attacks(square))
            elif piece.piece_type == chess.ROOK:
                score += 50 + len(board.attacks(square))
            elif piece.piece_type == chess.QUEEN:
                score += 90 + len(board.attacks(square))
            elif piece.piece_type == chess.KING:
                score += 900 + len(board.attacks(square))
        else:
            if piece.piece_type == chess.PAWN:
                score -= 10 + (chess.square_distance(square, chess.E7))
            elif piece.piece_type == chess.KNIGHT:
                score -= 30 + len(board.attacks(square))
            elif piece.piece_type == chess.BISHOP:
                score -= 30 + len(board.attacks(square))
            elif piece.piece_type == chess.ROOK:
                score -= 50 + len(board.attacks(square))
            elif piece.piece_type == chess.QUEEN:
                score -= 90 + len(board.attacks(square))
            elif piece.piece_type == chess.KING:
                score -= 900 + len(board.attacks(square))
    return score

def alpha_betaMinMaxL(board, depth, alpha, beta, maximizing_player=True):
    # Check if the maximum depth has been reached or if the game is over
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    # Evaluate all legal moves and store them in a list with their scores
    moves_scores = []
    for move in board.legal_moves:
        board.push(move)
        score = evaluate_heuristic(board)
        moves_scores.append((move, score))
        board.pop()

    # Sort the list of moves based on their scores
    moves_scores.sort(key=lambda x: x[1], reverse=maximizing_player)

    # Loop through the selected moves and evaluate them using alpha-beta
    for move, score in moves_scores:
        board.push(move)
        val = alpha_betaMinMaxL(board, depth-1, alpha, beta, not maximizing_player)
        board.pop()

        # Update the best score and alpha/beta values
        if maximizing_player:
            alpha = max(alpha, val)
            if alpha >= beta:
                break
        else:
            beta = min(beta, val)
            if beta <= alpha:
                break

    # Return the best score for the current player
    return alpha if maximizing_player else beta

def evaluate_heuristic(board):
    # Evaluate the board using a heuristic function
    # Here we use a simple evaluation function based on the difference in piece counts
    piece_count = np.array([len(board.pieces(piece_type, True)) - len(board.pieces(piece_type, False)) for piece_type in (chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN, chess.KING)])
    return np.sum(piece_count)

def alpha_beta_MinMaxbest(board, depth, alpha, beta, k, maximizing_player=True):
    # Check if the maximum depth has been reached or if the game is over
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    # Evaluate all legal moves and store them in a list with their scores
    moves_scores = []
    for move in board.legal_moves:
        board.push(move)
        score = evaluate_heuristic(board)
        moves_scores.append((move, score))
        board.pop()

    # Sort the list of moves based on their scores
    moves_scores.sort(key=lambda x: x[1], reverse=maximizing_player)

    # Select the top k moves to explore further
    moves_scores = moves_scores[:k]

    # Loop through the selected moves and evaluate them using alpha-beta
    for move, score in moves_scores:
        board.push(move)
        val = alpha_beta_MinMaxbest(board, depth-1, alpha, beta, k, not maximizing_player)
        board.pop()

        # Update the best score and alpha/beta values
        if maximizing_player:
            alpha = max(alpha, val)
            if alpha >= beta:
                break
        else:
            beta = min(beta, val)
            if beta <= alpha:
                break

    # Return the best score for the current player
    return alpha if maximizing_player else beta

# Define a transposition table to store board evaluations
transposition_table = {}

# Define a history table to store move history
history_table = {}

# Define the number 
def play(board_fen):
    # Create a chess board object from the FEN notation
    board = chess.Board(board_fen)

    # Set the initial values
    depth = 2
    alpha = float('-inf')
    beta = float('inf')

    # Choose the first move as a random legal move
    move = list(board.legal_moves)[0]

    # Loop through the legal moves and evaluate them using alpha-beta with move ordering
    for legal_move in board.legal_moves:
        board.push(legal_move)

        # Use transposition table to retrieve previous evaluations
        if board.fen() in transposition_table:
            score = transposition_table[board.fen()]
        else:
            # Use history heuristic to order moves
            history_score = 0
            if board.fen() in history_table:
                history_score = history_table[board.fen()]
            score = alpha_beta_MinMaxbest(board, depth-1, alpha, beta, True, history_score)
            transposition_table[board.fen()] = score

        board.pop()

        # If the score is better than the current best score, update the best move and score
        if score > alpha:
            alpha = score
            move = legal_move

    # Make the selected move on the board
    board.push(move)

def play_move(board, depth, k):
    # Print the current board position
    print(board)

    # Check if the game is over
    if board.is_game_over():
        print("Game over")
        return

    # Determine which player's turn it is
    if board.turn == chess.WHITE:
        player_name = "White"
    else:
        player_name = "Black"

    # Prompt the player for their move
    uci = input(player_name + " to move (UCI): ")

    # Make sure the move is legal
    try:
        move = chess.Move.from_uci(uci)
        if move not in board.legal_moves:
            raise ValueError()
    except:
        print("Invalid move")
        play_move(board, depth, k)
        return

    # Apply the player's move
    board.push(move)

    # Check if the game is over
    if board.is_game_over():
        print(board)
        print("Game over")
        return

    # Determine which player's turn it is
    if board.turn == chess.WHITE:
        player_name = "White"
    else:
        player_name = "Black"

    # Print the board after the player's move
    print(board)

    # Let the computer choose its move using MinMaxbest algorithm
    print("Computer is thinking...")
    best_move = None
    best_score = float('-inf')
    for move in board.legal_moves:
        board.push(move)
        score = alpha_beta_MinMaxbest(board, depth, float('-inf'), float('+inf'), k, False)
        board.pop()
        if score > best_score:
            best_move = move
            best_score = score
    # Apply the computer's move
    board.push(best_move)
    # Print the board after the computer's move
    print(board)
    # Play the next move
    play_move(board, depth, k)


def play_move_beta(board, depth, k):
    # Print the current board position
    print(board)
    # Check if the game is over
    if board.is_game_over():
        print("Game over")
        return
    # Determine which player's turn it is
    if board.turn == chess.WHITE:
        player_name = "White"
    else:
        player_name = "Black"
    # Prompt the player for their move
    uci = input(player_name + " to move (UCI): ")
    # Make sure the move is legal
    try:
        move = chess.Move.from_uci(uci)
        if move not in board.legal_moves:
            raise ValueError()
    except:
        print("Invalid move")
        play_move_beta(board, depth, k)
        return
    # Apply the player's move
    board.push(move)
    # Check if the game is over
    if board.is_game_over():
        print(board)
        print("Game over")
        return
    # Determine which player's turn it is
    if board.turn == chess.WHITE:
        player_name = "White"
    else:
        player_name = "Black"
    # Print the board after the player's move
    print(board)
    # Let the computer choose its move using BetaMinMaxL algorithm
    print("Computer is thinking...")
    best_move = None
    best_score = float('-inf')
    for move in board.legal_moves:
        board.push(move)
        score = alpha_betaMinMaxL(board, depth, k, False)
        board.pop()
        if score > best_score:
            best_move = move
            best_score = score
    # Apply the computer's move
    board.push(best_move)
    # Print the board after the computer's move
    print(board)
    # Play the next move
    play_move_beta(board, depth, k)


################################################################
# alpha_betaMinMaxL
# L = 2
# k = 5
# alpha = float('-inf')
# beta = float('inf')
# # Declare the chess board
# board = chess.Board()
# # Start the game
# n_moves = 0
# start_time = time.time()
# while not board.is_game_over():
#     # Get the legal moves
#     legal_moves = list(board.legal_moves)
#     best_move = None

#     if board.turn == chess.WHITE:
#         best_score = float('-inf')
#         for move in legal_moves:
#             board.push(move)
#             score = alpha_beta_MinMaxbest(board, L, alpha, beta, k, True)
#             board.pop()

#             if score > best_score:
#                 best_move = move
#                 best_score = score

#     else:
#         best_score = float('+inf')
#         for move in legal_moves:
#             board.push(move)
#             score = alpha_beta_MinMaxbest(board, L, alpha, beta, k, False)
#             board.pop()

#             if score < best_score:
#                 best_move = move
#                 best_score = score

#     # Make the move and update the board
#     board.push(best_move)
#     n_moves += 1
# # Print the final board position and the game result
# print("alpha_beta_MinMaxbest Execution time (seconds): " , round((time.time() - start_time), 2)) 
# print(board) 
# print(board.result() + " in " + str(n_moves) + " moves")

################################################################
#  alpha_beta_MinMaxbest
# L = 2
# alpha = float('-inf')
# beta = float('inf')
# # Declare the chess board
# board = chess.Board()
# # Start the game
# n_moves = 0
# start_time = time.time()
# while not board.is_game_over():
#      #Get the legal moves
#     legal_moves = list(board.legal_moves)
#     best_move = None

#     if board.turn == chess.WHITE:
#         best_score = float('-inf')
#         for move in legal_moves:
#             board.push(move)
#             score =alpha_betaMinMaxL(board, L, alpha, beta, True)
#             board.pop()
#             if score > best_score:
#                 best_move = move
#                 best_score = score
#     else:
#         best_score = float('+inf')
#         for move in legal_moves:
#             board.push(move)
#             score = alpha_betaMinMaxL(board, L, alpha, beta, False)
#             board.pop()
#             if score < best_score:
#                 best_move = move
#                 best_score = score
#      #Make the move and update the board
#     board.push(best_move)
#     n_moves += 1
#  #Print the final board position and the game result
# print("alpha_betaMinMaxL Execution time (seconds): ", round((time.time() - start_time), 2))
# print(board)
# print(board.result() + " in " + str(n_moves) + " moves")
################################################################
# alpha_beta_MinMaxbest aginst itself 
# Parameters
# L = 2
# k = 5
# alpha = float('-inf')
# beta = float('+inf')
# # Declare the chess board
# board = chess.Board()
# # Start the game
# n_moves = 0
# start_time = time.time()
# while not board.is_game_over():
#     legal_moves = list(board.legal_moves)
#     best_move = None

#     if board.turn == chess.WHITE:
#         best_score = float('-inf')
#         for move in legal_moves:
#             board.push(move)
#             score = alpha_beta_MinMaxbest(board, L, alpha, beta, k, True)
#             board.pop()
#             if score > best_score:
#                 best_score = score
#                 best_move = move
#     else:
#         for move in legal_moves:
#             best_score = float('+inf')
#             board.push(move)
#             score = alpha_beta_MinMaxbest(board, L, alpha, beta, k, False)
#             board.pop()
#             if score < best_score:
#                 best_score = score
#                 best_move = move
#     # Make the move and update the board
#     board.push(best_move)
#     n_moves += 1
# # Print the final board position and the game result
# print("alpha_beta_MinMaxbest Execution time (seconds): " , round((time.time() - start_time), 2))
# print(board) 
# print(board.result() + " in " + str(n_moves) + " moves")

################################################################
#  playin aginst alpha_beta_MinMaxbest using UCI
# board = chess.Board()
# play_move(board, depth=2, k=5)

################################################################
# playing aginst alpha_betaMinMaxL using UCi
# board = chess.Board()
# play_move_beta(board, depth=2, k=5)