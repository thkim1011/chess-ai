from chess import *
import ai
import importlib

# construct a better test case
board = Board(empty=True)
board.add_piece(locate_piece(KING, WHITE, locate("e1")))
board.add_piece(locate_piece(KING, BLACK, locate("e8")))
board.add_piece(locate_piece(ROOK, WHITE, locate("a1")))
board.add_piece(locate_piece(ROOK, WHITE, locate("h1")))

board.move_piece(locate_piece(ROOK, WHITE, locate("a1")), locate("a8"))
print(board)

print("Board is in check:", board.in_check(WHITE))
for move, b in board.get_moves(1):
    print(b)
    print(move, b.in_check(BLACK))
