import random
import sys

import computer as computer

list=["Rock","Paper","Scissor"]
computer=random.choice(list)
man=False
man_score=0
comp_score=0
while True:
    player=input("Rock,Paper or Scissor:")
    if(player=="Rock"):
        if(computer=="Rock"):
            print("Tie. No points for both of u")
            print("Enter E if u want to exit the game")
        elif(computer=="Scissor"):
            print("You Destroyed the Computer's Scissor.\n 1 point for u")
            man_score+=1
            print("Enter E if u want to exit the game")
        elif(computer=="Paper"):
            print("Computer crushed ur rock with a paper.\n1 point for Computer")
            comp_score+=1
            print("Enter E if u want to exit the game")
    elif(player=="Paper"):
        if(computer=="Paper"):
            print("Tie. No points for both of u")
            print("Enter E if u want to exit the game")
        elif(computer=="Rock"):
            print("You Destroyed the Computer's Rock.\n 1 point for u")
            man_score+=1
            print("Enter E if u want to exit the game")
        elif(computer=="Scissor"):
            print("Computer cutted ur paper with a Scissor.\n1 point for Computer")
            comp_score+=1
            print("Enter E if u want to exit the game")
    elif(player=="Scissor"):
        if(computer=="Scissor"):
            print("Tie. No points for both of u")
            print("Enter E if u want to exit the game")
        elif(computer=="Rock"):
            print("Computer crushed ur scissors with a rock.\n1 point for Computer")
            comp_score+=1
            print("Enter E if u want to exit the game")
        elif(computer=="Paper"):
            print("You cutted the Computer's Paper.\n 1 point for u")
            man_score+=1
            print("Enter E if u want to exit the game")
    elif(player=="E"):
        print("Scores")
        print("Player's Score: {}".format((man_score)))
        print("Computer's Score: {}".format((comp_score)))
        break



