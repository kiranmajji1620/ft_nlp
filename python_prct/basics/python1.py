import random
import statistics
import sys
import cowsay
import requests
import json

def rand_lib():
    coin = random.choice(["heads", "tails"])
    print(f"Toss {coin}")
    number = random.randint(1, 299)
    print(f"Random number : {number}")
    cards = ["jack", "queen", "king", "ace"]
    print(f"Original cards : {cards}")
    random.shuffle(cards)
    print(f"Shuffled cards : {cards}")

def stat_lib():
    print(statistics.mean([10, 90]))

def sys_lib():
    print(sys.argv)
    # Keeping the error checking separate from the code
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")

    # Handling errors
    try:
        print(f"Hello, my name is {sys.argv[1]}")
    except IndexError:
        print("Too few arguments")
    
    # using silce
    for arg in sys.argv[1:]:
        print(arg)
def cow_pack():
    if len(sys.argv) == 2:
        cowsay.cow("Hello" + sys.argv[1])
        # cowsay.cow("Hello")
        cowsay.trex("Helloo")

def api_call():
    if len(sys.argv) != 2:
        sys.exit()
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
    o = response.json()
    for result in o["results"]:
        print(result["trackName"])
    # print(json.dumps(response.json()), indent = 2)

def main():
    # rand_lib()
    # stat_lib()
    # sys_lib()
    # cow_pack()
    api_call()

if __name__ == "__main__":
    main()