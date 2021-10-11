BOARD_SIZE = 3
MAX_VALUE = 11

board = [[' ' for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
turn_count = 0

def print_board(board):
    print("-" * (BOARD_SIZE * 2 + 1))
    for row in board:
        print("|" + "|".join(row) + "|")
        print("-" * (BOARD_SIZE * 2 + 1))

def get_terminal(board, turn_count):
    for row in board:
        if len(set(row)) == 1 and ' ' not in row:
            return 10 if row[0] == 'O' else -10
    for i in range(BOARD_SIZE):
        column = [board[j][i] for j in range(BOARD_SIZE)]
        if len(set(column)) == 1 and ' ' not in column:
            return 10 if column[0] == 'O' else -10
    diagonal = [board[i][i] for i in range(BOARD_SIZE)]
    if len(set(diagonal)) == 1 and ' ' not in diagonal:
        return 10 if diagonal[0] == 'O' else -10
    diagonal = [board[BOARD_SIZE - i - 1][i] for i in range(BOARD_SIZE)]
    if len(set(diagonal)) == 1 and ' ' not in diagonal:
        return 10 if diagonal[0] == 'O' else -10
    if turn_count == BOARD_SIZE ** 2:
        return 0
    return 1

def minimax(board, depth, isMaximized, alpha, beta):
    current_state = get_terminal(board, depth)
    if current_state != 1:
        return current_state, -1, -1
    value = -MAX_VALUE if isMaximized else MAX_VALUE
    x, y = None, None
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == " ":
                copy = []
                for row in board:
                    line = list(row)
                    copy.append(line)
                copy[i][j] = "O" if isMaximized else "X"
                result, _, _ = minimax(copy, depth + 1, not isMaximized, alpha, beta)
                if isMaximized:
                    if result > value:
                        x, y = i, j
                        value = result
                    alpha = max(value, alpha)
                else:
                    if result < value:
                        x, y = i, j
                        value = result
                    beta = min(value, beta)
            if beta <= alpha:
                break
    return value, x, y

def get_next_move(board):
    global turn_count
    return minimax(board, turn_count, True, -MAX_VALUE, MAX_VALUE)

while turn_count < BOARD_SIZE ** 2:
    print_board(board)
    print("X turn. Input coordinate (0 0 for top right corner cell): ", end="")
    i, j = list(map(int, input().split()))
    board[i][j] = 'X'
    turn_count += 1
    current_state = get_terminal(board, turn_count)
    if current_state == 1:
        _, i, j = get_next_move(board)
        board[i][j] = 'O'
        turn_count += 1
        if get_terminal(board, turn_count) == 10:
            print("O XON")
            break
    else:
        if current_state == -10:
            print("X WON.")
        elif current_state == 0:
            print("TIE")
        break
print_board(board)
    