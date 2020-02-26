import copy

def win(board, player):
    board = board.board
    solution = []
    
    for x in range(0, 3):
        clue = 0
        empty = 0
        for y in range(0, 3):
            if( board[y][x] == player):
                clue += 1
            elif(board[y][x] == 0):
                if(empty == 0):
                    empty = [y, x]
                    clue += 1
        if(clue == 3):
            ##print('a')
            solution.append(empty)
            break

    for y in range(0, 3):
        clue = 0
        empty = 0
        for x in range(0, 3):
            if( board[y][x] == player):
                clue += 1
            elif(board[y][x] == 0):
                if(empty == 0):
                    empty = [y, x]
                    clue += 1
        if(clue == 3):
            ##print('b')
            solution.append(empty)
            break
        
    clue = 0
    empty = 0
    for x in range(0, 3):
        if( board[x][x] == player):
            clue += 1
        elif(board[x][x] == 0):
            if(empty == 0):
                empty = [x, x]
                clue += 1
    if(clue == 3):
        ##print('c')
        solution.append(empty)
        
    clue = 0
    empty = 0
    for x in range(0, 3):
        if( board[x][2-x] == player):
            clue += 1
        elif(board[x][2-x] == 0):
            if(empty == 0):
                empty = [2-x, x]
                clue += 1
    if(clue == 3):
        ##print('d')
        emp = [empty[1], empty[0]]
        solution.append(emp)

    if(isinstance(solution, list)):
        if(len(solution) == 0):
            x = 0
        else:
            x  = solution[0]

    return [x, solution]

def block(board, player):
    if(player == 1):
        move, s = win(board, 2)
    else:
        move, s = win(board, 1)

    return move

def fork(board, player):
    move = 0
    solution, moves  = [], []
    for i in range(0, 3):
        for j in range(0, 3):
            b = copy.deepcopy(board)
            if(b.board[i][j] == 0):
                b.board[i][j] = player
                m, solution = win(b, player)
                
                if(len(solution) > 1):
                    moves.append([i, j])

    if(len(moves) > 0):
        move = moves[0]

    return [move, moves]


def block_fork(board, player):
    move = 0
    m, forks = fork(board, (player%2)+1)
    if(len(forks) > 1):
        for i in range(len(forks)):
            b  = copy.deepcopy(board)
            b.board[forks[i][0]][forks[i][1]] = player
            if(win(b, player)[0] != 0 and fork(b, (player%2)+1)[0] == 0):
                move = forks[i]
        if(move == 0):
            for i in range(0, 3):
                for j in range(0, 3):
                    if(board.board[i][j] == 0):
                        bd  = copy.deepcopy(board)
                        bd.board[i][j] = player
                        if(bot(bd, (player%2)+1)[1] == 1):
                            move = [i, j]
    return move

def prepare_fork(board, player):
    board = board.board
    move = 0
    if(abs(board[0][0] - board[0][2]) == 1 and board[0][0] != 0 and board[0][2] != 0):
        move = opposite_corner(board, player)
    elif(abs(board[2][2] - board[0][2]) == 1 and board[2][2] != 0 and board[0][2] != 0):
        move = opposite_corner(board, player)
    elif(abs(board[0][0] - board[2][0]) == 1 and board[0][0] != 0 and board[2][0] != 0):
        move = opposite_corner(board, player)
    elif(abs(board[2][2] - board[2][0]) == 1 and board[2][2] != 0 and board[2][0] != 0):
        move = opposite_corner(board, player)

    return move

def center(board, player):
    board = board.board
    move = 0
    if(board[1][1] == 0):
        move = [1, 1]
    return move
   
def opposite_corner(board, player):
    if(type(board) != list):
        board = board.board
    move = 0
    if(board[0][0] == reverse_player(player)):
        if(board[2][2] == 0):
            move = [2, 2]
    elif(board[0][2] == reverse_player(player)):
        if(board[2][0] == 0):
            move = [2, 0]
    elif(board[2][0] == reverse_player(player)):
        if(board[0][2] == 0):
            move = [0, 2]
    elif(board[2][2] == reverse_player(player)):
        if(board[0][0] == 0):
            move = [0, 0]
    return move

def corner(board, player):
    board = board.board
    move = 0
    if(board[0][0] == 0):
       move = [0, 0]
    elif(board[0][2] == 0):
        move = [0, 2]
    elif(board[2][0] == 0):
        move = [2, 0]
    elif(board[2][2] == 0):
        move = [2, 2]
        
    return move

def side(board, player):
    board = board.board
    move = 0
    if(board[0][1] == 0):
       move = [0, 1]
    elif(board[1][0] == 0):
        move = [1, 0]
    elif(board[1][2] == 0):
        move = [1, 2]
    elif(board[2][1] == 0):
        move = [2, 1]
    return move  

def reverse_player(player):
    if(player == 1):
        rev = 2
    else:
        rev = 1
    return rev

strategy = [win, block, fork, block_fork, prepare_fork, center, opposite_corner, corner, side]

def bot(board, player):
    for i in range(0, 9):
        if(i == 0 or i == 2):
            move, s = strategy[i](board, player)
        else:
            move = strategy[i](board, player)
            
        if(move != 0):
            break

    return [move, i]

                

