import random

User_choice=int(input("enter a number: 0:rock 1:paper 2:scissor."))
comp_choice=random.randint(0,2)
print ("computer choice:")
print(comp_choice)

if User_choice<0 or User_choice>2:
      print("invalid")

if User_choice==0 and comp_choice==0:
      print("game is draw")

if User_choice>comp_choice:
      print("you win")

if comp_choice>User_choice:
      print("you lose")

if comp_choice==2 and User_choice==0:
      print("you win")

if User_choice==2 and comp_choice==0:
      print("you lose")
