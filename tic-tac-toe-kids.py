# Initialize board with position number and empty values 
# as key/value pairs
board = { 1 : ' ', 2 : ' ', 3: ' ',
         4 : ' ', 5 : ' ', 6 : ' ', 
         7 : ' ', 8 : ' ', 9 : ' '}

# Initialize variables
count = 0         # counter to track number of steps
playing = True    # boolean (true or false) to check if the game should continue
tie = False       # boolean (true or false) to check if there is a tie
curr_player = 'X' # variable to store current player identifier


def get_next_player(curr_player):
    if curr_player == 'X':
        return 'O'
    else:
        return 'X'
    
def print_fancy_board():
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[1], board[2], board[3]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[4], board[5], board[6]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(board[7], board[8], board[9]))
    print("\t     |     |")
    print("\n")


def print_rules():
    print("\nOnly numeric input is allowed: digits 1 thru 9")

# winning combinations
def check_winner(marker):
    if board[1] == marker and board[2] == marker and board[3] == marker or \
    board[4] == marker and board[5] == marker and board[6] == marker or \
    board[7] == marker and board[8] == marker and board[9] == marker or \
    board[1] == marker and board[4] == marker and board[7] == marker or \
    board[2] == marker and board[5] == marker and board[8] == marker or \
    board[3] == marker and board[6] == marker and board[9] == marker or \
    board[1] == marker and board[5] == marker and board[9] == marker or \
    board[3] == marker and board[5] == marker and board[7] == marker:

        print_fancy_board()

        print("\nPlayer", marker, "won!\n")
        return True
    else:
        return False


def insert_input(spot_num, marker):
    while board[spot_num] != ' ':
        print("spot taken, pick another number")
        spot_num = int(input())
    board[spot_num] = marker

    
# Main program
print_rules()

while playing:

    print_fancy_board()

    curr_player = get_next_player(curr_player)
    print("Player '" + curr_player + "' pick a number: ")
    spotNumberAsStr = input()
    print("You picked", spotNumberAsStr)

    spotNumber = int(spotNumberAsStr)

    #Inserting 'X' or 'O' in desired spot
    insert_input(spotNumber, curr_player)
    count += 1
    
    # Check if anybody won
    somebody_won = check_winner(curr_player)

    # Check if tie
    if count == 9 and somebody_won == False:
        print("Nobody won.")
        tie = True
        print_fancy_board()

    # Check if done
    if somebody_won or tie:
        playing = False
