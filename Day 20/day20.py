def find_house_number(target, multiplier, present_lim = None):
    lim = target/multiplier
    presents = [multiplier]*(lim+1)
    for i in xrange(2,lim+1):
        bound = min(lim, i*present_lim) if present_lim else lim
        for j in xrange(i,bound+1,i):
            presents[j]+=multiplier*i
    for i in xrange(1,lim+1):
        if presents[i] >= target:
            return i
    return -1

def main():
    target = 36000000
    print "Answer to part 1: {}".format(find_house_number(target,10))
    print "Answer to part 2: {}".format(find_house_number(target,11,50))

if __name__ == "__main__":
    main()