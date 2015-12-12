import sys
import re


PUZZLE_DATA_FILENAME = "day06_input.txt"
SIZE_MATRIX = 1000
MODIFICATION_RULES = {}

#modification rules for part 1
MODIFICATION_RULES[1]= {"turn on": lambda k: 1,
                        "turn off": lambda k: 0,
                        "toggle": lambda k: 1-k}

#modification rules for part 2
MODIFICATION_RULES[2]= {"turn on": lambda k: k+1,
                        "turn off": lambda k: max(0,k-1),
                        "toggle": lambda k: k+2}


def modify_lights(M, r1, c1, r2, c2, command, modification_rules):
    """
    Given a matrix M, coordinates for upper left cell (r1,c1), coordinates for
    lower right cell (r2,c2), a command, and a set of rules that map the command
    to lambda-function modifications, modify the lights within the bound range
    with the given command. 
    """
    for r in xrange(r1, r2+1):
        for c in xrange(c1, c2+1):
            M[r][c] = modification_rules[command](M[r][c])
            

def count_lights_on(commands, rule_index, size_matrix = SIZE_MATRIX):
    """
    Sums up the values of the cells of matrix M after performing all the commands found
    in the commands list. The rule index determines which set of rules to use.
    """
    M = [[0 for i in xrange(size_matrix)] for j in xrange(size_matrix)]

    for command in commands:
        try:
            match = re.match(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)", command)
            params = match.groups()
            command = params[0]
            r1, c1, r2, c2 = map(int,params[1:])
            modify_lights(M, r1, c1, r2, c2, command, MODIFICATION_RULES[rule_index])
        except:
            raise Exception("Invalid input format for line: {}".format(command))
            
    return sum(M[r][c] for r in xrange(size_matrix) for c in xrange(size_matrix))


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
    commands = file_contents_string.split('\n')

    print "Answer to part 1: {}".format(count_lights_on(commands,1))
    print "Answer to part 2: {}".format(count_lights_on(commands,2))

 
if __name__ == "__main__":
    main()