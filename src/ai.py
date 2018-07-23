from chess import *

def minimax(board, depth, turn):
    if depth == 0:
        return board.compute_score(turn), None

    maximum = -10000
    best_move = None
    for i in range(8):
        for j in range(8):
            piece = board.board[i][j]
            if piece == None:
                continue
            for position in piece.valid_pos(board):
                new_board = board.copy()
                new_board.move_piece(new_board.get_piece(piece.position), position)
                if new_board.in_check(turn):
                    continue
                opp_score, move = minimax(new_board, depth - 1,
                    1 - turn)
                if -opp_score > maximum:
                    maximum = -opp_score
                    best_move = Move(piece, position)
    return maximum, best_move

def minimax_with_pruning(board, depth, alpha, beta, turn):
    if depth == 0:
        return board.compute_score(turn), None
    maximum = -10000
    best_move = None
    for i in range(8):
        for j in range(8):
            piece = board.board[i][j]
            if piece == None:
                continue
            for position in piece.valid_pos(board):
                new_board= board.copy()
                new_board.move_piece(new_board.get_piece(piece.position), position)
                if new_board.in_check(turn):
                    continue
                opp_score, move = minimax_with_pruning(new_board, depth - 1,
                        beta, alpha, 1 - turn)
                if -opp_score > maximum:
                    maximum = -opp_score
                    best_move = Move(piece, position)
                if alpha >= beta:
                    return maximum, best_move
    return maximum, best_move


