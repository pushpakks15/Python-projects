from turtle import Turtle,Screen
from random import randint
timmy=Turtle()
# timmy.color("blue")
timmy.shape("arrow")
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# for t in range (10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
timmy.speed(3)
for sides in range(3, 11):
    for steps in range(1, sides):
        timmy.forward(100)
        angle = 360/sides
        timmy.right(angle)
        timmy.color("blue")
    timmy.forward(100)
    timmy.right(angle)








screen=Screen()
screen.exitonclick()