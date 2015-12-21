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

'''
def count_steps(transitions, medicine_molecule):
    phrase = medicine_molecule
    num_steps = 0
    while phrase != "e":
        pre_replacement_phrase = phrase
        for before, after in transitions:
            if after not in phrase: continue
            phrase = phrase.replace(after,before,1)
            num_steps+=1
        if phrase == pre_replacement_phrase: #no changes made, start over
            shuffle(transitions)
            return count_steps(transitions, medicine_molecule)
    return num_steps

def count_steps_min(transitions, medicine_molecule, num_trials = 20):
    return min(count_steps(transitions, medicine_molecule) for i in xrange(num_trials))
'''

def count_steps_fast(medicine_molecule):
    s = medicine_molecule
    return len(re.findall(r"[A-Z][a-z]?",s)) - 2*s.count("Rn") - 2*s.count("Y") - 1

def main():
    lines = [line.split(" ") for line in open(PUZZLE_DATA_FILENAME).read().split("\n")]
    transitions = []
    for before, arrow, after in lines[:-2]:
        transitions.append((before,after))
    medicine_molecule = lines[-1][0]
    print "Answer to part 1: {}".format(count_distinct_molecules(transitions, medicine_molecule))
    print "Answer to part 2: {}".format(count_steps_fast(medicine_molecule))


if __name__ == "__main__":
    main()
