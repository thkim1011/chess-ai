# Chess Board and Pieces

# Import


# Functions
def locate(pos_str):
    """
    Gives the position based on the string. In this program, all positions
    are represented as tuples in the form (ROW, COLUMN) of the array. 
    This function aims to ease the use of positions within this program.
    >>> locate("a1")
    (0, 0)
    >>> locate("a2")
    (1, 0)
    >>> locate("a3")
    (2, 0)
    >>> locate("e4")
    (3, 4)
    >>> locate("f8")
    (7, 5)
    >>> locate("g8")
    (7, 6)
    >>> locate("h8")
    (7, 7)
    """
    return ("12345678".index(pos_str[1]), "abcdefgh".index(pos_str[0]))

# TODO: Change tuple position to string position in doctest.
def piece_is_blocked_straight(piece, position):
    """
    Returns True if the straight path of piece to position is blocked.
    It does not check for whether there is a piece at the final destination
    since a move may be a valid attack. In addition, if position is not a
    straight movement of the initial, then True is returned since the piece
    is "blocked"
    >>> board = Board()
    >>> pawn1 = board.get_piece((1, 0))
    >>> piece_is_blocked_straight(pawn1, (3, 0))
    False
    >>> piece_is_blocked_straight(pawn1, (1, 1))
    False
    >>> piece_is_blocked_straight(pawn1, (6, 0))
    False
    >>> piece_is_blocked_straight(pawn1, (7, 0))
    True
    """
    row_change = position[0] - piece.position[0]
    col_change = position[1] - piece.position[1]

    n = abs(row_change)
    m = abs(col_change)

    if n == 0 or m == 0:
        row_unit = 0 if n == 0 else row_change // n
        col_unit = 0 if m == 0 else col_change // m
        path_length = max(n, m)

        for i in range(1, path_length):
            if piece.board.has_piece((piece.position[0] + row_unit * i,
                piece.position[1] + col_unit * i)):
                return True
        return False
    return True
   
def piece_is_blocked_diagonal(piece, position):
    """
    Returns True if the diagonal path of piece to position is blocked.
    It does not check for whether there is a piece at the final destination
    since a move may be a valid attack. In addition, if position is not a
    diagonal movement of the initial, then True is returned since the piece
    is "blocked"
    >>> board = Board(empty=True)
    >>> queen = Queen("white")
    >>> board.add_piece(queen, locate("d1"))
    >>> board.add_piece(Pawn("black"), locate("h5"))
    >>> board.add_piece(Pawn("white"), locate("c2")) # Set up board
    >>> piece_is_blocked_diagonal(queen, locate("d1")) # Not valid move
    True
    >>> piece_is_blocked_diagonal(queen, locate("e2")) # Valid move
    False
    >>> piece_is_blocked_diagonal(queen, locate("f3")) # Valid move
    False
    >>> piece_is_blocked_diagonal(queen, locate("h5")) # Valid (see above)
    False
    >>> piece_is_blocked_diagonal(queen, locate("c2")) # Valid (see above)
    False
    >>> piece_is_blocked_diagonal(queen, locate("a4")) # Not valid move
    True
    >>> piece_is_blocked_diagonal(queen, locate("h1")) # Wrong move
    True
    >>> piece_is_blocked_diagonal(queen, locate("a2")) # Wrong move
    True
    """
    row_change = position[0] - piece.position[0]
    col_change = position[1] - piece.position[1]

    n = abs(row_change)
    m = abs(col_change)

    if n == m and n != 0:
        row_unit = row_change // n
        col_unit = col_change // m

        for i in range(1, n):
            if piece.board.has_piece((piece.position[0] + row_unit * i,
                piece.position[1] + col_unit * i)):
                return True
        return False
    return True

# Board class
class Board:
    def __init__(self, empty=False):
        """ 
        Constructs a board with pieces in initial position.
        If empty is True, then board will not have any pieces.
        >>> board = Board()
        >>> print(board.board[0][0].name)
        rook
        >>> print(board.board[0][0].color)
        white
        >>> print(board.board[0][1].name)
        knight
        >>> print(board.board[0][2].name)
        bishop
        >>> print(board.board[0][3].name)
        queen
        >>> print(board.board[0][4].name)
        king
        >>> print(board.board[7][0].color)
        black
        """

        self.board = []
        self.pieces = []
        
        for _ in range(8):
            self.board.append([None] * 8)

        if not empty:
            # Populate board
            self.add_piece(Rook("white"), (0, 0))
            self.add_piece(Knight("white"), (0, 1))
            self.add_piece(Bishop("white"), (0, 2))
            self.add_piece(Queen("white"), (0, 3))
            self.add_piece(King("white"), (0, 4))
            self.add_piece(Bishop("white"), (0, 5))
            self.add_piece(Knight("white"), (0, 6))
            self.add_piece(Rook("white"), (0, 7))

            self.add_piece(Rook("black"), (7, 0))
            self.add_piece(Knight("black"), (7, 1))
            self.add_piece(Bishop("black"), (7, 2))
            self.add_piece(Queen("black"), (7, 3))
            self.add_piece(King("black"), (7, 4))
            self.add_piece(Bishop("black"), (7, 5))
            self.add_piece(Knight("black"), (7, 6))
            self.add_piece(Rook("black"), (7, 7))
        
            for i in range(8):
                self.add_piece(Pawn("white"), (1, i))
                self.add_piece(Pawn("black"), (6, i))

    def __str__(self):
        """
        Prints the board in the usual way.
        >>> print(Board())
            a   b   c   d   e   f   g   h
           --- --- --- --- --- --- --- ---
        8 | R | N | B | Q | K | B | N | R |
           --- --- --- --- --- --- --- ---
        7 | P | P | P | P | P | P | P | P |
           --- --- --- --- --- --- --- ---
        6 |   |   |   |   |   |   |   |   |
           --- --- --- --- --- --- --- ---
        5 |   |   |   |   |   |   |   |   |
           --- --- --- --- --- --- --- ---
        4 |   |   |   |   |   |   |   |   |
           --- --- --- --- --- --- --- ---
        3 |   |   |   |   |   |   |   |   |
           --- --- --- --- --- --- --- ---
        2 | p | p | p | p | p | p | p | p |
           --- --- --- --- --- --- --- ---
        1 | r | n | b | q | k | b | n | r |
           --- --- --- --- --- --- --- ---
            a   b   c   d   e   f   g   h
        """
        alpha = "abcdefgh"
        alpha_line = " "
        for i in alpha:
            alpha_line += "   " + i
        board = alpha_line

        border = "\n  " + " ---" * 8
        board += border
        for i in range(8, 0, -1):
            line = "\n{0} |".format(i)
            for j in self.board[i - 1]:
                if j is None:
                    line += "   |"
                elif j.color == "white":
                    line += " " + j.char.lower() + " |"
                else:
                    line += " " + j.char + " |"
            board += line
            board += border
        board += "\n" + alpha_line
        return board

    def get_piece(self, position):
        """
        Gets piece on board at given position.
        >>> board = Board()
        >>> board.get_piece((1, 0)).name
        'pawn'
        >>> board.get_piece((0, 0)).name
        'rook'
        >>> board.get_piece((0, 1)).name
        'knight'
        >>> board.get_piece((0, 1)).board is board
        True
        >>> board.get_piece((0, 1)).position == (0, 1)
        True
        """
        return self.board[position[0]][position[1]]

    def add_piece(self, piece, position):
        """
        Adds piece on board at given position.
        >>> board = Board(empty=True)
        >>> board.add_piece(Pawn("white"), (3, 3))
        >>> pawn = board.get_piece((3, 3))
        >>> pawn.name
        'pawn'
        >>> pawn.position
        (3, 3)
        >>> pawn.board is board
        True
        >>> pawn in board.pieces
        True
        """
        self.board[position[0]][position[1]] = piece
        piece.position = position
        piece.board = self
        self.pieces.append(piece)       

    def has_piece(self, position):
        """
        Returns whether board has some piece at position.
        >>> board = Board(empty=True)
        >>> board.has_piece((4, 4))
        False
        >>> board.add_piece(Pawn("white"), (4, 4))
        >>> board.has_piece((4, 4))
        True
        >>> board.has_piece((4, 5))
        False
        """
        return self.get_piece(position) is not None

    def move_piece(self, initial, final):
        """
        Moves piece from initial to final position. Naturally,
        if there is no piece on initial, nothing happens.
        >>> board = Board()
        >>> bishop = board.get_piece((0, 2))
        >>> bishop.position
        (0, 2)
        >>> bishop.name
        'bishop'
        >>> board.move_piece((0, 2), (5, 5))
        >>> bishop.position
        (5, 5)
        >>> board.get_piece((5, 5)) is bishop
        True
        >>> board.get_piece((0, 2)) is None
        True
        """
        piece = self.get_piece(initial)
        self.board[final[0]][final[1]] = piece
        self.board[initial[0]][initial[1]] = None
        piece.position = final
        
    def remove_piece(self, position):
        """
        Removes piece from position
        and returns a pointer to it.
        >>> board = Board()
        """
            
    def make_move(self, move):
        """
        TODO: Figure out details.
        Makes a move. Algorithm involved is most likely
        1) Check if checkmate?
        2) Check if move solves situation
        3) If not, then calls piece.is_valid(move.position)
        """
        try:
            if move.piece.is_valid(move.position):
                self.move_piece(move.piece.position, move.position)
                print(self)
        except ValueError:
            print("Invalid move. Try again")

   
# Move class
class Move:
    def __init__(self, piece, position):
        self.piece = piece
        self.position = position

# Pieces
class Piece:
    def __init__(self, color, position=None, board=None):
        assert color == "black" or color == "white"
        self.color = color
        self.position = position
        self.board = board

# TODO figure out en passant
class Pawn(Piece):
    name = "pawn"
    char = "P"

    def __init__(*args):
        """ Constructs a pawn.
        >>> pawn = Pawn("black", (1, 0))
        >>> pawn.name
        'pawn'
        >>> pawn.color
        'black'
        >>> pawn.position
        (1, 0)
        """
        Piece.__init__(*args) 

    def is_valid(self, position):
        """
        Given a position to move to, validates the move based on board.
        >>> board = Board(empty=True)
        >>> pawn1 = Pawn("white", (1, 3), board)
        >>> pawn2 = Pawn("black", (6, 4), board)
        >>> board.add_piece(pawn1, (1, 3))
        >>> board.add_piece(pawn2, (6, 4))
        >>> pawn1.is_valid((2, 3))
        True
        >>> pawn1.is_valid((3, 3))
        True
        >>> pawn1.is_valid((4, 3))
        False
        >>> board.move_piece((1, 3), (3, 3))
        >>> pawn1.is_valid((4, 3))
        True
        >>> pawn1.is_valid((5, 3))
        False
        >>> pawn2.is_valid((5, 4))
        True
        >>> pawn2.is_valid((4, 4))
        True
        >>> pawn2.is_valid((3, 4))
        False
        >>> board.move_piece((6, 4), (4, 4))
        >>> pawn1.is_valid((4, 4))
        True
        """
        if self.color == "white":
            # Forward 1
            if position[0] == self.position[0] + 1\
                    and position[1] == self.position[1]\
                    and not self.board.has_piece(position):
                return True
            # Forward 2
            elif position[0] == 3\
                    and self.position[0] == 1\
                    and position[1] == self.position[1]\
                    and not self.board.has_piece((2, position[1]))\
                    and not self.board.has_piece(position):
                return True
            # Attack
            elif position[0] == self.position[0] + 1\
                    and (position[1] == self.position[1] - 1
                        or position[1] == self.position[1] + 1)\
                    and self.board.has_piece(position)\
                    and self.board.get_piece(position).color == "black":
                return True
        else:
            # Forward 1
            if position[0] == self.position[0] - 1\
                    and position[1] == self.position[1]\
                    and not self.board.has_piece(position):
                return True
            # Forward 2
            elif position[0] == 4\
                    and self.position[0] == 6\
                    and position[1] == self.position[1]\
                    and not self.board.has_piece((5, position[1]))\
                    and not self.board.has_piece(position):
                return True
            # Attack
            elif position[0] == self.position[0] - 1\
                    and (position[1] == self.position[1] - 1
                        or position[1] == self.position[1] + 1)\
                    and self.board.has_piece(position)\
                    and self.board.get_piece(position).color == "white":
                return True
        return False
    
    def valid_moves(self):
        """
        Outputs a list of possible moves.
        """

class Bishop(Piece):
    name = "bishop"
    char = "B"
    def __init__(*args):
        Piece.__init__(*args)

    def is_valid(self, position):
        """
        Returns True if move to position is valid
        >>> board = Board()
        >>> board.move_piece(locate("e2"), locate("e4")) # Move ally pawn up
        >>> bishop = board.get_piece(locate("f1"))
        >>> bishop.is_valid(locate("b5")) # Valid move
        True
        >>> board.move_piece(locate("b7"), locate("b5")) # Move enemy pawn up
        >>> bishop.is_valid(locate("b5")) # Not correct
        True
        >>> bishop.is_valid(locate("g2")) # Blocked
        False
        >>> bishop.is_valid(locate("h3")) # Blocked again
        False
        >>> bishop.is_valid(locate("h4")) # Not a diagonal
        False
        """
        if piece_is_blocked_diagonal(self, position):
            return False
        if self.board.has_piece(position) and\
                self.board.get_piece(position).color == self.color:
            return False
        return True

class Knight(Piece): 
    name = "knight"
    char = "N"
    def __init__(*args):
        Piece.__init__(*args)

class Rook(Piece):
    name = "rook"
    char = "R"
    def __init__(*args):
        Piece.__init__(*args)

class Queen(Piece):
    name = "queen"
    char = "Q"
    def __init__(*args):
        Piece.__init__(*args)

class King(Piece):
    name = "king"
    char = "K"
    def __init__(*args):
        Piece.__init__(*args)
