


def display_board(luach):
    for i in range(3):
        for y in range(3):
            print("|",luach[i][y], end="|")
        print("")
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
            print("Please enter a valid number.")

def check_winner(l):
    winner = False
    if l[0][0] == l[1][1] == l[2][2]:
        winner = True
        if l[0][0] == "o":
            print("o winn")
            return winner
        elif l[0][0] == "x":
            print("x winn")
            return winner

    if l[0][1] == l[1][1] == l[2][1]:
        winner = True
        if l[0][1] == "o":
            print("o winn")
            return winner
        elif l[0][1] == "x":
            print("x winn")
            return winner

    if l[0][2] == l[1][1] == l[2][0]:
        winner = True
        if l[0][2] == "o":
            print("o winn")
            return winner
        elif l[0][2] == "x":
            print("x winn")
            return winner

    if l[1][0] == l[1][1] == l[1][2]:
        winner = True
        if l[1][0] == "o":
            print("o winn")
            return winner
        elif l[1][0] == "x":
            print("x winn")
            return winner

    if l[2][0] == l[2][1] == l[2][2]:
        winner = True
        if l[2][0] == "o":
            print("o winn")
            return winner
        elif l[2][0] == "x":
            print("x winn")
            return winner

    if l[0][0] == l[1][0] == l[2][0]:
        winner = True
        if l[0][0] == "o":
            print("o winn")
            return winner
        elif l[0][0] == "x":
            print("x winn")
            return winner

    if l[0][2] == l[1][2] == l[2][2]:
        winner = True
        if l[0][2] == "o":
            print("o winn")
            return winner
        elif l[0][2] == "x":
            print("x winn")
            return winner
    if l[0][0] == l[0][1] == l[0][2]:
      winner = True
      if l[0][0] == "o":
        print("o winn")
        return winner
      elif l[0][0] == "x":
        print("x winn")
        return winner


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
