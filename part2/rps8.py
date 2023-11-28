import sys 
import random 
from enum import Enum


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description='Say hello to someone',
    )

    parser.add_argument(
        '-n', '--name', metavar='name', type=str, required=True, help="the name of the person of someone")

    args = parser.parse_args()

def rps(name=args.name):
    game_count = 0
    player_wins = 0
    python_wins = 0
    

    def play_rps():  
        nonlocal player_wins
        nonlocal python_wins
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


            playerchoice = input(f"\n'{name},please enter rock(1), paper(2), or scissors(3):\n'")
        
            player = int(playerchoice)

            if player < 1 | player > 3:
                sys.exit("you must enter 1, 2, or 3")

            computerchoice = random.choice("123")
            computer = int(computerchoice)

            print("")
            print(f"\nplayer:  {str(RPS(player)).replace('RPS.', '')}")
            print(f"\ncomputer: {str(RPS(computer)).replace('RPS.', '')}")
            print("")

            def decide_winner(player, computer):
                nonlocal name
                nonlocal player_wins
                nonlocal python_wins
                if player == 1 and computer == 3:
                    player_wins += 1
                    print("{name}, you win!")
                elif player == 2 and computer == 1:
                    python_wins += 1
                    print("sorry, {name}, computer win!")
                elif player == 3 and computer == 2:
                    player_wins += 1
                    print("{name}, you win!")
                elif player == computer:
                    print("tie!")
                else:
                    python_wins += 1
                    print("{name}, sorry, computer wins!")       
        
            game_result = decide_winner(player, computer)
            
            print(game_result)

            nonlocal game_count
            game_count += 1

            print(f"\ngame count: {str(game_count)}")
            print(f"\n{name}'s wins: {str(player_wins)}")
            print(f"\npython wins: {str(python_wins)}")
        
    return play_rps()

rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()

    rock_paper_scissors = rps(args.name)
