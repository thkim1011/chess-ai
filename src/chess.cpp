//#include <pybind11/pybind11.h>
#include <chess.h>
#include <iostream>

/*
 * Constructor for the Board class. Constructs a board with pieces in initial
 * position. If empty is true, then board will not have any pieces.
 *
 * There are some instance variables that are of importance. this->board is a
 * two dimensional array that stores each of the pieces in their respective 
 * locations. We store everything about the board in this
 */
Board::Board() {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 8; j++) {
            this->board[i][j] = 1;
        }
    }
    this->board[0][0].piece = Piece::ROOK;
    this->board[0][1].piece = Piece::KNIGHT;
    this->board[0][2].piece = Piece::
}

/*
 * Output stream
 */
std::ostream& operator<<(std::ostream& out, const Board& board) {
    for (int i = 7; i >= 0; i--) {
        out << "--------------------\n";
        for (int j = 0; j < 8; j++) {
            if (board.board[i][j].valid) {
                //out << "|" << board.board[i][j].piece;
            }
            out << "\n";
        }
    }
}

/*
 * Get Box
 */
Box Board::getBox(Position pos) const {
    return this->board[pos.row][pos.col];
}
