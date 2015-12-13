import sys
from collections import defaultdict

PUZZLE_DATA_FILENAME = "day09_input.txt"

cache = {}

def hamiltonian_min_and_max_cost(dist_graph, city_names, from_city, visited, sentinel):
    """
    dist_graph: A cost dictionary. dist_graph[A][B] is the cost of going from city A to city B.
    city_names: A list of the city names
    from_city: The name of the city we are about to leave
    visited: A bitmask representing which cities we've already visited (mapping to city_names)
    sentinel: abs of this number is greater than any path cost, computed from abs(sum of all costs) + 1

    This function returns the min and max cost of the Hamiltonian path starting at from_city, without
    visiting any cities already denoted in the visited bitmask.

    Time complexity O(n^2 * 2^n) where n is the number of cities
    """
    
    if visited == (1<<len(city_names))-1: #if all cities have been visited, we stop
        return 0,0
    
    memo_key = (from_city, visited)
    if memo_key in cache: #if we've encountered this position before, return the work we've already done
        return cache[memo_key] 
    
    min_cost = abs(sentinel)
    max_cost = -abs(sentinel)
    
    for index,to_city in enumerate(city_names):
        if visited & (1<<index) == 0 and to_city in dist_graph[from_city]:
            min_cost_next, max_cost_next = hamiltonian_min_and_max_cost(dist_graph, city_names, to_city, visited | (1<<index), sentinel)
            min_cost = min(min_cost, dist_graph[from_city][to_city] + min_cost_next)
            max_cost = max(max_cost, dist_graph[from_city][to_city] + max_cost_next)
            
    cache[memo_key] = (min_cost, max_cost)
    return min_cost, max_cost


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
    lines = file_contents_string.split('\n')

    dist_graph = defaultdict(dict)
    sum_costs = 0
    
    for line in lines:
        words = line.strip().split(" ")
        from_city,to_city,dist = words[0],words[2],int(words[-1])
        dist_graph[from_city][to_city] = dist
        dist_graph[to_city][from_city] = dist
        sum_costs += abs(dist)

    min_cost = abs(sum_costs)+1 #bigger than any path cost
    max_cost = -(abs(sum_costs)+1) #smaller than any path cost
    city_names = list(dist_graph.keys())
    
    for index, to_city in enumerate(city_names):
        min_cost_next, max_cost_next = hamiltonian_min_and_max_cost(dist_graph, city_names, to_city, 1<<index, abs(sum_costs)+1)
        min_cost = min(min_cost, min_cost_next)
        max_cost = max(max_cost, max_cost_next)
     
    print "Answer to part 1: {}".format(min_cost)
    print "Answer to part 2: {}".format(max_cost)

 
if __name__ == "__main__":
    main()