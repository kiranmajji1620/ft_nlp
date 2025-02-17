def total(galleons, sickles, knuts):
    return (galleons*17 + sickles)* 29 + knuts

coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), " knuts")
# print(total(coins)) # doesn't work since coins will go to galleons
print(total(*coins), " knuts")

print(total(galleons=100, sickles=50, knuts=25))

coins = {"galleons" : 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]))

print(total(**coins))

def f(*args, **kwargs):
    print("Positional: ", args)
    print("Keywords: ", kwargs)

f(100, 20, 30)
f(galleons = 100, sickles = 50, knuts = 25)

words = ["hai", "sai", "kiran"]
print(words)
wordsU = map(str.upper, words)
print(*wordsU)

# Filters
students = [
    {"name" : "Hermoine", "house" : "Gryffindor"},
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Ron", "house" : "Gryffindor"},
    {"name" : "Draco", "house" : "Slytherin"}
]

gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
# print(*gryffindors)

for gryffindor in gryffindors:
    print(gryffindor["name"])

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("sheep"*i)

def sheep(n):
    for i in range(n):
        yield "sheep"*i