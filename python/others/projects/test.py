import tkinter as tk 



def func (lab):
    b.destroy()
    lab.pack(expand = True)

window = tk.Tk()
window.geometry("300x300")
window.config(bg ="#FFCCCC")

lab = tk.Label(window, text = "ola!!", font = ("calibri", 30), bg ="#FFCCCC", fg = "#ED1A1A" )
b = tk.Button(window, text = "aperte", font = ("calibri", 30), bg ="#FFCCCC", fg = "#ED1A1A", command= lambda: func(lab) )
b.pack (expand=True)


window.after(10000, window.destroy)

window.mainloop()


