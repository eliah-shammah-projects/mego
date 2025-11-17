import tkinter as tk 


def print_on_window (luach):


    window = tk.Tk()
    window.title("result")
    window.geometry("200x200")
    window.configure (bg = "lightblue")


    for i in range(3):
        window.columnconfigure(i, weight=1)
        window.rowconfigure(i, weight=1)

    for i in range (3):
        for  y in range (3):

            cel = tk. Label (window, text = luach[i][y], font = ("Arial", 20), fg = "blue", bg = "lightblue", borderwidth=2, relief="sunken" )
            cel.grid (row = i, column = y )
            
    window.after(10000, window.destroy)

    window.mainloop()


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

def print_txt(luach):
    with open("resultado.txt", "a") as f:
        for i in range(3):
            f.write("|".join(luach[i]) + "\n")
            if i < 2:
                f.write("_" * 5 + "\n")
       

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
            print_txt(l)

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
            print_txt(l)

            break

luach = [[" " for i in range(3)] for y in range(3)]
play_game(luach)
print_on_window (luach)