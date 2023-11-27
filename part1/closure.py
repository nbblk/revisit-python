# Closure is a function that returns a function

def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " has no coins left.")        
        
    return play_game

tommy = parent_function("Tommy", 3)
jack = parent_function("Jack", 5)

tommy()
tommy()

jack()

tommy()