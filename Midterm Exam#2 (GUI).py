from tkinter import *
from tkinter import ttk
window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400+10+10")

def ColorChange():
    btn.configure(bg = "Yellow")

btn = Button(window, text = "Click to Change Color", command=ColorChange)
btn.place(x = 155, y = 155)



window.mainloop()
