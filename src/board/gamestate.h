#ifndef GAMESTATE_H
#define GAMESTATE_H

#include <vector>

class Move {
    public:
};

class GameState {
    public:
        virtual vector<Move> get_valid_moves() = 0;
        virtual int get_score() = 0;
};

#endif
