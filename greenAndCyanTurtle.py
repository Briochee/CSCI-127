#Name: Rio
#Email:
#Date: 02-23-2023
#Program Description: this program draws a cyan and green shape stemming from the starting point

import turtle

turtle.colormode(255)

gcTurtle = turtle.Turtle()

for i in range(0,2):
    for gc in range(0,255,5):
        if i == 0:
            color = (0, gc, 0)
        elif i == 1:
            color = (0, gc, gc)
        gcTurtle.color(color)
        gcTurtle.pensize(gc)
        gcTurtle.forward(5)
    gcTurtle.penup()
    gcTurtle.backward(255)
    gcTurtle.right(90)
    gcTurtle.pendown()
