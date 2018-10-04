import unittest
import chess
from chess import Board, locate, locate_piece, BLACK, WHITE

import ai

KING = 0
QUEEN = 1
ROOK = 2
KNIGHT = 3
BISHOP = 4
PAWN = 5


class TestAI(unittest.TestCase):
    def test_minimax(self):
        # Own Test
        board1 = chess.Board()
        pawn = board1.get_piece(chess.locate("e2"))
        knight = board1.get_piece(chess.locate("g8"))
        board1.move_piece(pawn, chess.locate("e4"))
        board1.move_piece(knight, chess.locate("f6"))
        _, move = ai.minimax(board1, 3, 1)
        self.assertEqual(move, chess.Move(board1.get_piece(chess.locate("f6")), chess.locate("e4")))
        _, move = ai.minimax_with_pruning(board1, 3, -1000, 1000, 1)
        self.assertEqual(move, chess.Move(board1.get_piece(chess.locate("f6")), chess.locate("e4")))
        _, move = ai.minimax(board1, 3, 0)
        _, move = ai.minimax_with_pruning(board1, 3, -1000, 1000, 0)
        board1.move_piece(board1.get_piece(chess.locate("f1")), chess.locate("a6"))
        _, move = ai.minimax(board1, 3, 1)
        self.assertEqual(move, chess.Move(board1.get_piece(chess.locate("b8")), chess.locate("a6")))
        board1.move_piece(board1.get_piece(chess.locate("b8")), chess.locate("a6"))
        print(board1.compute_score(1))
        print(move)

        # Puzzle 68960 from lichess.org
        board3 = Board(empty=True)
        board3.add_piece(locate_piece(ROOK, WHITE, locate("d1")))
        board3.add_piece(locate_piece(ROOK, WHITE, locate("f1")))
        board3.add_piece(locate_piece(KING, WHITE, locate("g1")))
        board3.add_piece(locate_piece(PAWN, WHITE, locate("b2")))
        board3.add_piece(locate_piece(PAWN, WHITE, locate("c2")))
        board3.add_piece(locate_piece(PAWN, WHITE, locate("a3")))
        board3.add_piece(locate_piece(KNIGHT, BLACK, locate("e3")))
        board3.add_piece(locate_piece(PAWN, WHITE, locate("h3")))
        board3.add_piece(locate_piece(PAWN, BLACK, locate("c4")))
        board3.add_piece(locate_piece(PAWN, WHITE, locate("g4")))
        board3.add_piece(locate_piece(PAWN, BLACK, locate("b5")))
        board3.add_piece(locate_piece(PAWN, WHITE, locate("e5")))
        board3.add_piece(locate_piece(PAWN, WHITE, locate("f5")))
        board3.add_piece(locate_piece(BISHOP, BLACK, locate("a6")))
        board3.add_piece(locate_piece(PAWN, BLACK, locate("b6")))
        board3.add_piece(locate_piece(KNIGHT, WHITE, locate("d6")))
        board3.add_piece(locate_piece(KNIGHT, WHITE, locate("e7")))
        board3.add_piece(locate_piece(PAWN, BLACK, locate("f7")))
        board3.add_piece(locate_piece(PAWN, BLACK, locate("g7")))
        board3.add_piece(locate_piece(PAWN, BLACK, locate("h7")))
        board3.add_piece(locate_piece(ROOK, BLACK, locate("a8")))
        board3.add_piece(locate_piece(KNIGHT, BLACK, locate("b8")))
        board3.add_piece(locate_piece(ROOK, BLACK, locate("f8")))
        board3.add_piece(locate_piece(KING, BLACK, locate("h8")))
        print(board3)
        ai.minimax(board3, 4, WHITE)

        # Puzzle 68960 from lichess.org
        board3 = Board(empty=True)
        board3.add_piece(locate_piece(ROOK, WHITE, locate("d1")))
        board3.add_piece(locate_piece(ROOK, WHITE, locate("f1")))
        board3.add_piece(locate_piece(KING, WHITE, locate("g1")))
        board3.add_piece(locate_piece(PAWN, WHITE, locate("b2")))
        board3.add_piece(locate_piece(PAWN, WHITE, locate("c2")))
        board3.add_piece(locate_piece(PAWN, WHITE, locate("a3")))
        board3.add_piece(locate_piece(KNIGHT, BLACK, locate("e3")))
        board3.add_piece(locate_piece(PAWN, WHITE, locate("h3")))
        board3.add_piece(locate_piece(PAWN, BLACK, locate("c4")))
        board3.add_piece(locate_piece(PAWN, WHITE, locate("g4")))
        board3.add_piece(locate_piece(PAWN, BLACK, locate("b5")))
        board3.add_piece(locate_piece(PAWN, WHITE, locate("e5")))
        board3.add_piece(locate_piece(PAWN, WHITE, locate("f5")))
        board3.add_piece(locate_piece(BISHOP, BLACK, locate("a6")))
        board3.add_piece(locate_piece(PAWN, BLACK, locate("b6")))
        board3.add_piece(locate_piece(KNIGHT, WHITE, locate("d6")))
        board3.add_piece(locate_piece(KNIGHT, WHITE, locate("e7")))
        board3.add_piece(locate_piece(PAWN, BLACK, locate("f7")))
        board3.add_piece(locate_piece(PAWN, BLACK, locate("g7")))
        board3.add_piece(locate_piece(PAWN, BLACK, locate("h7")))
        board3.add_piece(locate_piece(ROOK, BLACK, locate("a8")))
        board3.add_piece(locate_piece(KNIGHT, BLACK, locate("b8")))
        board3.add_piece(locate_piece(ROOK, BLACK, locate("f8")))
        board3.add_piece(locate_piece(KING, BLACK, locate("h8")))
        print(board3)

        board3.move_piece(locate_piece(ROOK, WHITE, locate("d1")), locate("d2"))
        print(board3)
        for move, board in board3.get_moves(BLACK):
            print(move)

        print(ai.minimax(board3, 3, BLACK))
        print(BLACK)

    def test(self):
        board2 = chess.Board()
        print(board2)
        # Lets play a game with itself!
        depth = 3
        turn = 0
        for i in range(10):
            _, move = ai.minimax_with_pruning(board2, depth, -1000, 1000, turn)
            board2.move_piece(move.piece, move.position)
            print(board2)
            turn = 1 - turn


if __name__ == "__main__":
    unittest.main()