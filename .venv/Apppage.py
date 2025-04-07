from tkinter import *
from email.mime import image
import tkinter as tk


root = tk.Tk()
root.textbox = tk.Entry(root, width=20)

root.geometry("400x400")

root.title("Community Forum")

root.sizefrom("user")

root.resizable(width=True, height=True)


def button_clicked():
    print("You clicked it!")

# Creating a button with specified options
button = tk.Button(root, 
                   text="Post a question", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100
                   
)




button.place(x=700, y=500)

button = tk.Button(root, 
                   text="Post a notice", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100
                   
)

button.place(x=1000, y=500)



root.mainloop()

