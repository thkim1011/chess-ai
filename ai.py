from copy import deepcopy
from chess import *

def minimax(board, depth):
    minimum
    
    for piece in board.pieces:
        for position in piece.valid_pos():
            new_board = deepcopy(board)
            new_board.move_piece(piece, position):

def minimax_with_pruning(board, alpha, beta, depth):
    for piece in board.pieces:
        for move in piece.valid_moves():

