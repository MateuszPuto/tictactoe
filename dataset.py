import game
import ttt_ai as ttt
import random
import copy

def generate_random_game():
    board = game.board([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    numOfPieces = random.randint(0, 9)
    lst = [x for x in range(0,9)]
    sample = random.sample(lst, numOfPieces)
    turn = 0
    for i in range(len(sample)):
        x = sample[i] % 3
        y = sample[i] // 3
        turn = (turn % 2) + 1
        board.place(x, y, turn)

    return board

def generate_dataset(size):
    dataset = []
    for i in range(0, size):
        pos = generate_random_game()
        dataset.append([pos, play_perfect_game(copy.deepcopy(pos))[1]])

    return dataset

def play_perfect_game(board):
    while(not board.is_terminal() and not board.check_full_board()):
        move, i = ttt.bot(board, board.turn)
        board = board.place(move[0], move[1], board.turn)
##        board.print_board()

    if(board.is_terminal()):
        result = (board.turn % 2)
    else:
        result = 0.5

    return [board, result]

##result = 0
##board = game.board([[1, 2, 0], [0, 0, 0], [0, 0, 0]])
##board.print_board()
##board, result = play_perfect_game(board)
##print(result)
##board.print_board()


