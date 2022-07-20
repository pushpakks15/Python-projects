from turtle import Turtle,Screen
timmy=Turtle()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def reset():
    screen.resetscreen()

def turn_left():
    angle=0
    angle += 5
    timmy.left(angle)


def turn_right():
    angle=0
    angle += 5
    timmy.right(angle)


screen=Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=reset)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)










screen.exitonclick()