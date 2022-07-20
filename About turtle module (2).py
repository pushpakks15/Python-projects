from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=500)
is_on=False
user_bet= screen.textinput(title="Make a bet ", prompt="Which turtle will win the race? Enter the colour :")
print(user_bet)

timmy=Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.penup()
timmy.goto(-230,0)

jenny=Turtle()
jenny.shape("turtle")
jenny.color("blue")
jenny.penup()
jenny.goto(-230,20)

tony=Turtle()
tony.shape("turtle")
tony.color("green")
tony.penup()
tony.goto(-230,40)

sunny=Turtle()
sunny.shape("turtle")
sunny.color("yellow")
sunny.penup()
sunny.goto(-230,-20)

ronny=Turtle()
ronny.shape("turtle")
ronny.color("orange")
ronny.penup()
ronny.goto(-230,-40)

funny=Turtle()
funny.shape("turtle")
funny.color("purple")
funny.penup()
funny.goto(-230,-60)
list_of_turtles=[timmy,jenny,tony,sunny,ronny,funny]
if user_bet:
    is_on=True
while is_on:
    for turtle in list_of_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor()>200:
            winner = turtle.pencolor()

            is_on=False

            if user_bet == winner:
                print(f"Congrats,you won,The winner of the race is {winner}.")
            else:
                print(f"Sorry,you lost,The winner of the race is {winner}.")








screen.exitonclick()