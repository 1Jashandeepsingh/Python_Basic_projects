"""
WorkFlow 
1.Inpur from the user
2.computer choice randomaly
3.result print

Cases:
A.Rock
Rock=Rock => tie
Rock=Paper=>Paper win
Rock=Scissor = Rock win
b.Paper
Paper=Paper=>tie
Paper=Rock=Paper win
Paper=Scissor=Sciesor win
c.Sciesor
Sciesor=Sciesor = tie
Sciesor=Rock = Rock win
Sciesor=Paper = Sciesor win
"""

import random

item_list = ["Rock" , "Paper" , "Scissor"]

user_choice = input("Enter your move => Rock , Paper , Scissor =")
comp_choice = random.choice(item_list)

print(f"User Choice = {user_choice}, Computer Choice {comp_choice}")

if user_choice == comp_choice:
    print("Both choices same : tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("paper covers rock = computer win")
    else:
        print("Rock smashes scissor =  you win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper = computer win")
    else:
        print("paper covers rock = you win")
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts the paper = you win")
    else:
        print("Rock smashes Scissor = computer win")