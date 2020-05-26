import string

# All possible winner positions
WINNER_POSITIONS = ({0, 1, 2}, {3, 4, 5}, {6, 7, 8},
                    {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
                    {0, 4, 8}, {2, 4, 6})

CHAR_X = "X"
CHAR_O = "O"


def convert_coordinates(coord_x, coord_y):
    """Converts coordinate from user input to position in the field list"""

    return (coord_x - 1) + (3 * (3 - coord_y))


def cell_occupied(coord_x, coord_y):
    """Checks that a cell with the entered coordinates is occupied"""

    return not field[convert_coordinates(coord_x, coord_y)] == " "


def user_input_correct():
    input_to_check = user_input.split()
    if len(input_to_check) != 2 \
            or string.digits.find(input_to_check[0]) == -1 \
            or string.digits.find(input_to_check[1]) == -1:
        print("You should enter numbers!")
        return False
    elif int(input_to_check[0]) > 3 or int(input_to_check[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        return False
    elif cell_occupied(int(input_to_check[0]), int(input_to_check[1])):
        print("This cell is occupied! Choose another one!")
        return False

    return True


def is_winner(char):
    # Create a set with the current position for the char
    current_pos = {i for i in range(len(field)) if field[i] == char}

    # Check that the current position includes a winner position
    for winner_pos in WINNER_POSITIONS:
        if current_pos.issuperset(winner_pos):
            return True

    # No winner position
    return False


def check_winner():

    global winner
    if is_winner(CHAR_X):
        winner = CHAR_X
    elif is_winner(CHAR_O):
        winner = CHAR_O


def no_more_turns():
    return field.count(" ") == 0


def game_finished():
    return no_more_turns() or winner is not None


def check_state():
    if winner is not None:
        print(f"{winner} wins")
    elif no_more_turns():
        print("Draw")


def update_field(coord_x, coord_y, char):
    field[convert_coordinates(coord_x, coord_y)] = char


def print_field():
    """Draw the game field in console"""

    print(9 * "-")
    for row in range(3):
        print("|", " ".join(field[row * 3: 3 + row * 3]), "|")
    print(9 * "-")


# Main program

# Initial parameters
winner = None
current_turn = CHAR_X
turns_to_finish = 9

field = list(9 * " ")
print_field()

# Main game loop
while not game_finished():
    user_input = input("Enter the coordinates:")
    if user_input_correct():
        user_x, user_y = user_input.split()
        update_field(int(user_x), int(user_y), current_turn)
        current_turn = CHAR_X if current_turn == CHAR_O else CHAR_O
        print_field()
        check_winner()
        check_state()
