import sys
from collections import defaultdict

PUZZLE_DATA_FILENAME = "day09_input.txt"

memo_cache = {}

def hamiltonian_min_and_max_cost(costs_graph, node_names, from_node, already_visited):
    """
    Computes the min and max-cost Hamiltonian paths starting at from_node, without
    visiting any nodes encoded in the bitmask. This function is memoized on
    (from_node, already_visited) with an external dictionary called memo_cache.
    
    Inputs:
    costs_graph: A defaultdict of costs. costs_graph[A][B] is the cost of going from A to B directly
    node_names: A list of the node names, derived from the keys of costs_graph
    from_node: The name of the node we are about to leave
    already_visited: A bitmask representing which nodes we've already visited (mapping to node_names)

    Assumptions:
    -All costs in costs_graph are positive
    -The value 10**10 is larger than any path cost in the graph

    Returns:
    A tuple, (min_cost, max_cost)
    If no Hamiltonian path exists from (from_node, already_visited), then max_cost will be negative

    Time complexity:
    O(n^2 * 2^n), where n is the number of nodes
    """
    
    if already_visited == (1<<len(node_names))-1: #if all nodes have been visited, we stop
        return 0,0
    
    memo_key = (from_node, already_visited)
    if memo_key in memo_cache: #if we've encountered this position before, return the work we've already done
        return memo_cache[memo_key] 
    
    min_cost = 10**10
    max_cost = -10**10
    
    for index,to_node in enumerate(node_names):
        if already_visited & (1<<index) == 0 and to_node in costs_graph[from_node]:
            min_cost_next, max_cost_next = hamiltonian_min_and_max_cost(costs_graph, node_names, to_node, already_visited | (1<<index))
            min_cost = min(min_cost, costs_graph[from_node][to_node] + min_cost_next)
            max_cost = max(max_cost, costs_graph[from_node][to_node] + max_cost_next)
            
    memo_cache[memo_key] = (min_cost, max_cost)
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
        sum_costs += dist
        
    min_cost = 10**10
    max_cost = -10**10
    city_names = list(dist_graph.keys())
    
    for index, to_city in enumerate(city_names):
        min_cost_next, max_cost_next = hamiltonian_min_and_max_cost(dist_graph, city_names, to_city, 1<<index)
        min_cost = min(min_cost, min_cost_next)
        max_cost = max(max_cost, max_cost_next)
    
    print "Answer to part 1: {}".format(min_cost)
    print "Answer to part 2: {}".format(max_cost)


if __name__ == "__main__":
    main()