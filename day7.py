import sys
import argparse
import re

CARDRANK = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q': 12, 'K':13, 'A':14}
CARDRANK2 = {'J':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'Q': 12, 'K':13, 'A':14}
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.binScore = scoreHand(hand)
        self.handVal = handVal(hand)
        self.binScore2 = scoreHand2(hand)
        self.handVal2 = handVal2(hand)

class Rank:
    def __init__(self):
        self.hands = []

def handVal(hand):
    value = CARDRANK[hand[0]] * 14**4 + CARDRANK[hand[1]] * 14**3 + CARDRANK[hand[2]] * 14**2 + CARDRANK[hand[3]] * 14 + CARDRANK[hand[4]]   
    return(value) 

def handVal2(hand):
    value = CARDRANK2[hand[0]] * 14**4 + CARDRANK2[hand[1]] * 14**3 + CARDRANK2[hand[2]] * 14**2 + CARDRANK2[hand[3]] * 14 + CARDRANK2[hand[4]]   
    return(value) 

def scoreHand(hand):
    # return 1-7
    # 7 for five of kind
    # 6 for four of kind
    # 5 for full house
    # 4 for three of a kind
    # 3 for two pair
    # 2 for one pair
    # 1 for high card

    # search for 5 of a kind
    # search for 4 of a kind
    # search for full house * tricky
    # search for 3 of a kind (assume not full house)
    # search for 2 pair (assume not full house)
    # search for pair (assume nothing else)

    # or, count occurrence of each card, then sort
    # 5, 5, 5, 5, 5 = 25
    # 4, 4, 4, 4, 1 = 17
    # 3, 3, 3, 2, 2 = 13
    # 3, 3, 3, 1, 1 = 11
    # 2, 2, 2, 2, 1 = 9
    # 2, 2, 1, 1, 1 = 7
    # else
    pattern = []
    for card in hand:
        pattern.append(hand.count(card))
    pattern.sort(reverse=True)
    if pattern == [5, 5, 5, 5, 5]:
        return (7)
    elif pattern == [4, 4, 4, 4, 1]:
        return (6)
    elif pattern == [3, 3, 3, 2, 2]:
        return (5)
    elif pattern == [3, 3, 3, 1, 1]:
        return (4)
    elif pattern == [2, 2, 2, 2, 1]:
        return (3)
    elif pattern == [2, 2, 1, 1, 1]:
        return (2)
    else:
        return (1)

def scoreHand2(hand):
    score = scoreHand(hand)
    
    if 'J' in hand:
        for joker in CARDS:
            newScore = scoreHand(hand.replace("J", joker))
            if newScore > score:
                score = newScore
    return(score)

    

def compareEachCard(hand1, hand2):
    for c1, c2 in zip(hand1, hand2):
        # check type?
        if c1 == c2:
            pass
        else:
            return(CARDRANK[c1] > CARDRANK[c2])


def compareHands(hand1, hand2):
    score1 = scoreHand(hand1)
    score2 = scoreHand(hand2)

    if score1 == score2:
        return (compareEachCard(hand1, hand2))
    else:
        return (score1>score2)

    
def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input", type=str, default="no file")
    
    args = parser.parse_args()
    input=args.input

    # create necessary sort trees
    # or a list of lists 
    list7 = []
    list6 = []
    list5 = []
    list4 = []
    list3 = []
    list2 = []
    list1 = []
    list27 = []
    list26 = []
    list25 = []
    list24 = []
    list23 = []
    list22 = []
    list21 = []
    
    # totList = [list7, list6, list5, list4, list3, list2, list1]
    totList = [list1, list2, list3, list4, list5, list6, list7]
    totList2 = [list21, list22, list23, list24, list25, list26, list27]
    with open(input) as file:
        lines = file.readlines()
        for line in lines:
            hand = Hand(line.split()[0], eval(line.split()[1]))
            # print(f"{hand.hand}, {hand.bid}, {hand.binScore}, {hand.handVal}")
            match hand.binScore:
                case 7:
                    list7.append(hand)
                case 6:
                    list6.append(hand)
                case 5:
                    list5.append(hand)
                case 4:
                    list4.append(hand)
                case 3:
                    list3.append(hand)
                case 2:
                    list2.append(hand)
                case 1:
                    list1.append(hand)
            match hand.binScore2:
                case 7:
                    list27.append(hand)
                case 6:
                    list26.append(hand)
                case 5:
                    list25.append(hand)
                case 4:
                    list24.append(hand)
                case 3:
                    list23.append(hand)
                case 2:
                    list22.append(hand)
                case 1:
                    list21.append(hand)

        
    total = 0
    page = 1
    for list in totList:
        list.sort(key=lambda x: x.handVal)
        for i, element in enumerate(list):
            # print(element.hand)
            total += (i+page) * element.bid
        page += len(list)
    print(total)

        
    total = 0
    page = 1
    for list in totList2:
        list.sort(key=lambda x: x.handVal2)
        for i, element in enumerate(list):
            # print(element.hand)
            total += (i+page) * element.bid
        page += len(list)
    print(total)

if __name__ == '__main__':
    sys.exit(main())



