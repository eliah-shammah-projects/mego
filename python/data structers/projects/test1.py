
import tkinter as tk 


def print_on_window (luach):


    window = tk.Tk()
    window.title("result")
    window.geometry("500x500")
    window.configure (bg = "lightblue")

    for i in range (3):
        for  y in range (3):

            cel = tk. Label (window, text = luach[i][y], font = ("Arial", 20), fg = "blue", bg = "lightblue", borderwidth=2, relief="sunken" )
            cel.grid (row = i, column = y )

    window.after(4000, window.destroy)

    window.mainloop()
