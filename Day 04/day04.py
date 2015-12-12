import sys
from hashlib import md5
from itertools import count


PUZZLE_DATA_FILENAME = "day04_input.txt"


def make_MD5_hash(secret_key, prefix, start_num = 1):
    """
    Finds the smallest number >= start_num such that md5(secret_key + str(number)) begins with
    the given prefix string.
    """
    for num in count(start_num):
        md5_string = md5(secret_key + str(num)).hexdigest()
        if md5_string.startswith(prefix):
            return num


def get_file_input(filename):
    try:
        with open(filename) as f:
            data = f.read()
        return data
    except IOError:
       print "Unable to open/read input file {}".format(filename)
       sys.exit(1)


def main():
    secret_key = get_file_input(PUZZLE_DATA_FILENAME)

    print "Answer to part 1: {}".format(make_MD5_hash(secret_key, "00000"))
    print "Answer to part 2: {}".format(make_MD5_hash(secret_key, "000000"))

 
if __name__ == "__main__":
    main()