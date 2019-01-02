import chess.chess
import numpy as np
import numpy.random as random
import itertools as it
import time
import chess.ai

"""
This file is for training the heuristic. First, we describe 
our representation of the board. We want our features to
be the 
"""

# Define the ordering of the pieces.
# We'll go by the unicode numbers.


def convert_board_to_feature(board):
    features = np.zeros(shape=(12, 12, 15, 15))
    pieces = [piece for row in board.board for piece in row if piece is not None]
    for piece1, piece2 in it.product(pieces, repeat=2):
        features[feature_index(piece1, piece2)] += 1
    return features

def feature_index(piece1, piece2):
    piece_index1 = piece1.index + piece1.color * 6
    piece_index2 = piece2.index + piece2.color * 6
    horizontal_dist = piece2.position.row - piece1.position.row
    vertical_dist = piece2.position.col - piece1.position.col
    return piece_index1, piece_index2, horizontal_dist + 7, vertical_dist + 7
    
def construct_training_set(maximum):
    dataset_X = np.zeros(shape=(0, 32400))
    dataset_y = np.zeros(shape=0)

    counter = 0
    for pos1, pos2, pos3, pos4 in it.permutations(range(64), 4):
        for piece1, piece2 in it.permutations(range(10), 2):
            if random.random() > 0.0001:
                continue
            # Construct the board with four pieces, two of which are 
            # kings. 
            board = chess.Board(empty=True)
            board.add_piece(chess.locate_piece(chess.KING, chess.WHITE, 
                chess.Position(pos1 // 8, pos1 % 8)))
            board.add_piece(chess.locate_piece(chess.KING, chess.BLACK, 
                chess.Position(pos2 // 8, pos2 % 8)))
            board.add_piece(chess.locate_piece(piece1 % 5 + 1, piece1 // 5,
                chess.Position(pos3 // 8, pos3 % 8)))
            board.add_piece(chess.locate_piece(piece2 % 5 + 1, piece2 // 5,
                chess.Position(pos4 // 8, pos4 % 8)))

            # Convert to feature.
            feature = convert_board_to_feature(board)
            feature = feature.reshape((1, 32400))

            # Solve board to see if bad or good
            try:
                score, _ = ai.minimax(board, 4, chess.WHITE)
            except:
                print("Failed test case, but will skip!")
                continue
            if score > 0:
                dataset_y = np.append(dataset_y, [1])
            else:
                dataset_y = np.append(dataset_y, [-1])
            dataset_X = np.vstack([dataset_X, feature])

            # Record progress
            counter += 1
            if counter % 100 == 0:
                print("Completed", counter, "cases!")
            if counter > maximum:
                print("Found {0} samples! Will stop now.".format(maximum))
                return dataset_X, dataset_y
    return dataset_X, dataset_y

def main():
    start = time.time()
    X, y = construct_training_set(100000)
    np.savez('chess_data.npz', X=X, y=y)
    end = time.time()
    print("The program executed in {0} seconds!".format(end - start))

if __name__ == "__main__":
    main()
