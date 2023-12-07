import sys
import argparse
import re

class Card:
    def __init__(self, round, winNumList, drawNumList):
        self.round = round
        self.winNumList = winNumList
        self.drawNumList = drawNumList
        self.copies = 1
    def points(self):
        points = 0
        first = True 
        for num in self.winNumList:   
            if num in self.drawNumList:
                if first:
                    points = 1
                    first = False
                else:
                    points *= 2
                    # print("double match")
        return(points*self.copies)
    def matches(self):
        match = 0
        for num in self.winNumList:
            print (f"num: {num}, drawList {self.drawNumList}")
            if num in self.drawNumList:
                match += 1
        return(match)
    def addCopy(self, num):
        self.copies+=num

def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input", type=str, default="no file")
    
    args = parser.parse_args()
    input=args.input
    
    cardList = []
    with open(input) as file:
        for line in file.readlines():
            # m = re.search("(?:\d+{6})", line)
            winNumList = []
            drawNumList = []
            # print(line)
            for i, token in enumerate(line.split()):
                if i == 1:
                    round = token[:-1]
                # elif i>=2 and i<=6:
                elif i>=2 and i<=11:
                    winNumList.append(token)
                # elif i>=8 and i<=15:
                elif i>=13 and i<=37:
                    drawNumList.append(token)
            # print(round, winNumList, drawNumList)
            newCard = Card(round, winNumList, drawNumList)
            cardList.append(newCard)
                    
    total = 0
    for cards in cardList:
        # print(cards.round, cards.points())
        total += cards.points()

    # part 2
    total = 0
    for i, cards in enumerate(cardList):
        matches = cards.matches()
        copies = cards.copies
        for j in range(copies):
            for k in range(matches):
                # print (i+j+1, end="")
                cardList[i+k+1].addCopy(1)
        print()
    
    for cards in cardList:
        print(cards.copies)
        total += cards.copies
    

    print(total)
if __name__ == '__main__':
    sys.exit(main())

