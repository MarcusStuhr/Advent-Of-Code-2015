import sys


PUZZLE_DATA_FILENAME = "day01_input.txt"


def final_floor(instructions):
    """
    Assumed starting position is floor 0.
    Finds the final floor by counting up the number of ups vs. downs.
    """
    return sum(1 if instruction=='(' else -1 for instruction in instructions)


def find_basement_index(instructions):
    """
    Assumed starting position is floor 0.
    Tracks the up/down movements to determine when floor -1 is reached.
    Returns 1-indexed answer.
    Returns -1 if floor -1 is never reached.
    """
    current_floor = 0
    
    for index,instruction in enumerate(instructions):
        if   instruction == '(':  current_floor +=1
        elif instruction == ')':  current_floor -=1
        
        if current_floor == -1: return index+1
        
    return -1


def get_file_input(filename):
    try:
        with open(filename) as f:
            data = f.read()
        return data
    except IOError:
       print "Unable to open/read input file {}".format(filename)
       sys.exit(1)


def main():
    instructions = get_file_input(PUZZLE_DATA_FILENAME)
    
    print "Answer to part 1: {}".format(final_floor(instructions))
    print "Answer to part 2: {}".format(find_basement_index(instructions))

 
if __name__ == "__main__":
    main()