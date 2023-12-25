import sys
import argparse
import re

EXAMPLE = [(7, 9), (15, 40), (30, 200)]
INPUT = [(50, 242),  (74,1017), (86,1691), (85,1252)]

PART2= [{71530, 940200}]

    
def main(argv=None):

    total = 1
    for time, distance in PART2:
        roundTot = 0
        for i in range(time):
            d = (time - i) * i
            if d > distance:
                roundTot+=1
        total *= roundTot
        print(roundTot)
    print(total)


if __name__ == '__main__':
    sys.exit(main())



