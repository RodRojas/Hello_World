##Create a program that will play the “cows and bulls” game
##with the user. The game works like this:
##
##Randomly generate a 4-digit number. Ask the user to guess a
##4-digit number. For every digit that the user guessed correctly
##in the correct place, they have a “cow”. For every digit the user
##guessed correctly in the wrong place is a “bull.” Every time the
##user makes a guess, tell them how many “cows” and “bulls” they have.
##Once the user guesses the correct number, the game is over. Keep track
##of the number of guesses the user makes throughout teh game and
##tell the user at the end.
##
##Say the number generated by the computer is 1038. An example
##interaction could look like this:
##
##  Welcome to the Cows and Bulls Game! 
##  Enter a number: 
##  >>> 1234
##  2 cows, 0 bulls
##  >>> 1256
##  1 cow, 1 bull
##  ...

import random

def player():
    player = input("""Welcome to the Cows and Bulls Game!
              Enter a number: """)
    player = str(player).zfill(4)
    player = list(player)
    return player

def cpu():
    cpu = random.randint(0,9999)
    cpu = str(cpu).zfill(4)
    cpu = list(cpu)
    return cpu


def evaluate():
    player1 = player()
    cpu1 = cpu()
    print("you played {}".format(''.join(player1)))
    print("the computer played {}".format(''.join(cpu1)))
    score = {
        "cows": 0 ,
        "bulls": 0
        }
    for x in player1:
        if x in cpu1:
            score["cows"] += 1
        else:
            score["bulls"] +=1
    print(score)

evaluate()








              
