# Chess AI

Provides a very basic chess game and AI.

# Very Quick Tutorial

To construct a new chess board, use the Board class.

    >>> board = Board();

To show the board, print board.

    >>> print(board)

To locate a position, use locate().

    >>> locate("a3")
    a3

To get a piece, call the get_piece method.

    >>> board.get_piece(locate("a1"))
    Rook("white") at a1
    
