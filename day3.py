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

    with open(input) as file:
        for line in file.readlines():
    
    # perform analysis:



if __name__ == '__main__':
    sys.exit(main())
