from collections import deque


def print_matrix(mtrx):
    for row in mtrx:
        print("[ ", end="")
        print(*row, sep=", ", end="")
        print(" ]")


def is_valid_row(index):
    if 0 <= index <= 5:
        return True
    return False


def is_valid_col(index):
    if 0 <= index <= 6:
        return True
    return False


rows = 6
cols = 7

# create empty matrix
players = deque([1, 2])
print("Hello! Let's play Connect Four game!")

while True:
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    player_won = False
    moves_counter = 0
    print_matrix(matrix)

    # start the game
    while True:
        player_in_turn = players[0]

        # check if player input is valid, check if it's a number, if it is between 1 and 7 and if it's not a full column
        while True:
            try:
                move = int(input(f"Player {player_in_turn}, please choose a column [1-7]: \n"))
            except ValueError:
                print("Invalid input, not a number.")
            else:
                if 1 <= move <= 7:
                    if matrix[0][move - 1] == 0:
                        break
                    else:
                        print("Column is full!")
                else:
                    print("Invalid number, columns are 1 to 7.")

        selected_col = move - 1

        # put the rock at the bottom of the column and define it's position (row and column)
        for i in range(rows - 1, -1, -1):
            if matrix[i][selected_col] == 0:
                matrix[i][selected_col] = player_in_turn
                p_row = i
                p_col = selected_col
                moves_counter += 1
                break

        print_matrix(matrix)

        # check if there is a winner
        # first check for row win
        for n in range(-3, 1):
            count = 0
            for i in range(n, n + 4):    # (-3, 0)    (-2, 1)   (-1, 2)   (0, 3)
                if is_valid_col(p_col + i) and matrix[p_row][p_col + i] == player_in_turn:
                    count += 1
            if count == 4:
                player_won = True
                break
        else:
            # if no row win, check for col win
            for n in range(-3, 1):
                count = 0
                for i in range(n, n + 4):  # (-3, 0)    (-2, 1)   (-1, 2)   (0, 3)
                    if is_valid_row(p_row + i) and matrix[p_row + i][p_col] == player_in_turn:
                        count += 1
                if count == 4:
                    player_won = True
                    break
            else:
                # if no col win, check for primary diagonal win
                for n in range(-3, 1):
                    count = 0
                    for i in range(n, n + 4):  # (-3, 0)    (-2, 1)   (-1, 2)   (0, 3)
                        if is_valid_row(p_row + i) and is_valid_col(p_col + i) \
                                and matrix[p_row + i][p_col + i] == player_in_turn:
                            count += 1
                    if count == 4:
                        player_won = True
                        break
                else:
                    # lastly, check for secondary diagonal win
                    for n in range(-3, 1):
                        count = 0
                        for i in range(n, n + 4):  # (-3, 0)    (-2, 1)   (-1, 2)   (0, 3)
                            if is_valid_row(p_row + i) and is_valid_col(p_col - i) \
                                    and matrix[p_row + i][p_col - i] == player_in_turn:
                                count += 1
                        if count == 4:
                            player_won = True
                            break

        if player_won:
            print(f"Game complete!\nThe winner is player {player_in_turn}!")
            break

        if moves_counter == rows * cols:
            print("Board full, no one wins.")
            break

        players.rotate()

    play_again = input("Wanna play again? Y or N: ").upper()
    while play_again not in "YN":
        print("Invalid input.")
        play_again = input("Wanna play again? Y or N: ").upper()

    if play_again == "N":
        break

print("Thank you for playing!")
