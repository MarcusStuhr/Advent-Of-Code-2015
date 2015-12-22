from collections import defaultdict
from random import shuffle
import re

PUZZLE_DATA_FILENAME = "day19_input.txt"

def count_distinct_molecules(transitions, medicine_molecule):
    distinct_molecules = set()
    for before, after in transitions:
        for i in xrange(len(medicine_molecule)):
            if medicine_molecule[i:i+len(before)] == before:
                new_molecule = medicine_molecule[:i] + after + medicine_molecule[i+len(before):]
                distinct_molecules.add(new_molecule)
    return len(distinct_molecules)

def count_steps(medicine_molecule):
    s = medicine_molecule
    return len(re.findall(r"[A-Z][a-z]?",s)) - 2*s.count("Rn") - 2*s.count("Y") - 1

def main():
    lines = [line.split(" ") for line in open(PUZZLE_DATA_FILENAME).read().split("\n")]
    transitions = []
    for before, arrow, after in lines[:-2]:
        transitions.append((before,after))
    medicine_molecule = lines[-1][0]
    print "Answer to part 1: {}".format(count_distinct_molecules(transitions, medicine_molecule))
    print "Answer to part 2: {}".format(count_steps(medicine_molecule))


if __name__ == "__main__":
    main()
