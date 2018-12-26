"""
ai.py -- Defines functions for running minimax and minimax with alpha beta pruning.
"""

from chess import *
import math

gamma = 0.99

def minimax(board, depth, turn, heuristic=None):
    if depth == 0:
        return board.compute_score(turn), None

    maximum = -10000
    best_move = None
    for move, b in board.get_moves(turn, heuristic):
        if b.in_check(turn):
            continue
        opp_score, prev_move = minimax(b, depth - 1, 1 - turn)
        opp_score *= gamma # Make sooner checkmates higher worth
        if -opp_score >= maximum:
            maximum = -opp_score
            best_move = move
            best_move.next = prev_move
    return maximum, best_move


def minimax_with_pruning(board, depth, 
        turn, alpha=-math.inf, beta=math.inf, 
        heuristic=None):
    if depth == 0:
        return board.compute_score(turn), None
    maximum = -10000
    best_move = None
    for move, b in board.get_moves(turn):
        if b.in_check(turn):
            continue
        opp_score, prev_move = minimax_with_pruning(b, depth - 1,
                                                    -beta, -alpha, 1 - turn, heuristic)
        if -opp_score > maximum:
            maximum = -opp_score
            best_move = move
            best_move.next = prev_move
        alpha = max(alpha, -opp_score)
        if alpha >= beta:
            break
    return maximum, best_move
