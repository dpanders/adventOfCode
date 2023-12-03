import sys
import argparse


def getId(line):
    # assumes line is of the form:
    # Game x: blah blahblah
    tokens = line.split(":")
    token = tokens[0].split()
    return(int(token[1]))

def getSets(line):
    tokens = line.split(": ")
    setsStr = tokens[1]
    sets = setsStr.split("; ")
    return(sets)

def getSetDict(setStr):
    setDict = {}
    tokens = setStr.split(", ")
    
    for draws in tokens:
        pairs = draws.split()
        num = int(pairs[0])
        col = pairs[1]
        setDict[col] = num
        
    return(setDict)


# {"color": number}
class Set:
    def __init__(self, setDict):
        self.setDict = setDict
    def setPossible(self, limits):
        possible = True
        for color in self.setDict:
            if limits[color] < self.setDict[color]:
                possible = False
        return(possible)

class Game:
    def __init__(self, id):
        self.id = id
        self.sets=[]
    def addSet(self, set):
        """ takes in a dictionary and adds it to self.sets"""
        self.sets.append(set)
    def gamePossible(self, limits):
        possible = True
        for set in self.sets:
            if not set.setPossible(limits):
                possible = False
        return(possible)
    def maxEachColor(self):
        colorDict = {"red":0, "blue":0, "green":0}
        for color in colorDict:
            for set in self.sets:
                if color in set.setDict:
                    max = set.setDict[color]
                    if colorDict[color] < max:
                        colorDict[color] = max

        return(colorDict)
    

def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input", type=str, default="no file")
    
    args = parser.parse_args()
    input=args.input

    # list = [Game1, Game2, Game3, ...]
    #   Game = [Set1, Set2, Set3, ...]
    # 
    # empty list of Games
    # for each line
        # get ID
        # create a Game
            # get rounds
            # create each Round and add to Game
    gamesList = []
    with open(input) as file:
        for line in file.readlines():
            game = Game(getId(line))
            for setStr in getSets(line):
                setDict = getSetDict(setStr)
                set = Set(setDict)
                game.addSet(set)
            gamesList.append(game)
    
    # perform analysis:
    # for each game, count those below a certain number 
    total = 0
    # The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
    limits = {"red": 12, "green": 13, "blue": 14}
    for game in gamesList:
        if game.gamePossible(limits):
            total += game.id
    print(total)

    # part 2
    # find the max for each game and then multiple together and sum
    sum = 0
    for game in gamesList:
        maxEach = game.maxEachColor()
        power = 1
        for color in maxEach:
            power *= int(maxEach[color])
        sum += power
    print (sum)



if __name__ == '__main__':
    sys.exit(main())
