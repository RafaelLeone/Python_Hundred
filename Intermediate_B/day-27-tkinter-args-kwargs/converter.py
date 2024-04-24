from tkinter import *


window = Tk()
window.title("Convert miles to km & lb to kg")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Miles to km.
## Labels.
miles_label = Label(text="Miles")
equals_km_label = Label(text="equals")
result_km_label = Label(text='0')
km_label = Label(text="km")

## Entry.
miles_entry = Entry(width=10)
miles_entry.insert(END, string="0")

## Button.
def calculate_km():
    miles = miles_entry.get()
    try:
        result_km_label.config(text=int(miles)*1.609344)
    except:
        result_km_label.config(text="(please insert a number above.)")

calculate_km_button = Button(text="Calculate", command=calculate_km)

## Placement.
miles_entry.grid(row=0, column=1)
miles_label.grid(row=0, column=2)
equals_km_label.grid(row=1, column=0)
result_km_label.grid(row=1, column=1)
km_label.grid(row=1, column=2)
calculate_km_button.grid(row=2, column=1)

### Separate systems.
tab_text = Label(text='', pady=20)
tab_text.grid(row=3, column=1)

# lb to kg.
## Labels.
lb_label = Label(text="lb")
equals_kg_label = Label(text="equals")
result_kg_label = Label(text='0')
kg_label = Label(text="kg")

## Entry.
lb_entry = Entry(width=10)
lb_entry.insert(END, string="0")

## Button.
def calculate_kg():
    lbs = lb_entry.get()
    try:
        result_kg_label.config(text=int(lbs)*0.45359237)
    except:
        result_kg_label.config(text="(please insert a number above.)")

calculate_kg_button = Button(text="Calculate", command=calculate_kg)

## Placement.
lb_entry.grid(row=4, column=1)
lb_label.grid(row=4, column=2)
equals_kg_label.grid(row=5, column=0)
result_kg_label.grid(row=5, column=1)
kg_label.grid(row=5, column=2)
calculate_kg_button.grid(row=6, column=1)

window.mainloop()
