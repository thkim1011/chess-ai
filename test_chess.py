import chess
import unittest


class TestBoard(unittest.TestCase):
    def test_get_piece(self):
        # Basic Tests
        board = chess.Board()
        rook1 = board.get_piece(chess.locate("a1"))
        self.assertEqual(rook1.name, "rook")
        rook2 = board.get_piece(chess.locate("a8"))
        self.assertEqual(rook2.name, "rook")
        pawn1 = board.get_piece(chess.locate("a2"))
        self.assertEqual(pawn1.name, "pawn")
        pawn2 = board.get_piece(chess.locate("c2"))
        self.assertEqual(pawn2.name, "pawn")
        pawn3 = board.get_piece(chess.locate("e2"))
        self.assertEqual(pawn3.name, "pawn")
        pawn4 = board.get_piece(chess.locate("e7"))
        self.assertEqual(pawn4.name, "pawn")

        # Assuming move_piece works
        board.move_piece(pawn3, chess.locate("e4"))
        empty = board.get_piece(chess.locate("e2"))
        self.assertEqual(empty, None)
        pawn5 = board.get_piece(chess.locate("e4"))
        self.assertEqual(pawn5.name, "pawn")

    def test_move_piece(self):
        # General piece movement
        board = chess.Board()

    def test_get_moves(self):
        board = chess.Board()
        print(board)
        for b in board.get_moves():
            print(b)

    def test_copy(self):
        board = chess.Board()
        board.move_piece(board.get_piece(chess.locate("b1")), chess.locate("c3"))
        print(board)

    def test_en_passant(self):
        board = chess.Board()

        white_pawn = board.get_piece(chess.locate("e2"))
        black_pawn = board.get_piece(chess.locate("d7"))

        board.move_piece(white_pawn, chess.locate("e5"))
        board.move_piece(black_pawn, chess.locate("d5"))
        
        self.assertTrue(board.en_passant == black_pawn)
        self.assertTrue(white_pawn.is_valid(chess.locate("d6"), board))
        self.assertTrue(chess.locate("d6") in white_pawn.valid_pos(board))

if __name__ == "__main__":
    unittest.main()
