import sys
from hashlib import md5
from itertools import count


def make_MD5_hash(secret_key, prefix, start_num = 1):
    """
    Inputs:
    secret_key, part of the string which we'd like to perform the hash function on
    prefix, a string that we'd like to be at the start of the hash
    start_num, an integer (defaulted to 1)
    
    Outputs:
    The smallest number >= start_num such that md5(secret_key + str(number)) begins with
    the given prefix string.
    """
    for num in count(start_num):
        md5_string = md5(secret_key + str(num)).hexdigest()
        if md5_string.startswith(prefix):
            return num


def main():
    secret_key = "bgvyzdsv"

    print "Answer to part 1: {}".format(make_MD5_hash(secret_key, "00000"))
    print "Answer to part 2: {}".format(make_MD5_hash(secret_key, "000000"))

 
if __name__ == "__main__":
    main()
