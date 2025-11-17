

import tkinter as tk

letter = "o"

def fun ( i, j):
    global letter
    l = tk.Label(window, text = letter, font = ("arial", 26), bg = "#FFCCCC", fg = "red")
    l.grid(row = i, column = j)

    if letter == "o":
        letter = "x"
    else:
        letter = "o"

      

window = tk.Tk()
window.geometry("300x300")
window.config(bg ="#FFCCCC")

for i in range(3):

    window.columnconfigure(i, weight = 1)
    window.rowconfigure(i, weight = 1)



for y in range(3):
    for j in range(3):
        b = tk. Button (window, bg = "#FFCCCC", command= lambda y=y, j =j: fun(y,j) )
        b.grid (row = y, column = j)


window.mainloop()


