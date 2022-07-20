# 1.computer choice declare
import random
comp_choice=random.randint(1,100)
print("Welcome to the number guessing game")
print("Guess a number from 1-100")


# 2.Set difficulty
HARD_LEVEL_TURNS=5
EASY_LEVEL_TURNS=10





def compare(comp_choice,guess,turns):
    if comp_choice>guess:
      print("Too low\nGuess again")
      return turns-1
    elif comp_choice<guess:
      print("Too high\nGuess again")
      return turns-1
    else:
      print(f"Congrats you won!\nThe answer was {comp_choice}")
turns=0
      
def diff():
    diff=input("Set difficulty ,easy or hard: ")
    if diff=="hard":
      turns=HARD_LEVEL_TURNS
      return turns
    else:
      turns=EASY_LEVEL_TURNS
      return turns

  # 3.user guess
def game():
  turns=diff()
  guess=0
  while guess!=comp_choice:
      guess=int(input("Make a guess: "))
      print(f"The solution is {comp_choice}")
      turns=compare(comp_choice,guess,turns)
      print(f"You have {turns} attempts remaining.")
      if turns==0:
        print("Your no_of_attempts is over.You lost")
        return

game()

