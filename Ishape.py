#Name: Rio
#Email:
#Date: Feburary 14th, 2023
#This program draws an I in four different colors

import turtle
shapeI = turtle.Turtle()
shapeI.pensize(5)

for half in range(0,2):
    if half == 0:
        color = ["green", "blue"]
    elif half == 1:
        shapeI.left(90)
        color = ["cyan", "red"]
  
    shapeI.color(color[0])
    shapeI.forward(150)
    for h in range(2):
        shapeI.color(color[1])
        shapeI.left(90)
        shapeI.forward(50)
    for i in range(2):
        shapeI.right(90)
        shapeI.forward(50)
    shapeI.left(90)
    shapeI.forward(50)
   
