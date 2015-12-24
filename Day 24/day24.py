from itertools import combinations
from operator import mul

PUZZLE_DATA_FILENAME = "day24_input.txt"

def get_ideal_QE(weights, target_weight, num_groups, find_smallest = True):
    minimal_QE = float('inf')
    if num_groups == 1:
        return float('inf') if sum(weights) != target_weight else reduce(mul,weights)
    
    for i in xrange(1, len(weights)+1):
        for c in combinations(weights, i):
            if sum(c) == target_weight:
                if get_ideal_QE(weights-set(c), target_weight, num_groups-1, False) != float('inf'):
                    minimal_QE = min(minimal_QE, reduce(mul,c))
                    if not find_smallest: return minimal_QE
        if find_smallest and minimal_QE != float('inf'): break
        
    return minimal_QE

def main():
    weights = set(map(int,open(PUZZLE_DATA_FILENAME).read().split("\n")))
    print "Answer to part 1: {}".format(get_ideal_QE(weights, sum(weights)/3, 3))
    print "Answer to part 2: {}".format(get_ideal_QE(weights, sum(weights)/4, 4))

if __name__ == "__main__":
    main()