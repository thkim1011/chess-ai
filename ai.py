"""
ai.py -- Defines functions for running minimax and minimax with alpha beta pruning.
"""

from chess import *


def minimax(board, depth, turn):
    if depth == 0:
        return board.compute_score(turn), None

    maximum = -10000
    best_move = None
    for m in board.get_moves(turn):
        if m[1].in_check(turn):
            continue
        opp_score, _ = minimax(m[1], depth - 1, 1 - turn)
        if -opp_score > maximum:
            maximum = -opp_score
            best_move = m[0]
    return maximum, best_move


def minimax_with_pruning(board, depth, alpha, beta, turn):
    if depth == 0:
        return board.compute_score(turn), None
    maximum = -10000
    best_move = None
    for m in board.get_moves(turn):
        if m[1].in_check(turn):
            continue
        opp_score, _ = minimax_with_pruning(m[1], depth - 1,
                                            -beta, -alpha, 1 - turn)
        if -opp_score > maximum:
            maximum = -opp_score
            best_move = m[0]
        alpha = max(alpha, -opp_score)
        if alpha >= beta:
            return maximum, best_move
    return maximum, best_move
