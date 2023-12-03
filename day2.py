import sys
import argparse
import re


numbersAsWords=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbersAsWordsBackwards=["orez", "eno","owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]

def getFirstNumber(line):
    # go through the line and look for a number, store the location
    # and store the value for later?
    
    firstNumber = None
    firstPosition = None
    for index in range(len(numbersAsWords)):
        num = numbersAsWords[index]
        pos = line.find(num)
        if pos != -1:
            if firstPosition is None:
                firstPosition = pos
                firstNumber = index
            else:
                if firstPosition > pos:
                    firstPosition = pos
                    firstNumber = index
    

    m = re.search(r'[0-9]', line)
    number = None
    position = None
    if m:
        number = int(m.group(0))
        position = m.start()

    if position is not None and firstPosition is not None:    
        if position < firstPosition:
            return (number)
        else:
            return (firstNumber)
    elif position is not None:
        return(number)
    elif firstPosition is not None:
        return(firstNumber)
    else:
        return(None)
    
    # go through the line and look for a number as a word, store the location 
    # and store the value for later
    
    # compare, if the lower one is a number, return the string to char, if it is
    # a number as a word, use the value stored from the if
    
def getSecondNumber(line):
    # go through the line and look for a number, store the location
    # and store the value for later?
    line = line[::-1]

    firstNumber = None
    firstPosition = None
    for index in range(len(numbersAsWordsBackwards)):
        num = numbersAsWordsBackwards[index]
        pos = line.find(num)
        if pos != -1:
            if firstPosition is None:
                firstPosition = pos
                firstNumber = index
            else:
                if firstPosition > pos:
                    firstPosition = pos
                    firstNumber = index
    
    m = re.search(r'[0-9]', line)
    number = None
    position = None
    if m:
        number = int(m.group(0))
        position = m.start()

    if position is not None and firstPosition is not None:    
        if position < firstPosition:
            return (number)
        else:
            return (firstNumber)
    elif position is not None:
        return(number)
    elif firstPosition is not None:
        return(firstNumber)
    else:
        return(None)
    
    # go through the line and look for a number as a word, store the location 
    # and store the value for later
    
    # compare, if the lower one is a number, return the string to char, if it is
    # a number as a word, use the value stored from the if
    
    

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
            # print(type(firstChar))
            # print(type(secondChar))
            total+=firstChar*10+secondChar

            # print (str(firstChar) + " " +str(secondChar)+" : "+ line)
            
    
    print(total)






if __name__ == '__main__':
    sys.exit(main())
