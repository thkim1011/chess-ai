from chess import *

class Game:
    def __init__(self):
        """
        Starts a game instance. Player 0
        refers to white and player 1 refers
        to black.
        """
        self.board = Board()
        self.player = 0
        
        print(" ------------------")
        print("| Welcome to Chess |")
        print(" ------------------")

        while True:
            print(self.board)
            print("Player {0}'s turn".format(self.player))
            move = input("Make your move: ")


Game()
