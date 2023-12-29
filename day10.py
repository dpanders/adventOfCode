import sys
import argparse
import re

class square:
    def __init__(self, char, row, col, prevSquare):
        self.char = char
        self.row = row
        self.col = col
        self.stepsCW = 0
        self.stepsCCW = 0
        self.dirs = getDirs(char)
        self.prevSquare = prevSquare

def getDirs(char):
        
    match(char):
        case '|':
            ret = {"north":"south", "south":"north"}
        case '-':
            ret = {"east":"west", "west":"east"}
        case 'L':
            ret = {"north":"east", "east":"north"}
        case 'J':
            ret = {"west":"north", "north":"west"}
        case '7':
            ret = {"west":"south", "south":"west"}
        case 'F':
            ret = {"east":"south", "south":"east"}
        case 'S':
            ret = {"east":"south", "south":"east"}
        case '.':
            ret = None

    return(ret)

def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input", type=str, default="no file")
    
    args = parser.parse_args()
    input=args.input

    map = []
    with open(input) as file:
        for line in file.readlines():
            row=[]
            newline = line.split()[0]
            for char in newline:
                row.append(char)
            map.append(row)
    breakout = False
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == 'S':
                breakout = True
                break
        if breakout:
            break
        
    # starting with S coordinate
    # go cw and count
    
    inDirList = ['east', 'south']
    paths = []
    for inDir in inDirList:
        first = True
        steps = 0
        prevSquare = square(map[row][col], row, col, None)
        paths.append(prevSquare)
        prevSquare.stepsCW = steps
        while map[row][col] != 'S' or first:
            first = False
            newSquare = square(map[row][col], row, col, prevSquare)
            steps += 1
            newSquare.stepsCW = steps
            match newSquare.dirs[inDir]:
                case "north":
                    row -= 1
                    inDir = "south"
                case "east":
                    col += 1
                    inDir = "west"
                case "south":
                    row += 1
                    inDir = "north"
                case "west":
                    col -= 1
                    inDir = "east"
            prevSquare = newSquare
            print(col, row, steps)


    # go CCW and count
    # go along first count until second count decreases? or is same?

    # print that count    



if __name__ == '__main__':
    sys.exit(main())


