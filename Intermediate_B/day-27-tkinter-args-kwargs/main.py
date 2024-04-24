import tkinter
# from tkinter import *


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label.
my_label = tkinter.Label(text="I am Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)
# my_label.pack(side = "left")

my_label["text"] = "new"
my_label.config(text = "New Text", padx=20, pady=20)

# Entry.
input = tkinter.Entry(width=20)
input.grid(row=1, column=1)

# Button.
def button_clicked():
    received_text = input.get()
    my_label.config(text=received_text)
    print("I got clicked.")

button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(row=2, column=2)

window.mainloop()
