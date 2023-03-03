#Name: Rio
#Email:
#Date: Feburary 5th, 2023
#This program draws a 15 sided polygon

import turtle
wn = turtle.Screen()

turtle1 = turtle.Turtle()
sides = 15

for i in range(sides):
 turtle1.forward(100)
 turtle1.left(360/sides)

wn.exitonclick()
