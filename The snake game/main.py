
import time
from turtle import Turtle, Screen
from snake import Snake

screen=Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("THE EPIC SNAKE GAME")
screen.tracer(0)

snake=Snake()
screen.listen()
screen.onkey("Up",snake.up)
screen.onkey("Down",snake.down)
screen.onkey("Left",snake.left)
screen.onkey("Right",snake.right)

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()

















screen.exitonclick()

