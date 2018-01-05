from chess import *

# TODO: Add more doctests
# TODO: Make code better
def process(str_move, board):
    """
    Takes in move from user and processes it. Validity of move
    is not checked by this function.

    A proposal for a better algorithm:
    1) tokenize string
    2) process individually
    >>> board = Board()
    >>> process("0-0", board)
    King('white', (0, 4)) to (0, 7)
    >>> process("0-0-0", board)
    Queen('white', (0, 3)) to (0, 0)
    >>> process("e4", board)
    Pawn('white', (1, 4)) to (3, 4)
    >>> process("Nc3", board)
    Knight('white', (0, 1)) to (2, 2)
    """

    # Identify piece
    if str_move[0] in ["R", "N", "B", "Q", "K"]:
        piece_char = str_move[0]
    else:
        piece_char = "P"

    # Identify location
    # TODO: Fix since not necessarily true
    position = ("12345678".index(str_move[-1]), "abcdefgh".index(str_move[-2]))

    # Disambiguate
    # TODO: Add

    # Get all possible pieces
    possible_pieces = [piece for piece in board.pieces 
            if piece.is_valid(position)\
            and piece.char == piece_char]

    if len(possible_pieces) != 1:
        raise ValueError("Your move specifies {0} possible moves.".format(
            len(possible_pieces)))
    return Move(possible_pieces[0], position)

# Move class
class Move:
    def __init__(self, piece, position):
        self.piece = piece
        self.position = position

    def __str__(self):
        return "{0} to {1}".format(self.piece, self.position)

    def __repr(self):
        return str(self)

class Game:
    def __init__(self):
        """
        Starts a game instance.
        """
        self.board = Board()
        
        print(" ------------------")
        print("| Welcome to Chess |")
        print(" ------------------")

        while True:
            print(self.board)
            print("Player {0}'s turn".format(self.board.turn))
            move = process(input("Make your move: "), self.board)
            self.board.make_move(move)
