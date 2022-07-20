import turtle
from turtle import Turtle, Screen
from random import choice,randint
turtle.colormode(255)
timmy = Turtle()
timmy.shape("arrow")

timmy.speed("fastest")
def random_color():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    timmy.pencolor(r, g, b)
for i in range(0,75):
    timmy.circle(200)
    current_heading=timmy.heading()
    timmy.setheading(current_heading+5)

    random_color()







screen=Screen()
screen.exitonclick()