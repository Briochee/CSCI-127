#Name: Rio
#Email:
#Date: 02-25-2023
#Program Description: This program draws a pentagon with turtle stamps

import turtle

cFBpentagon = turtle.Turtle()
cFBpentagon.color("#6495ED")

for i in range(5):
    cFBpentagon.forward(100)
    cFBpentagon.left(72)
    cFBpentagon.shape("turtle")
    cFBpentagon.stamp()
