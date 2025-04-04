
from random import choice
n=int(input("enter the number of rounds:"))
choices = ["snake", "water", "gun"]
Rounds=1
points_user=0
points_computer=0
def game():
 global points_computer, points_user

 if choice_computer=="snake" and choice_user=="water" :
   points_computer +=1
 elif choice_computer=="snake" and choice_user=="gun" :
  points_user +=1
 elif choice_computer=="gun" and choice_user=="water" :
  points_user +=1
 elif choice_computer=="gun" and choice_user=="snake":
   points_computer +=1
 elif choice_computer=="water" and choice_user=="snake" :
  points_user +=1
 elif choice_computer=="water" and choice_user=="gun":
  points_user +=1
 else: (choice_computer=="water" and choice_user=="water") or (choice_computer=="snake" and choice_user=="snake") or (choice_computer=="gun" and choice_user=="gun")
 print("computer-"+choice_computer)
 print("points user:"+f"{points_user}"," points computer:"+f"{points_computer}")
while Rounds<=n:
 print("Round Number:"+f"{Rounds}")
 choice_computer = choice(choices)
 choice_user = input("snake, water , gun ?")
 game()
 Rounds +=1
if points_user>points_computer:
  print("You Win!")
elif points_computer>points_user :
  print("You lose")
else:
  print("It's a tie!")

