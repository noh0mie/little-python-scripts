def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def main():
    board = initialize_board()
    player = "X"

    while True:
        print_board(board)
        row = int(input("Player {}, enter row (1-3): ".format(player)))
        col = int(input("Player {}, enter column (1-3): ".format(player)))
        
        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Invalid input. Please enter a row and column between 1 and 3.")
            continue

        # Adjust the user input to 0-based indexing
        row -= 1
        col -= 1

        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("That spot is already taken. Try again.")
            continue

        if check_winner(board, player):
            print_board(board)
            print("Player {} wins!".format(player))
            break

        if all(all(cell != " " for cell in row) for row in board):
            print_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    main()
