#list in list because is easy to display

board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

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

def place_piece(selection, board):
    board[selection[0]][selection[1]] = 'X'

# error handling if is not a number & place X to a square
def main():
    while True:
        display_board(board)
        try:
            selection = convert_selection(select_square())
            place_piece(selection, board)
        except ValueError:
            print("It's not a number")

main 
if __name__ == "__main__":
    main()