##Make a one-player Rock-Paper-Scissors game.


from random import randint

player = input("rock, paper, scissors! what's your pick? ")

def python_input():
    play = randint(0,2)
    if play == 0:
        play = "rock"
    elif play == 1:
        play = "paper"
    else:
        play = "scissors"
    return play

computer = python_input()

print("I play {}".format(computer))

def who_wins(player, computer):
    if player == computer:
        print("it's a tie!")
    elif (computer == "rock" and
          player == "scissors" or
          computer == "scissors" and
          player == "paper" or
          computer == "paper" and
          player == "rock"):
        print("the computer wins !")
    else:
        print("you win !")

who_wins(player, computer)






    
