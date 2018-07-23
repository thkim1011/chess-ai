#include "board/chess.h"
#include "board/gamestate.h"
#include <vector>

// Piece Constructor
Piece::Piece(PieceType type, Position pos) : m_pos(pos), m_type(type) {

}

// Get Position
Position Piece::getPosition() {
    return mPos;
}

// Get PieceType
Position Piece::getType() {
    return mType;
}

// Board Constructor
Board::Board(bool empty) {
    board = new Piece*[64];
}

// Board Destructor
Board::~Board() {
    delete board;
}

// Get Piece
Piece* Board::getPiece(Position pos) {
    return nullptr;
}

// Add Piece
void Board::addPiece(Piece* piece) {
    
}

// Move Piece
Piece* Board::movePiece(Piece* piece, Position finalPos, ep=False, castle=False, promote=False) {
    return nullptr;
}

// Remove Piece
void Board::removePiece(Piece* piece) {
}
