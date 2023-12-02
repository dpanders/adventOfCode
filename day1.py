import sys
import argparse
import re


numbersAsWords=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def getFirstNumber(line):
    # go through the line and look for a number, store the location
    # and store the value for later?
    m=re.search(r'[0-9]', line2)
    num=line.find(
    
    # go through the line and look for a number as a word, store the location 
    # and store the value for later
    
    # compare, if the lower one is a number, return the string to char, if it is
    # a number as a word, use the value stored from the if
    return(value)
    
    

def getSecondNumber(line):    
    line2=line[len(line)::-1]

def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input", type=str, default="no file")
    
    args = parser.parse_args()
    input=args.input
    
    total = 0
    with open(input) as file:
        for line in file.readlines():
            firstChar=getFirstNumber(line)
            secondChar=getSecondNumber(line)
            #print(firstChar,secondChar)
            total+=int(firstChar+secondChar)
            
    
    print(total)






if __name__ == '__main__':
    sys.exit(main())
