# Chess Board and Pieces

# Import


# Board class
class Board:
    def __init__(self, empty=False):
        """ Constructs a board with pieces in initial position.
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
        Moves piece from initial to final position.
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
        """
        piece = self.get_piece(initial)
        self.board[final[0]][final[1]] = piece
        self.board[initial[0]][initial[1]]
        piece.position = final
        
    def remove_piece(self, position):
        """
        Removes piece from position
        and returns a pointer to it.
        >>> board = Board()
        """

    
    def piece_is_blocked_straight(self, piece, position):
        """
        Checks that there is no piece blocking 
        the path to the given position. If 
        path is not straight raise an exception.
        The ends are checked in a different method.
        >>> board = Board()
        >>> pawn1 = board.get_piece((1, 0))
        >>> board.piece_is_blocked_straight(pawn1, (3, 0))
        False
        >>> board.piece_is_blocked_straight(pawn1, (1, 1))
        False
        >>> board.piece_is_blocked_straight(pawn1, (6, 0))
        False
        >>> board.piece_is_blocked_straight(pawn1, (7, 0))
        True
        >>> board.piece_is_blocked_straight(pawn1, (7, 7))
        Traceback (most recent call last):
        ...
        ValueError: position is invalid
        >>> board.piece_is_blocked_straight(pawn1, (1, 0))
        Traceback (most recent call last):
        ...
        ValueError: position must differ from piece's
        """

        if piece.position == position:
            raise ValueError("position must differ from piece's")

        # Check forward/backward
        elif piece.position[0] == position[0]:
            if piece.position[1] < position[1]:
                ran = range(piece.position[1] + 1, position[1])
            elif piece.position[1] > position[1]:
                ran = range(position[1] + 1, piece.position[1])
            for i in ran:
                if self.has_piece((position[0], i)):
                    return True
            return False

        # Check left/right
        elif piece.position[1] == position[1]:
            if piece.position[0] < position[0]:
                ran = range(piece.position[0] + 1, position[0])
            elif piece.position[0] > position[0]:
                ran = range(position[0] + 1, piece.position[0])
            for i in ran:
                if self.has_piece((i, position[1])):
                    return True
            return False

        raise ValueError("position is invalid")
            
    def make_move(self, move):
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

        """
        

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
