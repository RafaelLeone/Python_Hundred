# import another_module
# import turtle
# from turtle import Turtle, Screen
from prettytable import PrettyTable


# Basics
# print(another_module.another_variable)

# timmy = turtle.Turtle()
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")

# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# Table
table = PrettyTable()

table.field_names = ["Name", "Type", "Type2",]
table.add_rows(
    [
        ["Pikachu", "Electric", "",],
        ["Pidgeot", "Normal", "Flying",],
    ]
)

table.align = "l"

print(table)
