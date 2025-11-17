
import tkinter as tk 



def check_winner(l):
    for i in range(3):
        if l[i][0] == l[i][1] == l[i][2] != " ":
            return True, l[i][0]

    for i in range(3):
        if l[0][i] == l[1][i] == l[2][i] != " ":
            return True, l[0][i]

    if l[0][0] == l[1][1] == l[2][2] != " ":
        return True, l[0][0]
    
    if l[0][2] == l[1][1] == l[2][0] != " ":
        return True, l[0][2]

    return False, 0

       

luach = [[" " for i in range(3)] for y in range(3)]

letter = "o"

def game (  i, j, luach):
        global letter
        if luach [i][j] == " ":

              l = tk.Label(window, text = letter, font = ("arial", 26), bg = "#FFCCCC", fg = "red")
              l.grid(row = i, column = j)
              luach[i][j] = letter
              v = check_winner(luach)

              if v[0]:
                l2 = tk.Label(window, text = f"{v[1]} winn!!!" , font =("arial", 20))
                l2.grid(row=3, column=0, columnspan=3)
                window.after(3000, window.destroy)

              if letter == "o":
                 letter = "x"
              else:
                 letter = "o"
              return
        
        else:
           l2 = tk.Label(window, text = "is full", font =("arial", 20))
           l2.grid(row=3, column=0, columnspan=3)
           window.after(3000, l2.destroy)


       


window = tk.Tk()
window.geometry("300x300")
window.config(bg ="#FFCCCC")

for i in range(3):

    window.columnconfigure(i, weight = 1)
    window.rowconfigure(i, weight = 1)

for y in range(3):
    for j in range(3):
        b = tk. Button (window, bg = "#FFCCCC", command= lambda y=y, j =j: game(y,j, luach) )
        b.grid (row = y, column = j)
    

window.mainloop()
