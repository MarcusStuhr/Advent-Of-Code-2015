import sys


PUZZLE_DATA_FILENAME = "day02_input.txt"


def wrapping_paper_needed(l,w,h):
    """
    Given gift dimensions l,w,h, determine how many sq. feet
    of wrapping paper is required.
    Answer is total surface area plus the area of the smallest side.
    """
    return 2*(l*w + l*h + w*h) + min(l*w, l*h, w*h)


def ribbon_length_needed(l,w,h):
    """
    Given gift dimensions l,w,h, determine how many feet of
    ribbon is required.
    Answer is 2*(sum of smallest 2 lengths) + l*w*h.
    The left part is equivalent to:
    2*(sum of all 3 lengths) - 2*(max of the 3 lengths)
    """
    return 2*(l + w + h) - 2*max(l, w, h) + l*w*h


def get_file_input(filename):
    try:
        with open(filename) as f:
            data = f.read()
        return data
    except IOError:
       print "Unable to open/read input file {}".format(filename)
       sys.exit(1)


def main():
    file_contents_string = get_file_input(PUZZLE_DATA_FILENAME)
    gift_dimensions_list = [map(int,line.split('x')) for line in file_contents_string.split('\n')]

    sum_sqft_wrapping_paper = 0
    sum_ribbon_length = 0
    
    for l,w,h in gift_dimensions_list:
        sum_sqft_wrapping_paper += wrapping_paper_needed(l,w,h)
        sum_ribbon_length += ribbon_length_needed(l,w,h)
        
    print "Answer to part 1: {}".format(sum_sqft_wrapping_paper)
    print "Answer to part 2: {}".format(sum_ribbon_length)

 
if __name__ == "__main__":
    main()