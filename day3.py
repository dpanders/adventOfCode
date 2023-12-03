import sys
import argparse
import array



def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input", type=str, default="no file")
    
    args = parser.parse_args()
    input=args.input

    fileArray = []
    with open(input) as file:
        for lines in file.readlines():
            nextRow = []
            for line in lines:
                for char in line:
                    if char != '\n':
                        nextRow.append(char)
                    
            # add each char to array column
            fileArray.append(nextRow)
    for rows in fileArray:
        print (rows)
#    print(fileArray)

    print(fileArray[0][0])
    print(fileArray[0][1])
    print(fileArray[0][2])
    
    
    # perform analysis:



if __name__ == '__main__':
    sys.exit(main())
