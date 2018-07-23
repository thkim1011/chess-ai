#include "utils.h"

Position::Position(char row, char col) : mRow(row), mCol(col) {}

char getRow() {
    return mRow;
}

char getCol() {
    return mCol;
}
