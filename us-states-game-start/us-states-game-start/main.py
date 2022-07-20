import turtle
import pandas
screen=turtle.Screen()
screen.title("US STATES GAME")
tim=turtle.Turtle()
image="C:/Users/Admin/PycharmProjects/us-states-game/us-states-game-start/us-states-game-start/blank_states_img.gif"
screen.addshape("C:/Users/Admin/PycharmProjects/us-states-game/us-states-game-start/us-states-game-start/blank_states_img.gif")
tim.shape(image)
score=0
is_on=True
list_of_answered_states=[]
list_of_remaining_states=[]
while is_on:
        ans=screen.textinput(title=f"States correct={score}/50",prompt="Type any one of the states:")
        answer=ans.title()
        data=pandas.read_csv("C:/Users/Admin/PycharmProjects/us-states-game/us-states-game-start/us-states-game-start/50_states.csv")
        list=[]
        states=data.state
        for each_state in states:
            list.append(each_state)
        xco=[]
        xcos=data.x
        for each_x in xcos:
            xco.append(each_x)
        yco=[]
        ycos=data.y
        for each_y in ycos:
            yco.append(each_y)

        if answer == "Exit":
            is_on=False
            list_of_remaining_states=[each_item for each_item in list if each_item not in list_of_answered_states ]
            data = pandas.DataFrame(list_of_remaining_states)
            data.to_csv("Learn.csv")

        if answer in list:
            score+=1
            position = list.index(answer)
            xcoordinate = xco[position]
            ycoordinate = yco[position]

            tom = turtle.Turtle()
            tom.hideturtle()
            tom.penup()
            tom.setposition(xcoordinate,ycoordinate)
            tom.write(answer, move=True, font=("Arial", 8, "normal"))
            list_of_answered_states.append(answer)
            if score==50:
                print("You won")
                break
















screen.exitonclick()