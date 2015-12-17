from itertools import combinations


PUZZLE_DATA_FILENAME = "day17_input.txt"


def count_combinations(container_sizes, target_sum, find_minimal = False):
    ans = 0
    for k in xrange(1, len(container_sizes)+1):
        for c in combinations(container_sizes, k):
            if sum(c) == target_sum:
                ans+=1
        if find_minimal == True and ans:
            break
    return ans


def get_file_input(filename):
    try:
        with open(filename) as f:
            data = f.read()
        return data
    except IOError:
        print "Unable to open/read input file {}".format(filename)
        sys.exit(1)


def main():
    container_sizes = map(int,get_file_input(PUZZLE_DATA_FILENAME).split("\n"))
    print "Answer to part 1: {}".format(count_combinations(container_sizes, 150))
    print "Answer to part 2: {}".format(count_combinations(container_sizes, 150, True))


if __name__ == "__main__":
    main()