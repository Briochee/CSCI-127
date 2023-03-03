#Name: Rio Simpson
#Email: simpson.rions@gmail.com
#Date: 02-23-2023
#Program Description: this program draws a cyan and green shape stemming from the starting point

import turtle

gcTurtle = turtle.Turtle()
turtle.colormode(255)

for i in range(0, 255, 5):  
    gcTurtle.color(0, i, 0)
    gcTurtle.pensize(i)
    gcTurtle.forward(5)

gcTurtle.penup()
gcTurtle.backward(255)
gcTurtle.right(90)
gcTurtle.pendown()

for i in range(0, 255, 5):  
    gcTurtle.color(0, i, i)
    gcTurtle.pensize(i)
    gcTurtle.forward(5)
