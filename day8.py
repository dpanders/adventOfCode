import sys
import argparse
import re


class Node:
    def __init__(self, curNode):
        self.curNode = curNode
        self.stepCnt = 0
    def updateNode(self, node):
        self.curNode = node
    def lastLetterZ(self):
        return(self.curNode[2] == 'Z')


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input", type=str, default="no file")
    
    args = parser.parse_args()
    input=args.input

    nodes = {}
    with open(input) as file:
        steps = file.readline()

        for line in file.readlines():
            matches = re.findall(r'([0-9A-Z]{3})', line)
            if matches:
                nodes[matches[0]] = {'L':matches[1], 'R':matches[2]}
    steps = steps.replace('\n', '')

    # part 1
    if False:
        curNode = 'AAA'
        i = 0
        stepCnt = 0
        while curNode != 'ZZZ':
            curNode = nodes[curNode][steps[i%len(steps)]]
            i+=1
            stepCnt += 1
        
        print(stepCnt)

    # part 2
    curNodes = []
    for key in nodes:
        if key[2] == 'A':
            newNode = Node(key)
            curNodes.append(newNode)
    
    for curNode in curNodes:
        i = 0
        while not curNode.lastLetterZ():
            curNode.updateNode(nodes[curNode.curNode][steps[i%len(steps)]])
            curNode.stepCnt += 1
            i += 1


    from math import lcm
    print(lcm(curNodes[0].stepCnt, curNodes[1].stepCnt, curNodes[2].stepCnt, curNodes[3].stepCnt, curNodes[4].stepCnt, curNodes[5].stepCnt ))


if __name__ == '__main__':
    sys.exit(main())


