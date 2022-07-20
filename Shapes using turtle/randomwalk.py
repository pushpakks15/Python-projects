import turtle
from turtle import Turtle, Screen
from random import choice,randint
turtle.colormode(255)
timmy = Turtle()
timmy.shape("arrow")
timmy.pensize(10)
timmy.speed("fastest")
def random_color():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    timmy.pencolor(r, g, b)


def selection():
    list_of_direction=["heads","tails"]
    a=choice(list_of_direction)
    if a=="heads":
        timmy.left(90)
    else:
        timmy.right(90)

for i in range(1000):
    random_color()
    timmy.forward(30)
    selection()

















screen=Screen()
screen.exitonclick()