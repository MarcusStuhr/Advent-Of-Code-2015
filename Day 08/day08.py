import re


PUZZLE_DATA_FILENAME = "day08_input.txt"


def main():
    file_contents_string = open(PUZZLE_DATA_FILENAME).read()
    strings = file_contents_string.split('\n')
    ans_part_1 = 0
    ans_part_2 = 0
    
    for s in strings:
        ans_part_1 += len(s) - len(eval(s))
        ans_part_2 += len(re.escape(s)) + 2 - len(s)
        
    print "Answer to part 1: {}".format(ans_part_1)
    print "Answer to part 2: {}".format(ans_part_2)

 
if __name__ == "__main__":
    main()