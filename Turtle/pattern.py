from turtle import Turtle
import random
import time
import math

colours = ["DarkSlateBlue", "green4", "PaleTurquoise", "red"]
random.shuffle(colours)

number = int(input("No. Turtles? "))
cursors = [Turtle() for i in colours[:number]]
for i, turtle in enumerate(cursors):
    turtle.penup()
    turtle.color(colours[i])
    turtle.pensize(5)
    turtle.shape("classic")
    turtle.speed("fastest")
    turtle.ht()
    turtle.goto(0, 0)

def rings(turtle):
    index = colours.index(turtle.fillcolor())
    xpos = [x - index for x in range(2 * index)]
    ypos = []
    for x in xpos:
        ypos.insert(0, round((index ** 2 - x ** 2) ** (1/2)))
        ypos.append(-1 * round((index ** 2 - x ** 2) ** (1/2)))

    turtle.pendown()
    for i, y in enumerate(ypos):
        time.sleep(0.5)
        turtle.goto(xpos[i % len(xpos)] * 5 , 5 * y)

time.sleep(1)

for cursor in cursors[::-1]:
    rings(cursor)

input()