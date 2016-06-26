##Generate a random number between 1 and 9
##(including 1 and 9). Ask the user to guess
##the number, then tell them whether they guessed
##too low, too high, or exactly right.

from random import randint

def guessing():
    player = input("guess a number between 1 and 9: ")
    player = int(player)
    cpu = randint(1,9)
    if player == cpu:
        print("you guessed it! you win!")
    elif player > cpu:
        print("the house wins, you were too high")
    else:
        print("the house wins, you were too low")
    print("the winning number was {}".format(cpu))
guessing()
