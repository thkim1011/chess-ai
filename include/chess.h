#ifndef CHESS_H
#define CHESS_H

#include <iostream>

enum class Piece: unsigned char {
    KING, QUEEN, ROOK, BISHOP, KNIGHT, PAWN
};

/*
 * Abstraction of a position on a chess board. We specifically create a struct
 * for this to save space, and to use it as a type from the python bindings.
 */
struct Position {
    unsigned char row: 3;
    unsigned char col: 3;
};

/*
 * Abstraction of one box of a chess board. A box either contains a piece, in
 * which we mark the VALID bit to be true, and each of the members of struct
 * Box are valid, or it is empty, in which we mark the VALID bit to be false.
 * For a valid box, we have the members, PIECE (which is one of Piece::KING,
 * Piece::QUEEN, etc.), COLOR (which is 1 for black and 0 for white), RECENT
 * (which is 1 if the piece was most recently moved and 0 otherwise), DIRTY
 * (which is 1 if the box has changed state since the board was initialized and
 * 0 otherwise). There is 1 unused bit which creates a total of 1 byte
 * representing this structure.
 */
struct Box {
    Piece piece: 3;
    bool color: 1;
    bool recent: 1;
    bool diry: 1;
    bool valid: 1;
};

/*
 * The Board class. This class is a representation of a single state of the
 * chess board. It consists of an 8 by 8 array of boxes. This is enough to
 * encapsulate the complete state of the board and to verify special moves such
 * as castling and en passant.
 */
class Board {
    public:
        // Constructor
        Board(bool empty=false);
        Box getBox(Position pos) const;
        friend std::ostream& operator<<(std::ostream& out, const Board& board);
    private:
        Box board[8][8];
};

// Output stream
std::ostream& operator<<(std::ostream&, const Board&);

#endif
