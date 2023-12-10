import sys
import argparse
import re

class Map:
    def __init__(self, name):
        self.name = name
        self.input = []
        self.out = []
        self.range = []
        self.inUpper = []
        self.shift = []
    def addRange(self, input, out, range):
        self.input.append(int(input))
        self.out.append(int(out))
        self.range.append(int(range))
        self.inUpper.append(int(input)+int(range))
        self.shift.append(int(out)-int(input))
    def map2(self, input):
        input = int(input)
        output = input
        for lower, upper, shift in zip(self.input, self.inUpper, self.shift):
            if input >= lower and input <= upper:
                output = input + shift
                break
        return (output)
    

    
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
        seeds = [i for i in line.split(":")[1].split()]
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
                map.addRange(path[1], path[0], path[2])
            elif inMap:
                MapList.append(map)
                inMap = False
        if inMap:
            MapList.append(map)
    
    locationList = []
    for seed in seeds:
        output = seed
        for map in MapList:
            output = map.map2(output)
        locationList.append((seed,output))

    lowestLocation = locationList[0][1]
    lowestSeed = 0
    for seed, location in locationList:
        if location < lowestLocation:
            lowestLocation = location
            lowestSeed = seed
    
    # part 1
    print(lowestSeed, lowestLocation)

    # part 
    part2Seeds = []
    pair = True
    print(seeds)
    print("part2")
    for x, y in zip(seeds, seeds[1:]):
        # print("*")
        if pair:
            print(range(int(y)))
            for i in range(int(y)):
                # print("@")
                part2Seeds.append(int(x)+i)
            pair = False
        else: 
            pair = True
    print('part2 search')
    locationList = []
    for seed in part2Seeds:
        # print("*",end="")
        output = seed
        for map in MapList:
            output = map.map2(output)
        locationList.append((seed,output))

    lowestLocation = locationList[0][1]
    lowestSeed = 0
    print("part2 location search")
    for seed, location in locationList:
        if location < lowestLocation:
            lowestLocation = location
            lowestSeed = seed
    
    print(lowestSeed, lowestLocation)


if __name__ == '__main__':
    sys.exit(main())



