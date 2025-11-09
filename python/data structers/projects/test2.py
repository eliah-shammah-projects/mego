


def display_board(luach):
    for i in range(3):
        for y in range(3):
            print("|",luach[y][i], "|", end = "")
        print ("")
        if i < 2:
            print ( "----------------")
    return luach

def player_input(c, luach):
    print("enter the number of the row and column")
    for i in range(9):
        try:
            row = int(input("Row: "))
            while row > 2 or row < 0:
                print("number out of the limit")
                row = int(input("Row: "))

            column = int(input("Column: "))
            while column > 2 or column < 0:
                print("number out of the limit")
                column = int(input("Column: "))

            if luach[row][column] == " ":
                luach[row][column] = c
                break
            else:
                print("its full")
        except ValueError:
            print("Please enter only numbers")

def check_winner(l):
    for i in range(3):
        if l[i][0] == l[i][1] == l[i][2] != " ":
            print(f" '{l[i][0]}' winn")
            return True

    for i in range(3):
        if l[0][i] == l[1][i] == l[2][i] != " ":
            print(f" '{l[0][i]}' winn")
            return True

    if l[0][0] == l[1][1] == l[2][2] != " ":
        print(f"  '{l[0][0]}' winn")
        return True
    if l[0][2] == l[1][1] == l[2][0] != " ":
        print(f" '{l[0][2]}' winn")
        return True

    return False


def chek_full(luach):
    for i in luach:
        for y in i:
            if y == " ":
                return False
    return True

def play_game(l):
    full = chek_full(l)
    if full:
        print("is full")
        return

    print("hellow. let start the game")
    display_board(l)

    for i in range(5):
        full = chek_full(l)
        if full:
            print("is full")
            return
        print("player o please choose your choice")
        player_input("o", l)
        winner = check_winner(l)
        display_board(l)
        if winner:
            check_winner(l)
            break

        full = chek_full(l)
        if full:
            print("is full")
            return
        print("player x please choose your choice")
        player_input("x", l)
        winner = check_winner(l)
        display_board(l)
        if winner:
            check_winner(l)
            break

luach = [[" " for i in range(3)] for y in range(3)]
play_game(luach)
