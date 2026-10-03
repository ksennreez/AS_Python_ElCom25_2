from main import toggle_light, check_win

def test_check_win():
    board_win = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert check_win(board_win) == True

    board_not_win = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert check_win(board_not_win) == False

def test_toggle_light():
    board = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    
    toggle_light(board, 2, 2)
    
    assert board[2][2] == 1
    assert board[1][2] == 1 
    assert board[3][2] == 1 
    assert board[2][1] == 1 
    assert board[2][3] == 1 
    
    assert board[0][0] == 0