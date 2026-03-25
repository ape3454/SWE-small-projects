from turtle import Turtle
from random import randint

mikey = Turtle() # michelangelo
mikey.color("DarkOrange")
donnie = Turtle() # donatello
donnie.color("BlueViolet")
raphael = Turtle()
raphael.color("brown3")
leo = Turtle() # leonardo
leo.color("blue3")
turtles = [mikey, donnie, raphael, leo]
for turtle in turtles:
    turtle.shape("turtle")
    turtle.penup()

coord = (-160, 100)
for i, turtle in enumerate(turtles):
    turtle.goto(coord[0], coord[1] - 30 * i)
    turtle.pendown()

#race
for movement in range(100):
    for turtle in turtles:
        turtle.forward(randint(1, 5))

input("Press")