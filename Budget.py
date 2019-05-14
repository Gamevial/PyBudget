# -*- coding:utf-8 -*-
from tkinter import *
from tkinter import messagebox
from distutils import command

budget = 0
#Kommentar:
root = Tk()
root.title("Budget Regner")
Pos = int(root.winfo_screenmmwidth()/700/2)
pos = int(root.winfo_screenmmheight()/700/2)
root.geometry("700x600")
root.config(bg="black")


#ny '

    
under = Label(text="Det her progam vil hjælpe dig med at holde styr på din økonomi", bg="black", fg="pink", font="times 15 bold")

tit = Label(text="Budget Regner", bg="black", fg="pink", font="Times 40 bold", )

tit.place(relx=0.5, rely=0.05, anchor=CENTER)
under.place(relx=0.5, rely=0.13, anchor=CENTER)

#title = Label(root, text="Dit nuværende budget", bg="black", fg="pink" , font="Times 15 bold")

#title.place(relx=0.25, rely=0.6, anchor=CENTER)


 
#Hej = StringVar()
#Hej.set("")
#san = Entry(root, fg="pink", bg="black", textvariable=Hej, relief="ridge", insertbackground="pink")

#san.pack()
#san.insert(END, "")

#lol = Button(root, text="tryk her", fg="pink", command=lambda: Hej.set(""))
#text = Label(root, fg="pink", bg="black", textvariable=Hej)

#lol.place(relx=0.25, rely=0.7, anchor=CENTER)
#san.place(relx=0.25, rely=0.65, anchor=CENTER)

#text.place(relx=0.25, rely=0.75, anchor=CENTER)



#ny

def subtract(m):
     global budget
     budget = budget - m.get()
     m.set("")
     messagebox.showinfo("hej", budget)
     

title = Label(root, text="Brugte penge", bg="black", fg="pink", font="Times 20 bold")

title.place(relx=0.5, rely=0.6, anchor=CENTER)

Nej = DoubleVar()
Nej.set("")
san1 = Entry(root, fg="pink", bg="black", textvariable=Nej, relief="ridge", insertbackground="pink", font="Times 12 bold")

san1.pack()
san1.insert(END, "")

knap = Button(root, text="tryk her", fg="pink", command=lambda: subtract(Nej))
text = Label(root, fg="pink", bg="black", textvariable=Nej)

knap.place(relx=0.5, rely=0.7, anchor=CENTER)
san1.place(relx=0.5, rely=0.65, anchor=CENTER)

text.place(relx=0.5, rely=0.75, anchor=CENTER)



#ny
def remember(b):
    global budget; budget = b.get()
    messagebox.showerror("budget", budget)
    b.set("")

drage = Label(root, text="Indtast dit budget", bg="black" , fg="pink", font="Times 20 bold")

drage.place(relx=0.25, rely=0.33, anchor=CENTER)

sej = DoubleVar()
sej.set("")
stddd1 = Entry(root, fg="pink", bg="black", textvariable=sej, relief="ridge", insertbackground="pink", font="times 12 bold")

stddd1.pack()
stddd1.insert(END, "")

stddd2 = Button(root, fg="pink", text="Tryk her", command=lambda: remember(sej))
stddd3 = Label(root, fg="pink", bg="black", textvariable=sej)

stddd1.place(relx=0.25, rely=0.38, anchor=CENTER)

stddd2.place(relx=0.25, rely=0.43, anchor=CENTER)

stddd3.place(relx=0.25, rely=0.48, anchor=CENTER)



# ny
def add(c):
    global budget; budget, budget = c.get()
    budget = c.get() + budget
    messagebox.showerror("budget", budget)
    c.set("")
#     global budget; budget, budget = b.get()
#     budget = c.get() + budget
#     messagebox.showerror("budget", budget)
#     c.set("")
    
    
til = Label(root, text="Tilføj beløbet til budget", bg="black" , fg="pink" , font="Times 20 bold")

til.place(relx=0.75, rely=0.33, anchor=CENTER)

cazo = StringVar()
cazo.set("")
stddd1 = Entry(root, fg="pink", bg="black", textvariable=cazo, relief="ridge", insertbackground="pink", font="Times 12 bold")

stddd1.pack()
stddd1.insert(END, "")


stddd2 = Button(root, fg="pink", text="Tryk her", command=lambda: cazo.set(""))
stddd3 = Label(root, fg="pink", bg="black", textvariable=cazo)

stddd1.place(relx=0.75, rely=0.38, anchor=CENTER)

stddd2.place(relx=0.75, rely=0.43, anchor=CENTER)

stddd3.place(relx=0.75, rely=0.48, anchor=CENTER)  

    



root.mainloop()