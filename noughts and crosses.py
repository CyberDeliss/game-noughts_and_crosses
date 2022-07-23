def display_board(board):
    print("\n"*100)
    for i in range(len(board),1,-3):
        line_game(*board[i-3:i])
        if i > 4:
            print('-----------')


def line_game(a,b,c):
    if a == '#':
        a = ' '
    if b == "#":
        b = ' '
    if c == "#":
        c = ' '
    print('   |   |   ')
    print(f' {a} | {b} | {c} ')
    print('   |   |   ')


def player_input():
    player1 = input("Please, choose the symbol 'x' or 'o'\n")
    if player1.lower() != 'x' and player1.lower() != 'o':
        right_player1 = player_input()
        return right_player1.lower()
    return player1.lower()


def position_input():
    _position = input("Please, choose the position from 1 to 9\n")
    if _position.isnumeric():
        _position = int(_position)
        if 1 <= _position and _position <= 9:
            return _position
        else:
            new_position = position_input()
            return new_position
    else:
        new_position = position_input()
        return new_position


def place_marker(_board, _marker, _position):
    if _board[_position] == '#':
        _board[position] = _marker
        return True
    else:
        return False


def win_check(_board, _mark):
    #  123     456     789     159     357     147     258     369
    win = False
    win_condition = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7], [1,4,7], [2,5,8], [3,6,9]]
    for condition in win_condition:
        if _board[condition[0]] == _board[condition[1]] == _board[condition[2]] == _mark:
            win = True
    return win

def space_is_full(_board):
    space = 0
    for i in range(1,len(_board)):
        if _board[i] == '#':
            space += 1
            return False
    if space == 0:
        print('Sorry, but no one win')
        return True

def replay():
    answer = input("Do you want to play again? 'Yes' or 'No'\n").lower()
    if answer == "yes" or answer == 'y':
        return True
    else:
        return False





############## Game ####################

while 1:
    # test_board = ['#','x','o','x','o','x','x','x','o','x']
    test_board = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    display_board(test_board)
    player = player_input()

    while not win_check(test_board, 'x') and not win_check(test_board, 'o') and not space_is_full(test_board):
        position = position_input()
        if place_marker(test_board, player, position):
            display_board(test_board)

            if player == 'x':
                player = 'o'
            else:
                player = 'x'
        else:
            continue
    if not replay():
        break



