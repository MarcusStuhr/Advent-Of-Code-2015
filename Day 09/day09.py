import sys
from collections import defaultdict


PUZZLE_DATA_FILENAME = "day09_input.txt"

memo_cache = {}


def hamiltonian_path_cost(costs_graph, from_node, already_visited):
    if already_visited == (1<<len(costs_graph.keys()))-1: #if all nodes have been visited, we stop
        return True, 0, 0

    memo_key = (from_node, already_visited)
    if memo_key in memo_cache: #if we've encountered this position before, return the work we've already done
        return memo_cache[memo_key]

    min_cost = 10**10
    max_cost = -10**10
    is_valid = False

    for index, to_node in enumerate(costs_graph.keys()):
        if already_visited & (1<<index) == 0 and to_node in costs_graph[from_node]:
            is_valid, min_cost_next, max_cost_next = hamiltonian_path_cost(costs_graph, to_node, already_visited | (1<<index))
            if is_valid:
                min_cost = min(min_cost, costs_graph[from_node][to_node] + min_cost_next)
                max_cost = max(max_cost, costs_graph[from_node][to_node] + max_cost_next)

    memo_cache[memo_key] = (is_valid, min_cost, max_cost)
    return is_valid, min_cost, max_cost


def find_hamiltonian_min_max_costs(costs_graph):
    min_cost = 10**10
    max_cost = -10**10
    is_valid = False

    for index, to_node in enumerate(costs_graph.keys()):
        is_valid, min_cost_next, max_cost_next = hamiltonian_path_cost(costs_graph, to_node, 1<<index)
        if is_valid:
            min_cost = min(min_cost, min_cost_next)
            max_cost = max(max_cost, max_cost_next)
    return is_valid, min_cost, max_cost


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

    for line in lines:
        words = line.strip().split(" ")
        from_city,to_city,dist = words[0],words[2],int(words[-1])
        dist_graph[from_city][to_city] = dist
        dist_graph[to_city][from_city] = dist

    is_valid, min_cost, max_cost = find_hamiltonian_min_max_costs(dist_graph)

    print "Answer to part 1: {}".format(min_cost)
    print "Answer to part 2: {}".format(max_cost)


if __name__ == "__main__":
    main()
