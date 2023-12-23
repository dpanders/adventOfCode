import sys
import argparse
import re

class Range:
    def __init__(self, destStart, sourceStart, range):
        self.destStart=destStart
        self.sourceStart=sourceStart
        self.range=range
    def inRange(self, source):
        return(source>=self.sourceStart and source<self.sourceStart+self.range)
    def translate(self, source):
        return(source-self.sourceStart+self.destStart)


class Map:
    def __init__(self, name):
        self.name = name
        self.ranges = []
    def addRange(self, destStart, sourceStart, range):
        newRange = Range(destStart, sourceStart, range)
        self.ranges.append(newRange)
    def map2(self, input):
        for range in self.ranges:
            if range.inRange(input):
                # print("in range!!")
                return(range.translate(input))
        return(input)



    
def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input", type=str, default="no file")
    
    args = parser.parse_args()
    input=args.input
    
    seeds = []
    MapList = []
    with open(input) as file:
        line = file.readline()
        seeds = [eval(i) for i in line.split(":")[1].split()]
        lines = file.readlines()
        inMap = False
        for line in lines:
            if "map" in line:
                map = Map(line.split()[0])
                inMap = True
                # start a new map?
            elif len(line) >1:
                # add route
                path = line.split()
                map.addRange(int(path[0]), int(path[1]), int(path[2]))
            elif inMap:
                MapList.append(map)
                inMap = False
        if inMap:
            MapList.append(map)
    
    #part 1
    location = 0
    seed = 0
    first = True
    # for map in MapList:
        # for range in map.ranges:
            # print(f"{range.destStart}, {range.sourceStart}, {range.range}")

    for seed in seeds:
        # print(f"seed: {seed} ", end="")
        input=seed
        for map in MapList:
            output = map.map2(input)
            input=output
            # print(f"{map.name} {output}, ", end="")
        # print(f"location {output}")
        if first:
            location=output
            first = False
        else:
            if output<location:
                location=output
    
    print (location)
    
    
    #part 2
    location = 0
    seed = 0
    first = True
    # for map in MapList:
        # for range in map.ranges:
            # print(f"{range.destStart}, {range.sourceStart}, {range.range}")

    rangeSeeds = zip(seeds[:len(seeds):2], seeds[1::2])
    print(f"processing {len(seeds)/2} ranges")
    for start, end in rangeSeeds:
        # print(f"seeds: {start} {start+end}")
        print("*",end="")
        for i in range(start, start+end):
            input=i
            for map in MapList:
                output = map.map2(input)
                input=output
                # print(f"{map.name} {output}, ", end="")
            # print(f"location {output}")
            if first:
                location=output
                first = False
            else:
                if output<location:
                    location=output
    print()
    print (location)



if __name__ == '__main__':
    sys.exit(main())



