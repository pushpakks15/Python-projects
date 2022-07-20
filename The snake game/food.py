from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.color("red")
        self.penup()
        self.shapesize(0.5,0.5)
        self.refresh()

    def refresh(self):
        random_x=random.randint(0,280)
        random_y=random.randint(0,280)
        self.goto(random_x,random_y)

