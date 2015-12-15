import sys
from itertools import groupby


def look_and_say(input_string, num_iterations):
    """
    Returns the string formed after applying the Look-And-Say algorithm on input_string (num_iterations times).
    """
    for i in xrange(num_iterations):
        input_string = ''.join([str(len(list(g))) + str(k) for k, g in groupby(input_string)])
    return input_string


def main():
    initial_string = "1113122113"
    print "Answer to part 1: {}".format(len(look_and_say(initial_string, 40)))
    print "Answer to part 2: {}".format(len(look_and_say(initial_string, 50)))

 
if __name__ == "__main__":
    main()
