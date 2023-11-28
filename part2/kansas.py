import random

song = "home on the range"

def randomfunfact():
    funfacts = [
        "Kansas is the flattest state in the US",
        "Kansas is the 15th largest state in the US",
        "Kansas is the 34th most populous state in the US",
        "Kansas is the 13th most densely populated state in the US",
        "Kansas is the 7th least densely populated state in the US",
        "Kansas is the 5th most productive agricultural state in the US",
        "Kansas is the 8th largest oil-producing state in the US",
        "Kansas is the 7th largest coal-producing state in the US",
        "Kansas is the 8th largest natural gas-producing state in the US",
        "Kansas is the 8th largest wind energy-producing state in the US",
    ]

    index = random.choice("0123")

    print(funfacts[int(index)])


# if __name__ == "__main__":
randomfunfact()
