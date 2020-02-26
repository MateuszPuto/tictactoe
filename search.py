import game
import dataset
import torch
import numpy as np
import copy
import random

model = torch.load('net02')
model.eval()

class search_tree:
    def __init__(self, startPosition):
        self.root = startPosition

    def search_one_deep(self, piece, breaking=0):
        moves = []
        quality = []
        for x in range(0, 3):
            for y in range(0, 3):
                if(self.root.check_move_legality(x, y, piece)):
                    moves.append([x, y])

        for move in moves:
            new = copy.deepcopy(self.root)
            lst = new.place(move[0], move[1], piece)
            lst = lst.board_plus_turn()
            if(piece == game.piece().os):
                quality.append(float(model(torch.tensor(lst).float())))
                ##quality.append(float(dataset.play_perfect_game(copy.deepcopy(lst))[1]))
            else:
                quality.append(1.0 - float(model(torch.tensor(lst).float())))
                ##quality.append(1.0 - float(dataset.play_perfect_game(copy.deepcopy(lst))[1]))                            
        topMoves = []
        yx = sorted(zip(quality, moves), reverse=True)
        print(yx)

        return yx[0]


board = game.board([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
piece = 1

while(not board.is_terminal() and not board.check_full_board()):
    search = search_tree(copy.deepcopy(board))
    move = search.search_one_deep(piece)
    board = board.place(move[1][0], move[1][1], piece)
    board.print_board()
    piece = (piece % 2) + 1

