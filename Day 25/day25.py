import re

PUZZLE_DATA_FILENAME = "day25_input.txt"

def main():
    r,c = map(int,re.findall(r"([\d]+)", open(PUZZLE_DATA_FILENAME).read()))
    ans = (20151125 * pow(252533, ((r+c-2)*(r+c-1))/2 + c - 1, 33554393) ) % 33554393
    print "Answer to part 1: {}".format(ans)
    print "Answer to part 2: Collect the other 49 stars and click the link"
    
if __name__ == "__main__":
    main()

