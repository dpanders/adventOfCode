import sys
import argparse
import array

fileArray = []

def isTouching(row, col):
    checkList = [(row-1, col-1),
                 (row-1, col),
                 (row-1, col+1),
                 (row, col-1),
                 (row, col+1),
                 (row+1, col-1),
                 (row+1, col),
                 (row+1, col+1)
                 ]
    allPoints=[]
    for i, point in enumerate(checkList):
        if (point[0] >=0) and (point[1] >= 0) and (point[0] < len(fileArray)) and (point[1] < len(fileArray[0])):
            allPoints.append((point[0],point[1]))
    print(allPoints)
    countIt = False
    for point in allPoints:
        if isSymbol(fileArray[point[0]][point[1]]):
            countIt = True
    return(countIt)

def isSymbol(char):
    retVal = False
    if char != '.' and not char.isnumeric():
        retVal = True
    print(f"char {char} {retVal}")    
    return(retVal)


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input", type=str, default="no file")
    
    args = parser.parse_args()
    input=args.input
    
    with open(input) as file:
        for lines in file.readlines():
            nextRow = []
            for line in lines:
                for char in line:
                    if char != '\n':
                        nextRow.append(char)
                    
            # add each char to array column
            fileArray.append(nextRow)

    total = 0
    

    for i, row in enumerate(fileArray):
        currentNumber = 0
        inNumber = False
        touching = False
        for j, char in enumerate(row):
            if char.isnumeric() and not inNumber:
                inNumber = True
                touching = isTouching(i, j)
                currentNumber = int(char)
            elif char.isnumeric() and inNumber:
                if not touching:
                    touching = isTouching(i, j)
                currentNumber *= 10
                currentNumber += int(char)
            elif not char.isnumeric() and inNumber:
                if touching:
                    total += currentNumber
                inNumber = False
                currentNumber = 0
                touching = False
            # else - not a number and not in a number, continue with no changes
        # make sure we handle ending a line on a number, treat this like a "exiting" a number condition
        if inNumber:
            # we exited on a number
            if touching:
                total += currentNumber

    print(total)



if __name__ == '__main__':
    sys.exit(main())
