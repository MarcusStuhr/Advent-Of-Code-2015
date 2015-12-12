import sys


PUZZLE_DATA_FILENAME = "day03_input.txt"


def houses_visited(instructions):
    """
    Returns a set of (unique) houses visited, given a string of instructions.
    The origin point (0,0) is included by default.
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


def num_houses_visited(*args):
    """
    Given a tuple of instruction strings, this loops over each string,
    computes houses_visited() to get the set of houses visited,
    and then unions all these results together to get the houses visited
    across all independent trips.
    The length of this master set is then returned.
    """
    master_set = set()
    for instructions in args:
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