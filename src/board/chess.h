/*
 * This file defines the Piece class and the Board class. 
 * An important note regarding the board class is that the board has
 * pointers to Piece objects. Since there are only 6 * 64 * 2 possible
 * piece with position, I've decided to store them in the heap, and 
 * deallocate memory afterwards.
 */

#ifndef CHESS_H
#define CHESS_H

#include "utils.h"
#include "board/gamestate.h"

class Piece {
    public:
        Piece(PieceType type, Position pos);
        Position getPosition();
        PieceType getType();
    private:
        Position mPos;
        PieceType mType;
};

class Board /*: GameState*/ {
    public:
        Board(bool empty=false);
        ~Board();
        Piece* getPiece(Position pos);
        void addPiece(Piece* piece, Position pos);
        Piece* movePiece(Piece* piece, Position finalPos, ep=False, castle=False, promote=False);
        void removePiece(Piece* piece);
    private:
        Piece** board;
        Piece* mWhiteKing;
        Piece* mBlackKing;
        Piece* mEnPassant;
        bool mWhiteQueenCastle;
        bool mWhiteKingCastle;
        bool mBlackQueenCastle;
        bool mBlackKingCastle;
}

#endif
