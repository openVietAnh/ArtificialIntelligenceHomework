board = [[' ' for i in range(3)] for j in range(3)]
turn_count = 0

def print_board(board):
    print("-" * 7)
    for row in board:
        print("|" + "|".join(row) + "|")
        print("-" * 7)

def get_terminal(board):
    global turn_count
    if turn_count == 9:
        return 0
    else:
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
                return -10 if board[i][0] == "X" else 10
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
                return -10 if board[0][i] == "X" else 10
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
            return -10 if board[0][0] == "X" else 10
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
            return -10 if board[0][2] == "X" else 10
        return 1

def minimax(board, depth, isMaximized):
    if depth == 9:
        return get_terminal(board), -1, -1
    value = -11 if isMaximized else 11
    x, y = None, None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                copy = []
                for row in board:
                    line = list(row)
                    copy.append(line)
                copy[i][j] = "O" if isMaximized else "X"
                result, _, _ = minimax(copy, depth + 1, not isMaximized)
                if isMaximized:
                    if result > value:
                        x, y = i, j
                        value = result
                else:
                    if result < value:
                        x, y = i, j
                        value = result
    return value, x, y

def get_next_move(board):
    global turn_count
    return minimax(board, turn_count, True)

while turn_count < 9:
    print_board(board)
    print("X turn. Input coordinate (e.g: 1 1 for center cell): ", end="")
    i, j = list(map(int, input().split()))
    board[i][j] = 'X'
    turn_count += 1
    current_state = get_terminal(board)
    print(current_state)
    if current_state == 1:
        _, i, j = get_next_move(board)
        board[i][j] = 'O'
        turn_count += 1
        if get_terminal(board) == 10:
            print("O XON")
            break
    else:
        if current_state == -10:
            print("X WON.")
        elif current_state == 0:
            print("TIE")
        break
print_board(board)
    