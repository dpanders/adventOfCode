import sys
import argparse
import re

def diffList(inputList):
    diffList = []
    i = 0
    while i < len(inputList)-1:
        diffList.append(inputList[i+1]-inputList[i])
        i += 1
    return(diffList)

class Sequence:
    def __init__ (self, inputList):
        self.seq = inputList
        if len(inputList) > 1:
            # print(diffList(inputList))
            self.nextNode = Sequence(diffList(inputList))
        else:
            self.nextNode = None
    def zeroList(self):
        zero = True
        for i in self.seq:
            zero = zero and (i == 0)
        return (zero)
    def nextVal(self):
        if self.nextNode is not None:
            return(self.seq[-1] + self.nextNode.nextVal())
        else:
            return(self.seq[-1])


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input", type=str, default="no file")
    
    args = parser.parse_args()
    input=args.input

    sequences = []
    with open(input) as file:
        for line in file.readlines():
            numbers = line.split()
            sequences.append([eval(i) for i in numbers])
    
    # part 1
    sum = 0
    for seq in sequences:
        # print(seq)
        seqNode = Sequence(seq)
        # print(seqNode.nextVal())
        sum += seqNode.nextVal()

    print(sum) 




if __name__ == '__main__':
    sys.exit(main())


