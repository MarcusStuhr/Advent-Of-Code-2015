import sys
from collections import defaultdict
from itertools import permutations
import re

PUZZLE_DATA_FILENAME = "day13_input.txt"

'''
Decided to try the permutation method for this one instead of using dynamic programming
'''


def optimal_happiness_gain(graph):
    best_delta = -10**10
    names = graph.keys()
    n = len(names)
    
    for perm in permutations(names):
        delta = sum(graph[perm[i]][perm[i+1]] + graph[perm[i+1]][perm[i]] for i in xrange(-1,n-1))
        best_delta = max(delta, best_delta)
    return best_delta


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
    lines = file_contents_string.split('\n')
    
    happiness_graph = defaultdict(dict)
    
    for line in lines:
        match = re.match(r"([\w]+) would (lose|gain) ([\d]+) happiness units by sitting next to ([\w]+).", line)
        if match:
            person_1, sign, change_amt_str, person_2 = match.groups()
            change_amt_int = int(change_amt_str) if sign == "gain" else -int(change_amt_str)
            happiness_graph[person_1][person_2] = change_amt_int
    
    ans_part_1 = optimal_happiness_gain(happiness_graph)

    for person in happiness_graph.keys():
        happiness_graph[person]["myself"] = 0
        happiness_graph["myself"][person] = 0

    ans_part_2 = optimal_happiness_gain(happiness_graph)
    
    print "Answer to part 1: {}".format(ans_part_1)
    print "Answer to part 2: {}".format(ans_part_2)


if __name__ == "__main__":
    main()