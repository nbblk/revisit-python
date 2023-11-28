def hello(name, lang):
    greetings = {
        "english": "Hello",
    }
    greetings = {
        "spanish": "Hallo",
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)
          
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Say hello to someone',
    )

    parser.add_argument(
        '-n', '--name', metavar='name', type=str, required=True, help="the name of the person of someone")

    parser.add_argument(
        "-l", '--lang', metavar="lang", type=str, required=True, help="the language to use", choices=["english", "spanish"]
    )

    args = parser.parse_args()

    hello(args.name, args.lang)