# Chess Board and Pieces

# Board class
class Board:
    def __init__(self):
        """ Constructs a board with pieces in initial position.
        >>> board = Board()
        >>> board.board[0][0].name
        "rook"
        >>> board.board[0][0].color
        "white"
        """
        self.board = []
        
        for _ in range(8):
            self.board.append([None] * 8)
        # Populate board
        self.board[0][0] = Rook("white", (0, 0))
        self.board[0][1] = Knight("white", (0, 1))
        self.board[0][2] = Bishop("white", (0, 2))
        self.board[0][3] = Queen("white", (0, 3))
        self.board[0][4] = King("white", (0, 4))
        self.board[0][5] = Bishop("white", (0, 5))
        self.board[0][6] = Knight("white", (0, 6))
        self.board[0][7] = Rook("white", (0, 7))

        self.board[7][0] = Rook("black", (7, 0))
        self.board[7][1] = Knight("black", (7, 1))
        self.board[7][2] = Bishop("black", (7, 2))
        self.board[7][3] = Queen("black", (7, 3))
        self.board[7][4] = King("black", (7, 4))
        self.board[7][5] = Bishop("black", (7, 5))
        self.board[7][6] = Knight("black", (7, 6))
        self.board[7][7] = Rook("black", (7, 7))
        
        for i in range(8):
            self.board[1][i] = Pawn("white", (1, i))
            self.board[6][i] = Pawn("black", (6, i))

    def __str__(self):
        border = " ---" * 8 + "\n"
        board = border
        for i in self.board:
            line = "| "
            for j in i:
                if j is None:
                    line += "  | "
                else:
                    line += j.char + " | "
            board += line + "\n"
            board += border
        return board

    def get_piece(self, position):
        return self.board[position[0]][position[1]]

    def set_piece(self, position, piece):
        self.board[position[0]][position[1]] = piece

    def has_piece(self, position):
        return get_piece(position) != None

    def is_blocked(self, piece, position):
        # Check forward/backward
        if 
        
        


"""
    def make_move(self, move):
        try:

            """

   
        
        
# Move class
class Move:
    def __init__(self, piece, position):
        self.piece = piece
        self.position = position
    





# Pieces
class Piece:
    def __init__(self, color, position, board):
        assert color == "black" or color == "white"
        assert 0 <= position[0] and position[0] < 8
        assert 0 <= position[1] and position[1] < 8
        self.color = color
        self.position = position
        self.board = board


class Pawn(Piece):
    name = "pawn"
    char = "P"

    def __init__(*args):
        """ Constructs a pawn.
        >>> pawn = Pawn("black", (0, 1))
        >>> pawn.name
        'pawn'
        >>> pawn.color
        'black'
        >>> pawn.position
        (0, 1)
        """
        Piece.__init__(*args) 

    def validate(self, move):
        assert isinstance(move, Move)
        if self.color == "white":
            # Forward 1
            if move.position[0] == self.position[0] + 1\
                    and !self.board.has_piece(move.position):
                return True
            # Forward 2
            elif move.position[0] == self.position[0] + 2\
                    and !self.board.has_piece(move.position)\
                    and !self.board.has_piece(move.position - (0, 1)) 

            # Forward 2
        if self.position[1] == 1 and self.color == "white": 
            
            if move[0] == move + 1

           
            



class Bishop(Piece):
    name = "bishop"
    char = "B"
    def __init__(self, color, position):
        Piece.__init__(self, color, position)

class Knight(Piece): 
    def __init__(self, color, position):
        Piece.__init__(self, color, position)
        self.name = "knight"
        self.char = "N"

class Rook(Piece):
    def __init__(self, color, position):
        Piece.__init__(self, color, position)
        self.name = "rook"
        self.char = "R"

class Queen(Piece):
    def __init__(self, color, position):
        Piece.__init__(self, color, position)
        self.name = "queen"
        self.char = "Q"

class King(Piece):
    def __init__(self, color, position):
        Piece.__init__(self, color, position)
        self.name = "king"
        self.char = "K"


