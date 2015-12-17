from collections import defaultdict


PUZZLE_DATA_FILENAME = "day09_input.txt"
memo_cache = {}


def hamiltonian_path_cost(costs_graph, from_node, already_visited, first_node = None):
    """
    Finds the min/max cost Hamiltonian path in the graph, starting at from_node without visiting anything in
    the bitmask already_visited. If a circuit is required, then first_node will be visited at
    the end when there are no more nodes to visit.
    
    Inputs:
    costs_graph: A defaultdict of dicts containing edge costs between nodes, labeled with strings. 
        e.g. costs_graph["label1"]["label2"] -> 25
    from_node: The label of the node we are about to leave from
    already_visited: A bitmask representing the nodes we've already visited 
    first_node: The label of the very first node we visited (in the event we require a circuit)
    
    Outputs:
    A three-element tuple containing a boolean (determining whether a valid Hamiltonian path was found), 
    the min cost Hamiltonian path, and the max cost Hamiltonian path.
    
    Requirements:
    An external dictionary, memo_cache, for memoization purposes.
    """
    
    if already_visited == (1<<len(costs_graph.keys()))-1: #if all nodes have been visited, we stop
        if first_node == None:
            return True, 0, 0
        else:
            if first_node in costs_graph[from_node]:
                return True, costs_graph[from_node][first_node], costs_graph[from_node][first_node]
            return False, 0, 0

    memo_key = (from_node, already_visited, first_node)
    if memo_key in memo_cache: #if we've encountered this position before, return the work we've already done
        return memo_cache[memo_key]

    min_cost = float('inf')
    max_cost = -float('inf')
    is_valid = False

    for index, to_node in enumerate(costs_graph.keys()):
        if already_visited & (1<<index) == 0 and to_node in costs_graph[from_node]:
            is_valid, min_cost_next, max_cost_next = hamiltonian_path_cost(costs_graph, to_node, already_visited | (1<<index), first_node)
            if is_valid:
                min_cost = min(min_cost, costs_graph[from_node][to_node] + min_cost_next)
                max_cost = max(max_cost, costs_graph[from_node][to_node] + max_cost_next)

    memo_cache[memo_key] = (is_valid, min_cost, max_cost)
    return is_valid, min_cost, max_cost


def find_hamiltonian_min_max_costs(costs_graph, require_return_origin = False):
    """
    Finds the min/max cost Hamiltonian path (or circuit, depending) in the graph, with no particular
    preference for where it begins
    
    Inputs:
    costs_graph: A defaultdict of dicts containing edge costs between nodes, labeled with strings. 
        e.g. costs_graph["label1"]["label2"] -> 25
    require_return_origin: A boolean determining whether or not the Hamiltonian path must start and
    end at the same place (i.e. forming a circuit)
        
    Outputs:
    A three-element tuple containing a boolean (determining whether a valid Hamiltonian path was found), 
    the min cost Hamiltonian path, and the max cost Hamiltonian path.
        
    Requirements:
    An external dictionary, memo_cache, for memoization purposes.
    
    Time complexity:
    O(n^2 2^n)
    """
    
    min_cost = float('inf')
    max_cost = -float('inf')
    is_valid = False
    memo_cache.clear()

    for index, to_node in enumerate(costs_graph.keys()):
        if require_return_origin:
            is_valid, min_cost_next, max_cost_next = hamiltonian_path_cost(costs_graph, to_node, 1<<index, to_node)
        else:
            is_valid, min_cost_next, max_cost_next = hamiltonian_path_cost(costs_graph, to_node, 1<<index)
        if is_valid:
            min_cost = min(min_cost, min_cost_next)
            max_cost = max(max_cost, max_cost_next)
    return is_valid, min_cost, max_cost


def main():
    file_contents_string = open(PUZZLE_DATA_FILENAME).read()
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
