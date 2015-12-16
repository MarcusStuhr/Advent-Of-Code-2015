import re

PUZZLE_DATA_FILENAME = "day16_input.txt"


SUE_STATS = {"children": 3,
             "cats": 7,
             "samoyeds": 2,
             "pomeranians": 3,
             "akitas": 0,
             "vizslas": 0,
             "goldfish": 5,
             "trees": 3,
             "cars": 2,
             "perfumes": 1}


def is_sue(sue_stats, compounds, amts, overrides_gt, overrides_lt):
    for i in xrange(len(compounds)):
        if compounds[i] in overrides_gt:
            if sue_stats[compounds[i]] >= amts[i]:
                return False
        elif compounds[i] in overrides_lt:
            if sue_stats[compounds[i]] <= amts[i]:
                return False
        else:
            if sue_stats[compounds[i]] != amts[i]:
                return False
    return True
    

def find_sue(lines, sue_stats, overrides_gt = [], overrides_lt = []):
    for line in lines:
        match = re.match(r"Sue ([\d]+): ([\w]+): ([\d]+), ([\w]+): ([\d]+), ([\w]+): ([\d]+)", line)
        groups = match.groups()
        sue, compounds, amts = int(groups[0]), groups[1::2], map(int,groups[2::2])
        if is_sue(sue_stats, compounds, amts, overrides_gt, overrides_lt):
            return int(sue)
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
    lines = get_file_input(PUZZLE_DATA_FILENAME).split("\n")
    print "Answer to part 1: {}".format(find_sue(lines, SUE_STATS))
    print "Answer to part 2: {}".format(find_sue(lines, SUE_STATS, ("cats","trees"),("pomeranians","goldfish")))


if __name__ == "__main__":
    main()