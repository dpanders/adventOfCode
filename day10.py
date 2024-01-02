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
            ret = {"east":"east", "south":"south", "west":"west", "north":"north"}
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
    curPoints = [[row, col], [row, col]]
    curDir = []
    firstSteps = {}
    if row != 0:
        firstSteps["south"] = [row-1, col]
    if row != len(map):
        firstSteps["north"] = [row+1, col]
    if col != 0:
        firstSteps["east"] = [row, col-1]
    if col != len(map):
        firstSteps["west"] = [row, col+1]

    first = True
    for step in firstSteps:
        row = firstSteps[step][0]
        col = firstSteps[step][1]
        char = map[row][col]
        directions = getDirs(char)
        if directions:
            if step in directions:
                curDir.append(getDirs('S')[step])
                if first:
                    curPoints[0] = [row, col]
                    first = False
                else:
                    curPoints[1] = [row, col]


    # current position on step 1, curDir set properly

    steps = 1
    while ((curPoints[0][0] != curPoints[1][0]) or (curPoints[0][1] != curPoints[1][1])):
        steps += 1
        # print(steps)
        for i, dir in enumerate(curDir):
            match getDirs(map[curPoints[i][0]][curPoints[i][1]])[dir]:
                case "north":
                    curPoints[i][0] -= 1
                    curDir[i] = "south"
                case "east":
                    curPoints[i][1] += 1
                    curDir[i] = "west"
                case "south":
                    curPoints[i][0] += 1
                    curDir[i] = "north"
                case "west":
                    curPoints[i][1] -= 1
                    curDir[i] = "east"
    print(steps)


    # go CCW and count
    # go along first count until second count decreases? or is same?

    # print that count    



if __name__ == '__main__':
    sys.exit(main())


