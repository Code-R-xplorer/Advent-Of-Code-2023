import math

from utils import read_file

values = read_file(2, str, False)

games = []


class Game:
    def __init__(self, ID, rounds):
        self.ID = ID
        self.rounds = rounds


class Round:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


for value in values:
    gameNumber, subsetList = value.split(': ')
    gameID = int(gameNumber.split(' ')[1])
    roundsList = subsetList.split('; ')
    gameRounds = []
    for r in roundsList:
        currentRed, currentGreen, currentBlue = 0, 0, 0
        cubesList = r.split(', ')
        for cube in cubesList:
            count, colour = cube.split(' ')
            if colour == 'red':
                currentRed += int(count)
            if colour == 'green':
                currentGreen += int(count)
            if colour == 'blue':
                currentBlue += int(count)
        currentRound = Round(currentRed, currentGreen, currentBlue)
        gameRounds.append(currentRound)
    game = Game(gameID, gameRounds)
    games.append(game)

bagRed, bagGreen, bagBlue = 12, 13, 14

gameIDSum = 0

for game in games:
    gameValid = True
    for gameRound in game.rounds:
        if gameRound.red > bagRed or gameRound.green > bagGreen or gameRound.blue > bagBlue:
            gameValid = False
    if gameValid:
        gameIDSum += game.ID

# Part 1 = 1931
print(gameIDSum)

gamePowerSum = 0

for game in games:
    minRed, minGreen, minBlue = 0, 0, 0
    for gameRound in game.rounds:
        if gameRound.red > minRed:
            minRed = gameRound.red
        if gameRound.green > minGreen:
            minGreen = gameRound.green
        if gameRound.blue > minBlue:
            minBlue = gameRound.blue
    gamePowerSum += (minRed * minGreen * minBlue)

# Part 2 = 83105
print(gamePowerSum)
