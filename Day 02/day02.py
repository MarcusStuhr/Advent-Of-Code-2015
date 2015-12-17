PUZZLE_DATA_FILENAME = "day02_input.txt"


def wrapping_paper_needed(l,w,h):
    """
    Inputs:
    Three ints: the length, width, and height of the gift
    
    Outputs:
    An integer representing the amount of wrapping paper needed (in sqft) according to the problem criteria
    """
    return 2*(l*w + l*h + w*h) + min(l*w, l*h, w*h)


def ribbon_length_needed(l,w,h):
    """
    Inputs:
    Three ints: the length, width, and height of the gift
    
    Outputs:
    An integer representing the amount of ribbon needed (in ft) according to the problem criteria
    """
    return 2*(l + w + h) - 2*max(l, w, h) + l*w*h


def main():
    file_contents_string = open(PUZZLE_DATA_FILENAME).read()
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
