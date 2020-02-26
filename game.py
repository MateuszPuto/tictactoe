import math

class piece():
    def __init__(self):
        self.xes = 1
        self.os = 2

class board():
    def __init__(self, board=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
        self.board = board
        xes, os = 0, 0
        for i in range(0, 3):
            for j in range(0, 3):
                if(board[i][j] == piece().xes):
                    xes += 1
                elif(board[i][j] == piece().os):
                    os += 1
        if(xes <= os):
            self.turn = 1
        else:
            self.turn = 2

    def place(self, x, y, piece):
        self.board[x][y] = piece
        self.turn = (self.turn % 2) + 1

        return self

    def board_into_list(self):
        x = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if(self.board[i][j] == 1):
                    x.append(1)
                    x.append(0)
                elif(self.board[i][j] == 2):
                    x.append(0)
                    x.append(1)
                else:
                    x.append(0)
                    x.append(0)

        return x

    def board_plus_turn(self):
        x = self.board_into_list()
        x.append(self.turn)

        return x

    def check_full_board(self):
        full = True
        for x in range(0, 3):
            for y in range(0, 3):
                if(self.board[y][x] == 0):
                    full = False

        return full

    def check_move_legality(self, x, y, piece):
        legal = False
        if(self.board[x][y] == 0 and piece == self.turn):
            legal = True

        return legal

    def print_board(self):
        print('  -   -   -')
        for y in range(len(self.board)):
            word = '|'
            for x in range(len(self.board[y])):
                if(self.board[y][x] == 1):
                    word += ' x '
                elif(self.board[y][x] == 2):
                    word += ' o '
                else:
                    word += '   '
                word += '|'
            print(word)
            print('  -   -   -')


    def is_terminal(self):
        win = False

        for piece in range(1, 3):
            for x in range(0, 3):
                for y in range(0, 3):
                    
                    threeInRow = 1
                    for n in range(0, 3):
                        if(self.board[n][x] != piece):
                            threeInRow = 0
                    if(threeInRow == 1):
                        win = True

                    threeInRow = 1     
                    for n in range(0, 3):
                        if(self.board[y][n] != piece):
                            threeInRow = 0
                    if(threeInRow == 1):
                        win = True

                    if(x == y):
                        threeInRow = 1     
                        for n in range(0, 3):
                            if(self.board[n][n] != piece):
                                threeInRow = 0
                        if(threeInRow == 1):
                            win = True
                        
                    if((x+y) == 2):
                        threeInRow = 1     
                        for n in range(0, 3):
                            if(self.board[n][2-n] != piece):
                                threeInRow = 0
                        if(threeInRow == 1):
                            win = True

        return win


