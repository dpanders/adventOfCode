import sys
import argparse
import re

SIMPLE_INPUT = "seeds: 79 14 55 13\
seed-to-soil map:\
50 98 2\
52 50 48\
\
soil-to-fertilizer map:\
0 15 37\
37 52 2\
39 0 15\
\
fertilizer-to-water map:\
49 53 8\
0 11 42\
42 0 7\
57 7 4\
\
water-to-light map:\
88 18 7\
18 25 70\
\
light-to-temperature map:\
45 77 23\
81 45 19\
68 64 13\
\
temperature-to-humidity map:\
0 69 1\
1 0 69\
\
humidity-to-location map:\
60 56 37\
56 93 4"

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
        
    '''
    
seed-to-soil map:
50 98 2
52 50 48
'''
    def map2reverse(self, output):
        output = int(output)
        input = output
        print(f"map2reverse with: {output}")
        for lower, upper, shift in zip(reversed(self.input), reversed(self.inUpper), reversed(self.shift)):
            print(lower, upper, shift)
            if output >= lower + shift and output <= upper + shift:
                input = output - shift
        print(f"input: {input}")
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
    
    #part 1
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

    print(lowestSeed, lowestLocation)

    # part 1b) reverse map
    # get seeds as ints so it's easier later
    seeds = [eval(i) for i in seeds]
    
    breakBool = False
    lowest = max(seeds)
    for i in range(max(seeds)):
        for map in reversed(MapList):
            input = map.map2reverse(i)
            if input in seeds:
                breakBool = True
                lowest = input
                break
        if breakBool:
            break
    
    print(lowest)

    if False:
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


if __name__ == '__main__':
    sys.exit(main())



