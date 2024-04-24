import tkinter
# from tkinter import *


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label.
my_label = tkinter.Label(text="I am Label", font=("Arial", 24, "bold"))
my_label.pack()
# my_label.pack(side = "left")

my_label["text"] = "new"
my_label.config(text = "New Text")

# Entry.
input = tkinter.Entry(width=50)
input.pack()

# Button.
def button_clicked():
    received_text = input.get()
    my_label.config(text=received_text)
    print("I got clicked.")

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

window.mainloop()
