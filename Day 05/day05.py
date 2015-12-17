import re


PUZZLE_DATA_FILENAME = "day05_input.txt"


def is_nice_part_1(s):
    """
    Returns True if string s is a nice string using criteria from part 1.
    Returns False otherwise.
    Uses a three-part regex:
    1. s does not contain "ab", "cd", "pq", or "xy"
    2. s has at least three vowels
    3. s contains a duplicated-letter pair
    """
    return all([(not re.search(r"(ab|cd|pq|xy)", s)),  len(re.findall(r"[aeiou]", s)) >= 3, re.search(r"(.)\1", s)])


def is_nice_part_2(s):
    """
    Returns True if string s is a nice string using criteria from part 2.
    Returns False otherwise.
    Uses a two-part regex:
    1. s contains a letter triplet where the first and third characters match. Second char can be anything.
    2. s contains at least two identical, non-overlapping letter pairs
    """
    return all([re.search(r"(.).\1", s), re.search(r"(..).*\1", s)])


def count_nice_strings_part_1(strings):
    """
    Sums up the count of strings that fulfill the nice-string criteria from part 1
    """
    return sum(is_nice_part_1(s) for s in strings)


def count_nice_strings_part_2(strings):
    """
    Sums up the count of strings that fulfill the nice-string criteria from part 2
    """
    return sum(is_nice_part_2(s) for s in strings) 


def main():
    file_contents_string = open(PUZZLE_DATA_FILENAME).read()
    strings = file_contents_string.split('\n')

    print "Answer to part 1: {}".format(count_nice_strings_part_1(strings))
    print "Answer to part 2: {}".format(count_nice_strings_part_2(strings))

 
if __name__ == "__main__":
    main()