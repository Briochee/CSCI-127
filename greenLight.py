#Name: Rio Simpson
#Email: simpson.rions@gmail.com
#Date: 02-23-2023
#Program Description: this program draws a green shape

import turtle

gShape = turtle.Turtle()

turtle.colormode(255)
gShape.right(90)
gShape.backward(300)

for a in range(0,255,10):
    gShape.color(0,a,0)
    gShape.forward(10)
    gShape.pensize(a)
for b in range(255,0,-10):
    gShape.color(0,b,0)
    gShape.forward(10)
    gShape.pensize(b)