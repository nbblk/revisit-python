import sys 
import random 
from enum import Enum

game_count = 0


def play_rps():  
    class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
        
    while True:
        playagain = input("play again? (y/n): ")

        if playagain.lower() == "n":
            playagain = False
            print("thanks for playing!");
            sys.exit("bye");

        else:
            playagain = True
            print("ok, here we go again!")


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

        def decide_winner(player, computer):
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
    
        game_result = decide_winner(player, computer)
        
        print(game_result)

        global game_count
        game_count += 1

        print("game count: " + str(game_count))

      

    # print(RPS(1))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)
    # sys.exit()

play_rps()

