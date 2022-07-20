# import colorgram
# colors = colorgram.extract('color.jpg', 20)
import random

# color_list=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     color_seq=(r,g,b)
#     color_list.append(color_seq)
#
# print(color_list)
import turtle

color_list=[(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27)]
from turtle import Turtle, Screen
turtle.colormode(255)

timmy=Turtle()
timmy.pensize(10)
timmy.setheading(225)
timmy.penup()
timmy.hideturtle()
timmy.forward(300)
timmy.setheading(0)
timmy.pendown()
timmy.speed("fastest")
def move():
    for i in range(10):
        timmy.dot(random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()

for i in range(5):
    move()
    timmy.left(90)
    timmy.penup()
    timmy.forward(30)
    timmy.left(90)
    move()
    timmy.right(90)
    timmy.penup()
    timmy.forward(30)
    timmy.right(90)






screen = Screen()
screen.exitonclick()

