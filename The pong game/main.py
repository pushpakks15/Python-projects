import time
from turtle import Turtle,Screen
from move import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen=Screen()
screen.title("THE PONG GAME")
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)

paddle1=Paddle(350,0)
paddle2=Paddle(-350,0)
bally=Ball()
scoreboard=Scoreboard()




screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")


slp=0.1
is_on=True
while is_on:

    time.sleep(slp)
    screen.update()
    bally.move()
    if bally.ycor() > 280 or bally.ycor() < -280:
        bally.bounce_y()
    if bally.distance(paddle1)<50 and bally.xcor()>320 or bally.distance(paddle2)<50 and bally.xcor()<-320:
        bally.bounce_x()
    if bally.distance(paddle1)>50 and bally.xcor()>380 or bally.distance(paddle2)>50 and bally.xcor()<-380:
        bally.bounce_x()
    if bally.xcor()>380:
        scoreboard.l_point()
        bally.goto(0, 0)
    if bally.xcor()<-380:
        scoreboard.r_point()
        bally.goto(0, 0)







screen.exitonclick()

