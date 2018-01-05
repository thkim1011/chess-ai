from copy import deepcopy
from chess import *

def minimax_with_pruning(board, alpha, beta):
    for piece in board.pieces:
        for move in piece.valid_moves():

