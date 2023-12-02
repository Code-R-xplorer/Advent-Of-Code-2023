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
    # Remove the 'Game' part as we only need the number
    gameID = int(gameNumber.split(' ')[1])
    roundsList = subsetList.split('; ')
    gameRounds = []
    # Each game is split into multiple rounds
    for r in roundsList:
        currentRed, currentGreen, currentBlue = 0, 0, 0
        # Split the round into the list of the cubes
        cubesList = r.split(', ')
        # If a cube colour is present then increase the respective count
        for cube in cubesList:
            count, colour = cube.split(' ')
            if colour == 'red':
                currentRed += int(count)
            if colour == 'green':
                currentGreen += int(count)
            if colour == 'blue':
                currentBlue += int(count)
        # Create a Round object and append the totals to the game's rounds
        currentRound = Round(currentRed, currentGreen, currentBlue)
        gameRounds.append(currentRound)
    # At the end of a game create a Game object and add the id and rounds for that game
    game = Game(gameID, gameRounds)
    games.append(game)

# How many cubes of each colour are in the bag
bagRed, bagGreen, bagBlue = 12, 13, 14

gameIDSum = 0

for game in games:
    gameValid = True
    for gameRound in game.rounds:
        # For each round if any colour is greater than the cubes in the bag, the game is impossible and so is invalid
        if gameRound.red > bagRed or gameRound.green > bagGreen or gameRound.blue > bagBlue:
            gameValid = False
    if gameValid:
        gameIDSum += game.ID

# Part 1 = 1931
print(gameIDSum)

gamePowerSum = 0

# Now to find the minimum number of cubes needed in a bag for each game
for game in games:
    minRed, minGreen, minBlue = 0, 0, 0
    for gameRound in game.rounds:
        if gameRound.red > minRed:
            minRed = gameRound.red
        if gameRound.green > minGreen:
            minGreen = gameRound.green
        if gameRound.blue > minBlue:
            minBlue = gameRound.blue
    # The power set of each game is the minimum number of cubes in the bag for each colour multiplied together
    gamePowerSum += (minRed * minGreen * minBlue)

# Part 2 = 83105
print(gamePowerSum)
