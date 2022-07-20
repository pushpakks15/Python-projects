from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,xco,yco):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(4, 2)
        self.goto(xco, yco)

    def go_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def go_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)
