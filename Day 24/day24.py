from itertools import combinations
from operator import mul

PUZZLE_DATA_FILENAME = "day24_input.txt"

def get_ideal_QE(weights, num_groups): #assumes sum(weights) % num_groups == 0
    target_weight = sum(weights) / num_groups
    for i in xrange(1, len(weights)+1):
        for c in combinations(weights, i):
            if sum(c) == target_weight:
                return reduce(mul, c)

def main():
    weights = map(int,open(PUZZLE_DATA_FILENAME).read().split("\n"))
    print "Answer to part 1: {}".format(get_ideal_QE(weights,3))
    print "Answer to part 2: {}".format(get_ideal_QE(weights,4))

if __name__ == "__main__":
    main()