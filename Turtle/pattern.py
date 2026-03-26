from turtle import Turtle, pensize
import random
import time
import math
import colorsys

ss = 1000 #screensize

print("Spirals")
number = int(input("Input a number: "))
curviness = int(input("How curvy?(lower is less, changes depending on power scale) "))

spectrum = int(input("Choose colour spectrum (1 - 5)"))
match spectrum:
    case 1:
        rlim = (128, 255)
        glim = (128, 255)
        blim = (128, 255)
    case 2:
        rlim = (67, 202)
        glim = (0, 67)
        blim = (135, 255)
    case 3:
        rlim = (0, 67)
        glim = (135, 255)
        blim = (67, 202)
    case 4:
        rlim = (0, 135)
        glim = (135, 255)
        blim = (135, 255)
    case 5:
        rlim = (135, 255)
        glim = (0, 135)
        blim = (135, 255)
    case _:
        rlim = (0, 255)
        glim = (0, 255)
        blim = (0, 255)

cursor = Turtle()

def reset():
    cursor.penup()
    cursor.pensize(1)
    cursor.speed(10)
    cursor.ht()
    cursor.home()

reset()
cursor.screen.screensize(ss, ss)
cursor.screen.tracer(0)

for iteration in range(9999):
    offset = random.randint(0, 360)
    for i in range(number):
        cursor.screen.colormode(255)
        cursor.color(random.randint(*rlim), random.randint(*glim), random.randint(*blim))
        cursor.pendown()
        cursor.setheading(360 * i / number % 360 + offset)
        ccUp = True
        while not any(abs(i1) >= ss for i1 in cursor.position()):
            for i2 in range(1, 121):
                cursor.right(1 * (-1 if ccUp else 1))
                cursor.forward(cursor.pensize() / curviness)
                cursor.pensize(cursor.pensize() + ss / number / 628)
                if any(abs(i3) >= ss for i3 in cursor.position()):
                    break
                colour = list(colorsys.rgb_to_hsv(*[i/255 for i in cursor.pencolor()]))
                colour[2] = max(0, colour[2] - (colour[2] if colour[2] != 0 else 1) / 50 / (cursor.distance(ss/2 * (1 if ((offset + 360 * i / number % 360) - 90) < 90 else -1), ss/2 * (1 if ((offset + 360 * i / number % 360) - 180) > 0 else -1)))**1.39 / (number * cursor.pensize() * curviness**4))
                cursor.color(*[int(255 * i) for i in colorsys.hsv_to_rgb(*colour)])
            ccUp = not ccUp
        cursor.penup()
        reset()
        cursor.screen.update()


input()