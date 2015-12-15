import sys
import re


PUZZLE_DATA_FILENAME = "day08_input.txt"


def get_file_input(filename):
    try:
        with open(filename) as f:
            data = f.read()
        return data
    except IOError:
        print "Unable to open/read input file {}".format(filename)
        sys.exit(1)


def main():
    file_contents_string = get_file_input(PUZZLE_DATA_FILENAME)
    strings = file_contents_string.split('\n')
    ans_part_1 = 0
    ans_part_2 = 0
    
    for s in strings:
        ans_part_1 += len(s) - len(eval(s))
        ans_part_2 += len(re.escape(s)) + 2 - len(s)
        
    print "Answer to part 1: {}".format(ans_part_1)
    print "Answer to part 2: {}".format(ans_part_2)

 
if __name__ == "__main__":
    main()
