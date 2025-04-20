import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Rows, columns, diagonals
    lines = board + [list(col) for col in zip(*board)] + [
        [board[i][i] for i in range(3)],
        [board[i][2 - i] for i in range(3)],
    ]

    if ['X'] * 3 in lines:
        return 'X'
    if ['O'] * 3 in lines:
        return 'O'
    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'
    return None

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'X': return -1
    if winner == 'O': return 1
    if winner == 'Draw': return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Game loop
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe: You are X, AI is O")

    while True:
        print_board(board)

        # Player move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Cell occupied.")
            except:
                print("Invalid input.")

        if check_winner(board):
            break

        # AI move
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = 'O'

        winner = check_winner(board)
        if winner:
            break

    print_board(board)
    print("Winner:", check_winner(board))

# Run the game
play_game()
