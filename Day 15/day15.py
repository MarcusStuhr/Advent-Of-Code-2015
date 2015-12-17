import re

PUZZLE_DATA_FILENAME = "day15_input.txt"
CALORIE_TARGET = 500
TEASPOON_TARGET = 100


def gen_tuple_dists(n, s): #tuples of len n, that sum to s
    if n == 1:
        yield (s,)
    else:
        for i in xrange(s + 1):
            for j in gen_tuple_dists(n - 1, s - i):
                yield (i,) + j


def get_max_cookie_score(ingredients, calorie_constraint = False):
    num_ingredients = len(ingredients)
    num_attribs = len(ingredients[0])-1
    max_score = 0
    for dist in gen_tuple_dists(num_ingredients, TEASPOON_TARGET):
        score = 1
        cals = 0
        for i in xrange(num_attribs):
            score *= max(0, sum(dist[j]*ingredients[j][i] for j in xrange(num_ingredients)))
        cals = sum(dist[j]*ingredients[j][-1] for j in xrange(num_ingredients))
        if not calorie_constraint or (calorie_constraint and cals==CALORIE_TARGET):
            max_score = max(score, max_score)
    return max_score


def main():
    lines = open(PUZZLE_DATA_FILENAME).read().split("\n")
    ingredients = [map(int,re.findall(r"[-]?[\d]+",line)) for line in lines]
    
    print "Answer to part 1: {}".format(get_max_cookie_score(ingredients))
    print "Answer to part 2: {}".format(get_max_cookie_score(ingredients,True))


if __name__ == "__main__":
    main()