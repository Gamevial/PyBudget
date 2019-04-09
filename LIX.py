from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Budget")
x = int(root.winfo_screenwidth()/2 - 800/2)
y = int(root.winfo_screenheight()/2 - 770/2)
root.geometry("800x770+{}+{}".format(x,y)); root.resizable(False, False)
root.config(bg="white")

MathButtonStyle = ttk.Style()
MathButtonStyle.theme_use("clam")
MathButtonStyle.configure(
    "MathButton.TButton", 
    foreground="white", 
    background="black", 
    font="Times 20 bold", 
    bordercolor="blue", 
    lightcolor="blue", 
    darkcolor="blue", 
    padding=13, 
    width=27
    )

T = Entry(font="Times 30 bold", bg="white", fg="black", relief="ridge", insertbackground="blue")
T.pack()
T.insert(END, "")

knap = ttk.Button(style="MathButton.TButton", bg="white", fg="black", text="Hejsa")
knap.pack()

guessVar = StringVar()
result = StringVar()
result.set("Type your budget")



title = Label(text="Budget Calculator", bg="white", fg="black", font="Times 40 bold")
pressEnter = Label(text="Type the amount of money", fg="black", bg="white", font="Times 20 bold")

T.place(relx=0.5, rely=0.43, anchor=CENTER)
title.place(relx=0.5, rely=0.15, anchor=CENTER)
pressEnter.place(relx=0.5, rely=0.38, anchor=CENTER)


root.mainloop()