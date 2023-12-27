import sys
import argparse
import re

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
            matches = re.findall(r'([A-Z]{3})', line)
            if matches:
                nodes[matches[0]] = {'L':matches[1], 'R':matches[2]}
    steps = steps.replace('\n', '')
    curNode = 'AAA'
    i = 0
    stepCnt = 0
    while curNode != 'ZZZ':
        curNode = nodes[curNode][steps[i%len(steps)]]
        i+=1
        stepCnt += 1
    
    print(stepCnt)

if __name__ == '__main__':
    sys.exit(main())



