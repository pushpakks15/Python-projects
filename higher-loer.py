from art import logo,vs
from game_data import data
import random
score=0

def A():
    print("Compare A:")
    print( f"{first_comp['name']},a {first_comp['description']}, from {first_comp['country']}.")

def B():
    print("Against B:")
    print (f"{second_comp['name']},a {second_comp['description']}, from {second_comp['country']}.")

game_over=False
op=False
while op is False:
   first_comp=random.choice(data)
   break
while game_over is False:
    if op==True:
      print(logo)
      first_comp==second_comp
      print("Compare A:")
      print (f"{second_comp['name']},a {second_comp['description']}, from {second_comp['country']}.")
    second_comp=random.choice(data)
    if op==False:
      print(logo)
      A()
    print(vs)
    B()
    if first_comp==second_comp:
        second_comp=random.choice(data)
    choice=input("Who has more followers? Type 'A' or 'B': ")
    if choice=="A":
        if first_comp['follower_count']>second_comp['follower_count']:
          score +=1
          print(f"You are right,your score is :{score}")
          op=True
        else:
          print(f"Sorry,that's wrong.Your final score is {score}")
          game_over=True
          op=True
    elif choice=="B":
        if first_comp['follower_count']<second_comp['follower_count']:
          score +=1
          print(f"You are right,your score is {score+1}")
          op=True
        else:
          print(f"Sorry,that's wrong.Your final score is {score}")
          game_over=True
          op=True
    

 


 
          








