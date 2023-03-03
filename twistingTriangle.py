#Name: Rio Simpson
#Email: simpson.rions@gmail.com
#Date: 02-22-2023
#Program Description: this program draws a twisting triangle
import turtle

triangle = turtle.Turtle()

for i in range(1,31):
    triangle.forward(i*10)
    triangle.left(121)