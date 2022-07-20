
def blackjack():
    play_blackjack=True
    while play_blackjack:
        bj=input("Do you want to play BLACKJACK? Yes or No : ").lower()
        if bj=="no":
            play_blackjack=False
        else:
            import random
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            user_cards=random.sample(cards,2)
            print(user_cards)
            current_score_user=sum(user_cards)
            print(f"The current score is {current_score_user}")
            comp_cards=random.sample(cards,2)
            final_score=sum(comp_cards)
            print(f"The first card of computer is {comp_cards[0]}")
            
            
            
              
                  
            game_over=False
            while not game_over:
              another_card=input("Type 'y' to get another card, type 'n' to pass: y  ")
              if another_card=="y":
                extra_card=random.choice(cards)
                if extra_card==11:
                  if sum(user_cards)>=20:
                    extra_card==1
                user_cards.append(extra_card)
                print(user_cards)
                current_score_user=sum(user_cards)
                print(f"The current score of user is {current_score_user}")
                print(f"The first card of computer is {comp_cards[0]}")
                another_card=input("Type 'y' to get another card, type 'n' to pass: y  ")
              if another_card=="y":
                extra_card=random.choice(cards)
                if extra_card==11:
                      if sum(user_cards)>=20:
                          extra_card==1
                user_cards.append(extra_card)
                print(user_cards)
                current_score_user=sum(user_cards)
                if sum(user_cards)>21:
                        print(f"The current score of user is {current_score_user}")
                        print(f"The current score of computer is {final_score}")
                        print("You went over.You lose")
                if sum(user_cards)<=21:
                    print(f"The current score of user is {current_score_user}")
                    print(f"The first card of computer is {comp_cards[0]}")
                
              while sum(comp_cards)<16:
                      extra_comp=random.choice(cards)
                      if extra_comp==11:
                          if sum(comp_cards)>=19:
                            extra_card==1
                      comp_cards.append(extra_comp)
                      final_score=sum(comp_cards)
                      if sum(comp_cards)>21:
                          print(f"The current score of user is {current_score_user}")
                          print(f"The current score of computer is {final_score}")
                          print("Opponent gone over.You win")
                          game_over=True
              if sum(user_cards)>21:
                print(f"The current score of user is {current_score_user}")
                print(f"The current score of computer is {final_score}")
                print("You went over.You lose")
                game_over=True
              if sum(user_cards)==21 and sum(comp_cards)==21:
                print(f"The current score of user is {current_score_user}")
                print(f"The current score of computer is {final_score}")
                print("It's a draw but computer wins.")
                game_over=True
              elif sum(user_cards)==21:
                print(f"The current score of user is {current_score_user}")
                print(f"The current score of computer is {final_score}")
                print("You win.")
                game_over=True
              elif sum(comp_cards)==21:
                print(f"The current score of user is {current_score_user}")
                print(f"The current score of computer is {final_score}")
                print("The computer wins.")
                game_over=True
              elif sum(user_cards)==sum(comp_cards):
                print(f"The current score of user is {current_score_user}")
                print(f"The current score of computer is {final_score}")
                print("Its a draw")
                game_over=True
              elif sum(user_cards)>sum(comp_cards) and sum(user_cards)<=21:
                print(f"The current score of user is {current_score_user}")
                print(f"The current score of computer is {final_score}")
                print("You win")
                game_over=True
              elif sum(user_cards)<sum(comp_cards):
                print(f"The current score of user is {current_score_user}")
                print(f"The current score of computer is {final_score}")
                print("You lose")
                game_over=True
             
                
blackjack()
          
            
