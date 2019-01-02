from chess.chess import *

# TODO: Add more doctests
# TODO: Make code better
# TODO: Use tokenized array to solve problem.
def process(str_move, board, turn):
    """
    Takes in move from user and processes it. Validity of move
    is not checked by this function.

    A proposal for a better algorithm:
    1) tokenize string
    2) process individually
    >>> board = Board()
    >>> process("0-0", board, "white")
    King('white', (0, 4)) to (0, 7)
    >>> process("0-0-0", board, "white")
    Queen('white', (0, 3)) to (0, 0)
    >>> process("e4", board, "white")
    Pawn('white', (1, 4)) to (3, 4)
    >>> process("Nc3", board, "white")
    Knight('white', (0, 1)) to (2, 2)
    """

    if str_move == "0-0":
        pass
    if str_move == "0-0-0":
        pass


    # Tokenize
    tokenized = []
    for i in str_move:
        if i in "1234567890":
            tokenized[-1] += i
        else:
            tokenized.append(i)
    
    piece_char = None
    d_file = None
    d_rank = None
    for i in tokenized:
        if len(i) == 1:
            if i == "x":
                continue
            if i in "abcdefgh":
                d_rank = i
            if i in ["R", "N", "B", "Q", "K"]:
                piece_char = i
        if len(i) == 2:
            if i[0:1] in ["R", "N", "B", "Q", "K"]:
                piece_char = i
                d_file = i[1:2]
            if i[0] in "abcdefgh" and i[1] in "12345678":
                position = locate(i)
    if piece_char is None:
        piece_char = "P"

    # Get all possible pieces
    possible_pieces = [piece for piece in board.pieces[turn] 
            if piece.is_valid(position)\
            and piece.char == piece_char]
    if d_file is not None:
        possible_pieces = [piece for piece in possible_pieces
                if "12345678"[piece.position.row] == d_file]
    if d_rank is not None:
        possible_pieces = [piece for piece in possible_pieces
                if "abcdefgh"[piece.position.col] == d_rank]
    if len(possible_pieces) != 1:
        raise ValueError("Your move specifies {0} possible moves.".format(
            len(possible_pieces)))
    return Move(possible_pieces[0], position)

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
