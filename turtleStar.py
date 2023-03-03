#Name: Rio Simpson
#Email: simpson.rions@gmail.com
#Date: Feburary 5th, 2023
#This program draws a star

import turtle
wn = turtle.Screen()

star = turtle.Turtle()

for i in range(6):
    star.forward(50)
    star.right(60)
    star.forward(50)
    star.left(120)

wn.exitonclick()
