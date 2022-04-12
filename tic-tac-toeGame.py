#list in list because is easy to display

board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

game_over = False 

def display_board(board):
    for row in board:
        print(row)

# input value from user with validation range

def select_square():
    userInput = int(input("Selected square: "))
    if(userInput <1 or userInput > 9 ):
        print("Invalid value, range option is between 1 to 9")
    else:
        return userInput

# convert user value to a tuple to access position(floor division and modulo)
def convert_selection(selection):
    selection -= 1
    return (selection // 3, selection % 3)

# verify if is not ocupied and place x or 0
def place_piece(selection,is_x, board):
        if board[selection[0]][selection[1]] == '_':
            print("O trun") if is_x else print("X turn") 
            board[selection[0]][selection[1]] = "X" if is_x else "O"
        else:
            raise ValueError

# error handling if is not a number & place piece to a square
def main():
    is_x = True
    game_over = False
    print("X trun") 
    while not game_over:
        display_board(board)
        try:
            selection = convert_selection(select_square())
            place_piece(selection, is_x, board)
        except ValueError:
            print("It's not a number or is ocupied")
            continue
        game_over = is_win(board) or is_draw(board)
        is_x = not is_x

# the board is full
def is_draw(board):
    for row in board:
        for val in row:
            if val == "_":
                return False
    display_board(board)
    print("Draw!")
    return True

# winer 8 posib
def is_win(board):
    winner = None
    for i in range(3):
        # horizontal
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
            winner = board[i][0]
            break
        # vertical
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":
            winner = board[0][i]
            break
    # diagonal
    if board[1][1] != "_":
        if (board[0][0] == board[1][1] == board[2][2]
            or board[0][2] == board[1][1] == board[2][0]):
            winner = board[1][1]
    if winner is not None:
        display_board(board)
        print(f"{winner} is the winner!")
        return True
    return False

# main
if __name__ == "__main__":
    main()
