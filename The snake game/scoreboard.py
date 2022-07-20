from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)       
        self.write(f"SCORE={self.score}",move=False,align="center",font=('Cambria', 18, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",move=False,align="center",font=('Cambria', 18, 'normal'))



    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE={self.score}", move=False, align="center", font=('Cambria', 18, 'normal'))







