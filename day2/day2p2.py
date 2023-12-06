arquivo = open("input.txt")

RED = "red"
GREEN = "green"
BLUE = "blue"

def findColor(game, color):
    if (game.find(color) == -1):
        return 0
    return int(game.split(color)[0].split(" ")[-2])

def getLineId(line):
    return int(line.split(":")[0].split(" ")[1])

sum = 0
for line in arquivo:
    
    maxRed   = 0
    maxGreen = 0
    maxBlue  = 0
    
    games = line.split(":")[1].split(";")
    for game in games:
        red   = findColor(game, RED)
        green = findColor(game, GREEN)
        blue  = findColor(game, BLUE)

        if (red > maxRed):
            maxRed = red

        if (green > maxGreen):
            maxGreen = green

        if (blue > maxBlue):
            maxBlue = blue

        print(red)
        print(green)
        print(blue)
        print("")
    print(maxRed)
    print(maxGreen)
    print(maxBlue)
    power = maxBlue * maxGreen * maxRed
    sum += power
    print(power)
    print(sum)
    print("==========")

print(sum)
