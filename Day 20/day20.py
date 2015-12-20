def find_house_number(target, multiplier, present_lim = None):
    lim = target/10
    divs = [0]*(lim+1)
    for a in xrange(1,lim+1):
        bound = min(lim, a + (present_lim-1)*a) if present_lim else lim
        for j in xrange(a,bound+1,a):
            divs[j]+=multiplier*a
    for i in xrange(lim+1):
        if divs[i] >= target:
            return i
    return -1

def main():
    target = 36000000
    print "Answer to part 1: {}".format(find_house_number(target,10))
    print "Answer to part 2: {}".format(find_house_number(target,11,50))


if __name__ == "__main__":
    main()