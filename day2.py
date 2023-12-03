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


class Game:
    def __init__(self, id):
        self.id = id
        self.sets=[]
    def addSet(self, set):
        """ takes in a dictionary and adds it to self.sets"""
        self.sets.append(Set)
        
    

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
    for game in gamesList:
        total += game.id
    print(total)





if __name__ == '__main__':
    sys.exit(main())
