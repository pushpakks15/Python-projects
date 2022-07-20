from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1,1)
        self.color("white")
        self.x_move=10
        self.y_move=10



    def move(self):
        new_xcor=self.xcor()+ self.x_move
        new_ycor=self.ycor()+ self.y_move
        self.goto(new_xcor,new_ycor)

    def bounce_y(self):
        self.y_move *=-1

    def bounce_x(self):
        self.x_move *=-1



