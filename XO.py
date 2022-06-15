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