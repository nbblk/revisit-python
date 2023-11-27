import sys 
import random 
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:
    playerchoice = input('please enter rock(1), paper(2), or scissors(3):\n')
    player = int(playerchoice)

    if player < 1 | player > 3:
        sys.exit("you must enter 1, 2, or 3")

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("")
    print("player: " + str(RPS(player)).replace('RPS.', ''))
    print("computer: " + str(RPS(computer)).replace('RPS.', ''))
    print("")

    if player == 1 and computer == 3:
        print("you win!")
    elif player == 2 and computer == 1:
        print("computer win!")
    elif player == 3 and computer == 2:
        print("you win!")
    elif player == computer:
        print("tie!")
    else:
        print("computer wins!")

    playagain = input("play again? (y/n): ")    

    if playagain.lower() == "n":
        playagain = False
        print("thanks for playing!");
    else:
        playagain = True
        print("ok, here we go again!")

sys.exit("bye");
# print(RPS(1))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()



