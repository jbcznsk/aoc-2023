arquivo = open("input.txt")

MAX_RED   = 12
MAX_GREEN = 13
MAX_BLUE  = 14

RED = "red"
GREEN = "green"
BLUE = "blue"

def findColor(game, color):
    return int(game.split(color)[0].split(" ")[-2])

def getLineId(line):
    return int(line.split(":")[0].split(" ")[1])

def getNumberOfGames(line):
    for game in line.split(":")[1].split(";"):
        print(game)
        print(str(findColor(game, "red")) + "\t" + str(findColor(game, "green") + "\t" + str(findColor(game, "blue"))))
        print("")
    return len(line.split(";"))

sum = 0
for line in arquivo:
    games = line.split(":")[1].split(";")
    possible = True
    for game in games:
        print("Analising game " + game)
        if (findColor(game, RED) > MAX_RED or 
            findColor(game, GREEN) > MAX_GREEN or
            findColor(game, BLUE) > MAX_BLUE):
            print("Not Possible")
            possible = False
        else:
            print("Possible")
    if (possible):
        sum += getLineId(line)

print(sum)
