# Chess Board and Pieces

# Import
from copy import deepcopy

# Functions
def locate(pos_str):
    """
    Gives the position object based on the string. In this program, all 
    positions are represented by an instance of the Position class.
    This function aims to ease the use of positions within this program.
    >>> locate("a1")
    a1
    >>> locate("a2")
    a2
    >>> locate("a3")
    a3
    >>> locate("e4")
    e4
    >>> locate("f8")
    f8
    >>> locate("g8")
    g8
    >>> locate("h8")
    h8
    """
    return Position("12345678".index(pos_str[1]), "abcdefgh".index(pos_str[0]))

def piece_is_blocked_straight(piece, position):
    """
    Returns True if the straight path of piece to position is blocked.
    It does not check for whether there is a piece at the final destination
    since a move may be a valid attack. In addition, if position is not a
    straight movement of the initial, then True is returned since the piece
    is "blocked"
    >>> board = Board()
    >>> pawn1 = board.get_piece(locate("a2"))
    >>> piece_is_blocked_straight(pawn1, locate("a4"))
    False
    >>> piece_is_blocked_straight(pawn1, locate("b2"))
    False
    >>> piece_is_blocked_straight(pawn1, locate("a7"))
    False
    >>> piece_is_blocked_straight(pawn1, locate("a8"))
    True
    """
    row_change = position.row - piece.position.row
    col_change = position.col - piece.position.col

    n = abs(row_change)
    m = abs(col_change)

    if n == 0 or m == 0:
        row_unit = 0 if n == 0 else row_change // n
        col_unit = 0 if m == 0 else col_change // m
        path_length = max(n, m)

        for i in range(1, path_length):
            if piece.board.get_piece(piece.position + (row_unit * i, 
                col_unit * i)):
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
    row_change = position.row - piece.position.row
    col_change = position.col - piece.position.col

    n = abs(row_change)
    m = abs(col_change)

    if n == m and n != 0:
        row_unit = row_change // n
        col_unit = col_change // m

        for i in range(1, n):
            if piece.board.get_piece(piece.position + (row_unit * i, 
                col_unit * i)):
                return True
        return False
    return True

# Position class
class Position:
    def __init__(self, row, col):
        """ 
        Constructs a position with row and col members.
        >>> pos = Position(3, 2)
        >>> pos.row
        3
        >>> pos.col
        2
        """
        self.row = row
        self.col = col
    
    def __str__(self):
        """
        Returns the chess board representation of position.
        >>> print(Position(0, 0))
        a1
        >>> print(Position(3, 2))
        c4
        """
        return "abcdefgh"[self.col] + "12345678"[self.row]

    def __repr__(self):
        """
        Returns the chess board representation of position.
        >>> Position(0, 0)
        a1
        >>> Position(3, 2)
        c4
        """
        return str(self)

    def __add__(self, pair):
        """
        Returns the position translated by a pair indicating the
        change in row and change in column.
        >>> locate("a1") + (1, 1)
        b2
        >>> locate("c4") + (1, -1)
        b5
        """
        return Position(self.row + pair[0], self.col + pair[1])

    def __eq__(self, other):
        """
        Returns true if two position objects are equal.
        >>> locate("a1") == locate("a1")
        True
        >>> locate("c3") == locate("d5")
        False
        """
        return self.row == other.row and self.col == other.col

    def in_range(self):
        """
        Returns true if row and col are in range.
        >>> Position(1, 3).in_range()
        True
        >>> Position(8, 8).in_range()
        False
        """
        return 0 <= self.row and self.row < 8\
                and 0 <= self.col and self.col < 8

# Move class
class Move:
    def __init__(self, piece, position, kill=None, ep=False, castle=False):
        self.piece = piece
        self.position = position
        self.kill = kill

# Board class
class Board:
    def __init__(self, empty=False):
        """ 
        Constructs a board with pieces in initial position.
        If empty is True, then board will not have any pieces.

        There are some instance variables that are of importance.

        self.board is a two dimensional array that stores each of the pieces
        in their respective locations.

        self.pieces is a dictionary consisting of two keys "white" and "black"
        and the respective array of pieces that are within these categories.

        self.history is an array of the moves that have occurred so far. Any move
        is recorded by a call to the move_piece method. It is used by the
        undo_move method.

        self.en_passant points to the pawn that has moved two steps up and
        thus is "en passant"-able. That is, a pawn in the correct conditions
        may be able to take the pawn. 

        self.queen_side_castle is a dictionary consisting of two keys "white"
        and "black" which tells whether the respective king may castle through
        the queen's side.

        self.king_side_castle is a dictionary consisting of two keys "white"
        and "black" which tells whether the respective king may castle through
        his side.
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
        self.pieces = {"white": [], "black": []}
        self.kings = {}
        self.history = []
        self.en_passant = None
        self.queen_side_castle = {"white": True, "black": True}
        self.king_side_castle = {"white": True, "black": True}
        
        for _ in range(8):
            self.board.append([None] * 8)

        if not empty:
            # Populate board
            self.add_piece(Rook("white"), Position(0, 0))
            self.add_piece(Knight("white"), Position(0, 1))
            self.add_piece(Bishop("white"), Position(0, 2))
            self.add_piece(Queen("white"), Position(0, 3))
            self.add_piece(King("white"), Position(0, 4))
            self.add_piece(Bishop("white"), Position(0, 5))
            self.add_piece(Knight("white"), Position(0, 6))
            self.add_piece(Rook("white"), Position(0, 7))

            self.add_piece(Rook("black"), Position(7, 0))
            self.add_piece(Knight("black"), Position(7, 1))
            self.add_piece(Bishop("black"), Position(7, 2))
            self.add_piece(Queen("black"), Position(7, 3))
            self.add_piece(King("black"), Position(7, 4))
            self.add_piece(Bishop("black"), Position(7, 5))
            self.add_piece(Knight("black"), Position(7, 6))
            self.add_piece(Rook("black"), Position(7, 7))
        
            for i in range(8):
                self.add_piece(Pawn("white"), Position(1, i))
                self.add_piece(Pawn("black"), Position(6, i))

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
        >>> board.get_piece(locate("a2")).name
        'pawn'
        >>> board.get_piece(locate("a1")).name
        'rook'
        >>> board.get_piece(locate("b1")).name
        'knight'
        >>> board.get_piece(locate("b1")).board is board
        True
        >>> board.get_piece(locate("b1")).position == locate("b1")
        True
        """
        return self.board[position.row][position.col]

    def add_piece(self, piece, position):
        """
        Adds piece on board at given position.
        >>> board = Board(empty=True)
        >>> board.add_piece(Pawn("white"), locate("d4"))
        >>> pawn = board.get_piece(locate("d4"))
        >>> pawn.name
        'pawn'
        >>> pawn.position
        d4
        >>> pawn.board is board
        True
        >>> pawn in board.pieces["white"]
        True
        """
        self.board[position.row][position.col] = piece
        piece.position = position
        piece.board = self
        self.pieces[piece.color].append(piece)

        # Record King
        if piece.name == "king":
            self.kings[piece.color] = piece
    
    # TODO: Add more doctests and thoroughly describe what happens
    # in the docs.
    def move_piece(self, piece, position, ep=False, castle=False, promote=False):
        """
        Moves piece from initial to final position. Returns any piece that was
        killed by the move.

        The goal of this method is so that when we call move_piece on piece
        and position such that piece.is_valid(position) and not board.in_check()
        then the resulting game should be completely valid. The condition 
        that piece.is_valid is called separately relaxes some of the rules 
        and allows for moving pieces in a free style.

        The analogy could be made that move_piece is to a real player moving
        chess pieces in an arbitrary fashion, while following the rules 
        leads to a valid chess game.

        In addition, board.in_check() should be called after the move is made
        since the move must be made in order to check for a check.

        Castling is an exception. When castling is specified, then 
        >>> board = Board()
        >>> bishop = board.get_piece(locate("c1"))
        >>> bishop.position
        c1
        >>> bishop.name
        'bishop'
        >>> board.move_piece(bishop, locate("f6"))
        >>> bishop.position
        f6
        >>> board.get_piece(locate("f6")) is bishop
        True
        >>> board.get_piece(locate("c1")) is None
        True
        """
        # En passant
        if piece.name == "pawn":
            unit = 1 if piece.color == "white" else -1
            start = 1 if piece.color == "white" else 6
            if piece.position.row == start and position.row == start + 2 * unit:
                self.en_passant = piece
        else:
            self.en_passant = None

        # Castling
        if piece.name == "king":
            self.queen_side_castle[piece.color] = False
            self.king_side_castle[piece.color] = False

        if piece.name == "rook" and piece.position.row == 0:
            self.queen_side_castle[piece.color] = False

        if piece.name == "rook" and piece.position.row == 7:
            self.king_side_castle[piece.color] = False
        
        # En passant
        if ep:
            if not isinstance(piece, Pawn):
                raise ValueError("only pawns may move en passant")
            target = self.get_piece(position + (-1, 0))
            if not target or target is not board.en_passant:
                raise ValueError("move is not en passant")
            target.remove_piece(target)

        if castle:
            if not isinstance(piece, King):
                raise ValueError("only king may castle")
            row = 0 if piece.color == "white" else 7;
            if position.col == 3:
                if not self.queen_side_castle[piece.color]:
                    raise ValueError("cannot move since either rook or king\
                            has previously moved")
                if board.in_check(piece.color):
                    raise ValueError("cannot castle out of check")
                self.board[position.row][2] = piece
                self.board[position.row][3] = None
                if board.in_check(piece.color):
                    raise ValueError("cannot castle through check")
                self.board[position.row][

                board.move_piece(position + (0, -1))
                if board.in_check(




            elif position.col == 7:
            

        # Move piece
        target = self.get_piece(position)
        if target:
            self.remove_piece(target)
        self.board[position.row][position.col] = piece
        self.board[piece.position.row][piece.position.col] = None
        piece.position = position

        return target

    def remove_piece(self, piece):
        """
        Removes piece from board and returns a pointer to the piece.
        >>> board = Board()
        >>> piece = board.remove_piece(board.get_piece(locate("e2")))
        >>> board.get_piece(locate("e2")) is None
        True
        >>> piece in board.pieces["white"]
        False

        """
        self.board[piece.position.row][piece.position.col] = None
        piece.position = None
        piece.board = None
        self.pieces[piece.color].remove(piece)
    
    def undo_move(self):


    def in_check(self, color):
        """
        Returns true if the given player (color) is currently in check.
        >>> board = Board()
        >>> board.in_check("white")
        False
        >>> board.in_check("black")
        False
        >>> queen = board.get_piece(locate("d8"))
        >>> board.move_piece(queen, locate("e2"))
        Pawn('white', None)
        >>> board.in_check("white")
        True
        >>> board.in_check("black")
        False
        """
        opp = "black" if color == "white" else "white"
        for piece in self.pieces[opp]:
            if piece.is_valid(self.kings[color].position):
                return True
        return False
    
# Pieces
class Piece:
    def __init__(self, color, position=None, board=None):
        """
        Constructs a piece. A piece has several important instance variables.

        self.color is the piece's color.

        self.position is the piece's position, an instance of the Position class.

        self.board is the board that the piece belongs to.
        >>> piece = Piece("black", Position(0, 0), None)
        >>> piece.color
        'black'
        >>> piece.position
        a1
        >>> piece.board
        """
        assert color == "black" or color == "white"
        self.color = color
        self.position = position
        self.board = board

    def __str__(self):
        """
        Returns the string representation of Piece. It is given in
        the form "Piece_Name(color, position)". For example, a Rook object
        with color "black" and position a1 will be represented as
        "Rook("black", a1)".
        >>> print(Piece("black", Position(0, 0)))
        Piece('black', a1)
        >>> print(Piece("white", Position(7, 7)))
        Piece('white', h8)
        """
        return "{0}({1}, {2})".format(self.__class__.__name__, 
                repr(self.color), repr(self.position))

    def __repr__(self):
        """
        Returns the representation of Piece. It is the same as
        the __str__ method.
        >>> Piece("black", Position(0, 0))
        Piece('black', a1)
        """
        return Piece.__str__(self)

class Pawn(Piece):
    name = "pawn"
    char = "P"

    def __init__(*args):
        """ Constructs a pawn.
        >>> pawn = Pawn("black", locate("a2"))
        >>> pawn.name
        'pawn'
        >>> pawn.color
        'black'
        >>> pawn.position
        a2
        """
        Piece.__init__(*args)
    
    def is_valid(self, position):
        """
        Given a position to move to, validates the move based on board.
        >>> board = Board()
        >>> pawn1 = board.get_piece(locate("d2"))
        >>> pawn2 = board.get_piece(locate("e7"))
        >>> pawn3 = board.get_piece(locate("c7"))
        >>> pawn1.is_valid(locate("d3")) # Advance white pawn
        True
        >>> pawn1.is_valid(locate("d4"))
        True
        >>> pawn1.is_valid(locate("d5"))
        False
        >>> board.move_piece(pawn1, locate("d4"))
        >>> pawn1.is_valid(locate("d5")) # Advance white pawn
        True
        >>> pawn1.is_valid(locate("d6"))
        False
        >>> pawn2.is_valid(locate("e6")) # Advance black pawn
        True
        >>> pawn2.is_valid(locate("e5"))
        True
        >>> pawn2.is_valid(locate("e4"))
        False
        >>> board.move_piece(pawn2, locate("e5"))
        >>> pawn1.is_valid(locate("e5")) # Attack black pawn
        True
        >>> pawn2.is_valid(locate("d4")) # Attack white pawn
        True
        >>> board.move_piece(pawn1, locate("d5"))
        >>> board.move_piece(pawn3, locate("c5"))
        >>> pawn1.is_valid(locate("c6"))
        True
        """
        unit = 1 if self.color == "white" else -1
        start = 1 if self.color == "white" else 6
        target = self.board.get_piece(position)
        # Move one unit
        if position == self.position + (unit, 0) and not target:
            return True
        # Move two units
        if position == self.position + (2 * unit, 0)\
                and self.position.row == start\
                and not self.board.get_piece(self.position + (unit , 0))\
                and not target:
            return True
        # But most importantly, he attac
        if position == self.position + (unit, 1)\
                or position == self.position + (unit, -1):
            if target and target.color != self.color:
                return True
            mod_pos = position + (-unit, 0)
            if self.board.get_piece(mod_pos)\
                    and self.board.get_piece(mod_pos).color != self.color\
                    and self.board.get_piece(mod_pos) == self.board.en_passant:
                return True
        return False
    
    def valid_pos(self):
        """
        Outputs a list of valid positions to move to.
        >>> board = Board()
        >>> pawn1 = board.get_piece(locate("e2"))
        >>> pawn2 = board.get_piece(locate("d7"))
        >>> pawn1.valid_pos()
        [e3, e4]
        >>> pawn2.valid_pos()
        [d6, d5]
        >>> board.move_piece(pawn1, locate("e4"))
        >>> board.move_piece(pawn2, locate("d5"))
        >>> pawn1.valid_pos()
        [e5, d5]
        >>> pawn2.valid_pos()
        [d4, e4]
        """
        valid_pos = []
        unit = 1 if self.color == "white" else -1
        start = 1 if self.color == "white" else 6
        forward_one = self.position + (unit, 0)
        forward_two = self.position + (2 * unit, 0)
        
        # Move forward
        if not self.board.get_piece(forward_one):
            valid_pos.append(forward_one)
            if self.position.row == start\
                    and not self.board.get_piece(forward_two):
                valid_pos.append(forward_two)
        
        # Attack
        attack_pos = [self.position + (unit, -1), self.position + (unit, 1)]
        for p in attack_pos:
            ep = p + (-unit, 0)
            if self.board.get_piece(p)\
                    and self.board.get_piece(p).color != self.color:
                valid_pos.append(p)
            elif self.board.get_piece(ep)\
                    and self.board.get_piece(ep) is self.board.en_passant:
                valid_pos.append(p)

        return valid_pos


class Bishop(Piece):
    name = "bishop"
    char = "B"
    def __init__(*args):
        Piece.__init__(*args)

    def is_valid(self, position):
        """
        Returns True if move to position is valid.
        >>> board = Board()
        >>> pawn1 = board.get_piece(locate("e2"))
        >>> pawn2 = board.get_piece(locate("b7"))
        >>> bishop = board.get_piece(locate("f1"))
        >>> board.move_piece(pawn1, locate("e4")) # Move ally pawn up
        >>> bishop.is_valid(locate("b5")) # Valid move
        True
        >>> board.move_piece(pawn2, locate("b5")) # Move enemy pawn up
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
        target = self.board.get_piece(position)
        if target and target.color == self.color:
            return False
        return True

    def valid_pos(self):
        """
        Returns the possible position for self (bishop) to move.
        >>> board = Board()
        >>> bishop = board.get_piece(locate("f1"))
        >>> pawn = board.get_piece(locate("e2"))
        >>> bishop.valid_pos()
        []
        >>> board.move_piece(pawn, locate("e3"))
        >>> bishop.valid_pos()
        [e2, d3, c4, b5, a6]
        >>> board.move_piece(bishop, locate("d3"))
        >>> bishop.valid_pos()
        [e4, f5, g6, h7, c4, b5, a6, e2, f1]
        """
        valid_pos = []
        for unit in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            cur = self.position
            while True:
                cur = cur + unit
                if not cur.in_range():
                    break
                piece = self.board.get_piece(cur)
                if piece:
                    if piece.color != self.color:
                        valid_pos.append(cur)
                    break
                
                valid_pos.append(cur)
        return valid_pos

class Knight(Piece): 
    name = "knight"
    char = "N"
    def __init__(*args):
        Piece.__init__(*args)

    def is_valid(self, position):
        """
        Returns True if move to position is valid.
        >>> board = Board()
        >>> knight = board.get_piece(locate("b1"))
        >>> knight.is_valid(locate("b1"))
        False
        >>> knight.is_valid(locate("c3"))
        True
        >>> knight.is_valid(locate("d2"))
        False
        >>> knight.is_valid(locate("d4"))
        False
        >>> knight.is_valid(locate("a3"))
        True
        """
        row_change = abs(self.position.row - position.row)
        col_change = abs(self.position.col - position.col)
        if not (row_change == 2 and col_change == 1 or\
                row_change == 1 and col_change == 2):
            return False
        target = self.board.get_piece(position)
        if target and target.color == self.color:
            return False
        return True

    def valid_pos(self):
        """
        Returns a list of valid positions for self (knight) to move to.
        >>> board = Board()
        >>> knight = board.get_piece(locate("b1"))
        >>> knight.valid_pos()
        [c3, a3]
        >>> board.move_piece(knight, locate("c3"))
        >>> knight.valid_pos()
        [e4, d5, b5, a4, b1]
        >>> board.move_piece(knight, locate("b5"))
        >>> knight.valid_pos()
        [d6, c7, d4, a7, c3, a3]
        """
        valid_pos = []

        for unit in [(1, 2), (2, 1), (-1, 2), (2, -1),
                (1, -2), (-2, 1), (-1, -2), (-2, -1)]:
            cur = self.position + unit
            if not cur.in_range():
                continue
            piece = self.board.get_piece(cur)
            if piece and piece.color == self.color:
                continue
            valid_pos.append(cur)
        
        return valid_pos

class Rook(Piece):
    name = "rook"
    char = "R"
    def __init__(*args):
        Piece.__init__(*args)

    def is_valid(self, position):
        """Returns True if move to position is valid
        >>> board = Board(empty=True)
        >>> rook = Rook("black")
        >>> board.add_piece(rook, locate("d4"))
        >>> board.add_piece(Pawn("white"), locate("d2"))
        >>> board.add_piece(Pawn("white"), locate("b4"))
        >>> rook.is_valid(locate("d2"))
        True
        >>> rook.is_valid(locate("d1"))
        False
        >>> rook.is_valid(locate("d3"))
        True
        >>> rook.is_valid(locate("d4"))
        False
        >>> rook.is_valid(locate("a4"))
        False
        >>> rook.is_valid(locate("b4"))
        True
        >>> rook.is_valid(locate("b3"))
        False
        """
        if piece_is_blocked_straight(self, position):
            return False
        target = self.board.get_piece(position)
        if target and target.color == self.color:
            return False
        return True
    
    def valid_pos(self):
        """
        Returns the valid moves for rook.
        >>> board = Board()
        >>> board.remove_piece(board.get_piece(locate("a2")))
        >>> rook = board.get_piece(locate("a1"))
        >>> rook.valid_pos()
        [a2, a3, a4, a5, a6, a7]
        >>> board.move_piece(rook, locate("a4"))
        >>> rook.valid_pos()
        [a5, a6, a7, b4, c4, d4, e4, f4, g4, h4, a3, a2, a1]
        >>> board.move_piece(rook, locate("d4"))
        >>> rook.valid_pos()
        [d5, d6, d7, e4, f4, g4, h4, d3, c4, b4, a4]
        """
        valid_pos = []
        for unit in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            cur = self.position
            while True:
                cur = cur + unit
                if not cur.in_range():
                    break
                piece = self.board.get_piece(cur)
                if piece:
                    if piece.color != self.color:
                        valid_pos.append(cur)
                    break
                
                valid_pos.append(cur)
        return valid_pos


class Queen(Piece):
    name = "queen"
    char = "Q"
    def __init__(*args):
        Piece.__init__(*args)
    
    # TODO: Finish doctests
    def is_valid(self, position):
        """
        Returns True if move to position is valid.
        """
        if piece_is_blocked_straight(self,position) and\
                piece_is_blocked_diagonal(self, position):
            return False
        if self.board.get_piece(position) and\
                self.board.get_piece(position).color == self.color:
            return False
        return True

    def valid_pos(self):
        valid_pos = []
        for unit in [(1, 0), (0, 1), (-1, 0), (0, -1),
                (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            cur = self.position
            while True:
                cur = cur + unit
                if not is_in_range(cur):
                    break
                piece = self.board.get_piece(cur)
                if piece:
                    if piece.color != self.color:
                        valid_pos.append(cur)
                    break
                
                valid_pos.append(cur)
        return valid_pos


# TODO: Implement castling
class King(Piece):
    name = "king"
    char = "K"
    def __init__(*args):
        Piece.__init__(*args)
    
    # TODO: Finish doctests
    def is_valid(self,position):
        """
        Returns True if move to position is valid.
        """
        row_change = abs(position.row - self.position.col)
        col_change = abs(position.row - self.position.col)

        if row_change == 0 and col_change == 0:
            return False
        if row_change > 1 or col_change > 1:
            return False
        if self.board.get_piece(position) and\
                self.board.get_piece(position).color == self.color:
            return False
        return True
    
    # TODO: Add doctests
    # TODO: Implement castling
    # TODO: Finish
    def valid_pos(self):
        """
        Returns the valid positions for the king.
        >>> board = Board(empty=True)
        >>> board.add_piece(Rook("white"), locate("a1"))
        >>> board.add_piece(Rook("white"), locate("h1"))
        >>> board.add_piece(King("white"), locate("e1"))
        >>> board.add_piece(Rook("black"), locate("a8"))
        >>> king = board.kings["white"]
        >>> king.valid_pos()

        """
        valid_pos = []
        for unit in [(1, 0), (1, 1), (0, 1), (-1, 1),
                (-1, 0), (-1, -1), (0, -1), (1, -1)]:
            cur = self.position + unit
            target = self.board.get_piece(cur)
            if cur.in_range() and (not target or target.color != self.color):
                valid_pos.append(cur)

        return valid_pos
