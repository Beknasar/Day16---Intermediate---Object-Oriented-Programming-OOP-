# from turtle import Turtle, Screen
# tom = Turtle()
# tom.shape('turtle')
# tom.color('magenta', "DarkGreen")
# tom.forward(100)


# my_screen = Screen()
# my_screen.bgcolor("DeepSkyBlue")
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

# Coronavirus model
# from turtle import *
# color("green")
# bgcolor('black')
# speed(11)
# hideturtle()
# b = 0
# while b < 200:
#     right(b)
#     forward(b * 3)
#     b += 1
# exitonclick()


from prettytable import PrettyTable
print("Table 1")
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

print("Table 2")
table2 = PrettyTable()
table2.field_names = ['Pokemon Name', "Type"]
table2.add_rows(
    [
        ["Pikachu", "Electric"],
        ['Squirtle', 'Water'],
        ['Charmander', "Fire"],
    ]
)
print(table2)
