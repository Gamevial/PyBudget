from tkinter import*

root = Tk()
root.title("budgetprogram")
x = int(root.winfo_screenwidth()/2 - 800/2)
y = int(root.winfo_screenheight()/2 - 770/2)
root.geometry("800x770+{}+{}".format(x,y)); root.resizable(False, False)
root.config(bg="black")

guessVar = StringVar()
result = StringVar()
result.set("Indsast dit bugdet")


def hide():
    result.set("indtast dit budget")
    Button.configure(bg="red" , fg = "black" , text ="Se hvor mange penge du tilbage" , command=reveal)
    




root.mainloop()


