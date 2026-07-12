#TIC TAC TOE GAME
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

win = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)

played = set()

def print_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def check_winner(board, player):
    for i in win:
        if board[i[0]] == player and board[i[1]] == player and board[i[2]] == player:
            return True
    return False

def check_draw(board):
    for i in board:
        if i == " ":
            return False
    return True

def switch_player(player):
    if player == "X":
        return "O"
    else:
        return "X"

player = "X"

for i in range(9):
    print_board(board)
    pos = int(input("Player " + player + " Enter position (1-9): ")) - 1

    if pos >= 0 and pos <= 8:
        if board[pos] == " ":
            board[pos] = player
            played.add(pos + 1)

            if check_winner(board, player):
                print_board(board)
                print("Player", player, "wins!")
                break

            if check_draw(board):
                print_board(board)
                print("Match Draw!")
                break

            player = switch_player(player)
        else:
            print("Position already taken.")
    else:
        print("Invalid position.")

print("Played Positions:", played)