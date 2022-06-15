def player_input():
    player1 = None
    player2 = None
    while player1 not in ["X", "O"]:
        player1 = input("What mark do you want to play? X or O: ")
        if player1 not in ["X", "O"]:
            print("Invalid choose, please choose X or O: ")
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    print(f"player 1 is {player1}")
    print(f"player 2 is {player2}")
    return player1, player2

def place_marker(boardlist, player, position):
    boardlist[position - 1] = player
    return boardlist

def display_board(boardlist):
    board = f"""  
    {boardlist[6]} | {boardlist[7]} | {boardlist[8]}
    {boardlist[3]} | {boardlist[4]} | {boardlist[5]}
    {boardlist[0]} | {boardlist[1]} | {boardlist[2]}
            """
    print(board)

def win_check(board, mark):
    if (
        board[0] == board[1] == board[2] == mark
        or board[3] == board[4] == board[5] == mark
        or board[6] == board[7] == board[8] == mark
        or board[0] == board[3] == board[6] == mark
        or board[1] == board[4] == board[7] == mark
        or board[2] == board[5] == board[8] == mark
        or board[0] == board[4] == board[8] == mark
        or board[2] == board[4] == board[6] == mark
    ):
        return True
    else:
        return False

def choose_first():
    pass

def space_check(board, position):
    if board[position - 1] == "":
        return True
    else:
        print("Choose another position")
        return False

def full_board_check(board):
    if "" not in board:
        print("The games is TIED")
        return True
    else:
        return False

def player_choice(boardlist, player):
    p_choice = int(input("What position do you want to mark? "))
    if p_choice in range(1, 10):
        if space_check(boardlist, p_choice):
            boardlist = place_marker(boardlist, player, p_choice)
            if win_check(boardlist, player):
                print(f"{player} is the winner")
                return True
            elif full_board_check(boardlist):
                return True
            display_board(boardlist)
        else:
            player_choice(boardlist, player)
    return False