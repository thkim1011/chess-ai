#ifndef UTILS_H
#define UTILS_H

class Position {
    public:
        Position(char row, char col);
        char getRow();
        char getCol();
    private:
        char mRow;
        char mCol;
}

enum class PieceType { King, Queen, Rook, Bishop, Knight, Pawn };

extern Position positions[8][8]
#endif
