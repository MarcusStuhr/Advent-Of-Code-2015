import sys


PUZZLE_DATA_FILENAME = "day03_input.txt"


def houses_visited(instructions):
    """
    Inputs:
    A string of instructions containing characters from {'<','V','>','^'}, representing directions
    
    Outputs:
    A set of two-element tuples representing the coordinates of which houses were visited.
    
    Assumptions:
    Traversal begins at point (0,0)
    (0,0) is counted as being visited by default.
    """
    houses = set([(0,0)])
    cur_x = 0
    cur_y = 0
    for instruction in instructions:
        if   instruction == '<': cur_x-=1
        elif instruction == '>': cur_x+=1
        elif instruction == 'v': cur_y-=1
        elif instruction == '^': cur_y+=1
        houses.add((cur_x,cur_y))
    return houses


def num_houses_visited(*instructions_args):
    """
    Inputs:
    A tuple of instruction strings. Each string contains characters from {'<','V','>','^'}, representing directions
    
    Outputs:
    The number of houses visited (collectively) across all instruction strings -- the length of a 
    master set formed after unioning together the results from houses_visited() for each instruction string
    """
    master_set = set()
    for instructions in instructions_args:
        master_set |= houses_visited(instructions)
    return len(master_set)


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

    num_houses_visted_part_1 = num_houses_visited(instructions)
    
    santas_instructions = instructions[0::2] #every other instruction, from index 0
    robo_santas_instructions = instructions[1::2] #every other instruction, from index 1
    num_houses_visited_part_2 = num_houses_visited(santas_instructions, robo_santas_instructions)
    
    print "Answer to part 1: {}".format(num_houses_visted_part_1)
    print "Answer to part 2: {}".format(num_houses_visited_part_2)

 
if __name__ == "__main__":
    main()
