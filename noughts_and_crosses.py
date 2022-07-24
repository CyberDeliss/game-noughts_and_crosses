"""
It is Game "Noughts and Crosses"
"""

def display_board(board):
    """
    :param board:
    :return: none. This function to print the board
    """
    print("\n"*100)
    for i in range(len(board),1,-3):
        line_game(*board[i-3:i])
        if i > 4:
            print('-----------')

def line_game(one, two, three):
    """
    This function to print one line from the board
    """
    if one == '#':
        one = ' '
    if two == "#":
        two = ' '
    if three == "#":
        three = ' '
    print('   |   |   ')
    print(f' {one} | {two} | {three} ')
    print('   |   |   ')

def player_input():
    """
    Player should to choose the side
    :return: 'x' or 'o'
    """
    player1 = input("Please, choose the symbol 'x' or 'o'\n")
    if player1.lower() != 'x' and player1.lower() != 'o':
        right_player1 = player_input()
        return right_player1.lower()
    return player1.lower()

def position_input():
    """
    Player should to choose the cell
    :return: position from 1 to 9
    """
    while True:
        _position = input("Please, choose the position from 1 to 9\n")
        try:
            _position = int(_position)
            if 1 <= _position <= 9:
                return _position
        except TypeError:
            continue

def place_marker(_board, _marker, _position):
    """
    If the cell is empty ('#'), change cell of _board (_position) to _marker
    :param _board:
    :param _marker: 'x' or 'o'
    :param _position: position from 1 to 9
    :return: True or False
    """
    if _board[_position] == '#':
        _board[position] = _marker
        return True
    return False


def win_check(_board, _mark):
    """
    True if player (_mark) is winner
    :param _board:
    :param _mark: 'x' or 'o'
    :return: True or False
    """
    #  123     456     789     159     357     147     258     369
    win = False
    win_condition = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                     [1, 5, 9], [3, 5, 7], [1, 4, 7],
                     [2, 5, 8], [3, 6, 9]]
    for condition in win_condition:
        if _board[condition[0]] == _board[condition[1]] == _board[condition[2]] == _mark:
            win = True
            # print(f"Player '{_mark}' is winner")
    return win

def space_is_full(_board):
    """
    True if the _board hasn't empty cells
    :param _board:
    :return: True or False
    """
    space = 0
    for i in range(1, len(_board)):
        if _board[i] == '#':
            space += 1
            return False
    # print('Sorry, but no one win')
    return True

def replay():
    """
    True if players want to play again
    :return: True or False
    """
    answer = input("Do you want to play again? 'Yes' or 'No'\n").lower()
    if answer in ("yes", "y"):
        return True
    return False

def game_continue(_board):
    """
    Conditions for stopping the game and
    answer can the game continue or not

    :param test_board: is board
    :return: True or False
    """
    player1 = 'x'
    player2 = 'o'

    # Condition for stop game:
    conditions = [win_check(_board, player1), # Someone is winner
                  win_check(_board, player2), # Someone is winner
                  space_is_full(_board)]  # All space is fill
    for condition in conditions:
        if condition:
            # Why game was stopped?
            if conditions[0]:
                print(f"Player '{player1}' is winner")
            elif conditions[1]:
                print(f"Player '{player2}' is winner")
            elif conditions[2]:
                print('Sorry, but no one win')
            return False
    return True


def change_player(_player):
    """
    Change player first on player second
    :param _player: 'x' or 'o'
    :return: 'o' or 'x'
    """
    if _player == "x":
        _player = 'o'
    else:
        _player = 'x'
    return _player

############## Game ####################

while 1:
    # test_board = ['#','x','o','x','o','x','x','x','o','x']
    test_board = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    display_board(test_board)
    player = player_input()

    while game_continue(test_board):
        position = position_input()
        if place_marker(test_board, player, position):
            display_board(test_board)

            player = change_player(player)

        else:
            continue

    if not replay():
        break
