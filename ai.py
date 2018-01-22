from copy import deepcopy
from chess import *

def minimax(board, depth, turn):
    if depth == 0:
        return board.compute_score(turn), None

    maximum = -10000
    best_move = None
    for piece in board.pieces[turn]:
        for position in piece.valid_pos():
            new_board = deepcopy(board)
            new_board.move_piece(new_board.get_piece(piece.position), position)
            if new_board.in_check(turn):
                continue
            opp_score, move = minimax(new_board, depth - 1,
                "white" if turn =="black" else "black")
            if -opp_score > maximum:
                maximum = -opp_score
                best_move = Move(piece, position)
    return maximum, best_move

def minimax_with_pruning(board, depth, alpha, beta, turn):
    if depth == 0:
        return board.compute_score(turn), None
    maximum = -10000
    best_move = None
    for piece in board.pieces[turn]:
        for position in piece.valid_pos():
            new_board= deepcopy(board)
            new_board.move_piece(new_board.get_piece(piece.position), position)
            if new_board.in_check(turn):
                continue
            opp_score, move = minimax_with_pruning(new_board, depth - 1,
                    beta, alpha, "white" if turn == "black" else "black")
            if -opp_score > maximum:
                maximum = -opp_score
                best_move = Move(piece, position)
            if alpha >= beta:
                return maximum, best_move
    return maximum, best_move


