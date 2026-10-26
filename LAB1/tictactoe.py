board = [" "] * 9


def display():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def bot_move():

    # Case 1: Bot can win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            if check_winner("O"):
                return

            board[i] = " "

    # Case 2: Block opponent
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"

            if check_winner("X"):
                board[i] = "O"
                return

            board[i] = " "

    # Case 3: Center
    if board[4] == " ":
        board[4] = "O"
        return

    # Case 4: Corner
    for i in [0, 2, 6, 8]:
        if board[i] == " ":
            board[i] = "O"
            return

    # Case 5: Any empty position
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return


def play(bot):
    global board

    board = [" "] * 9

    while True:

        # Player/System 1
        display()

        pos = int(input("Player 1 (X), enter position: ")) - 1

        if board[pos] != " ":
            print("Position already occupied!")
            continue

        board[pos] = "X"

        if check_winner("X"):
            display()
            print("Player 1 wins!")
            break

        if " " not in board:
            display()
            print("Draw!")
            break

        # Player/System 2 or Bot
        if bot:
            bot_move()
            print("Bot played")
        else:
            display()

            pos = int(input("Player 2 (O), enter position: ")) - 1

            if board[pos] != " ":
                print("Position already occupied!")
                continue

            board[pos] = "O"

        if check_winner("O"):
            display()
            print("Player 2/Bot wins!")
            break

        if " " not in board:
            display()
            print("Draw!")
            break


print("TIC TAC TOE")
print("1. System vs System")
print("2. System vs Bot")

choice = int(input("Enter choice: "))

if choice == 1:
    play(False)

elif choice == 2:
    play(True)

else:
    print("Invalid choice")
