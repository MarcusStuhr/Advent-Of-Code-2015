from itertools import combinations


PUZZLE_DATA_FILENAME = "day17_input.txt"


def count_combinations(container_sizes, target_sum):
    dp = [1] + [0]*(target_sum)
    for cur_num in container_sizes:
        for next_num in xrange(target_sum, cur_num-1, -1):
            dp[next_num] += dp[next_num - cur_num]
    return dp[target_sum]


def count_minimal_combinations(container_sizes, target_sum):
    ans = 0
    for k in xrange(1, len(container_sizes) + 1):
        for c in combinations(container_sizes, k):
            if sum(c) == target_sum:
                ans+=1
        if ans:
            break
    return ans


def main():
    container_sizes = map(int,open(PUZZLE_DATA_FILENAME).read().split("\n"))
    print "Answer to part 1: {}".format(count_combinations(container_sizes, 150))
    print "Answer to part 2: {}".format(count_minimal_combinations(container_sizes, 150))


if __name__ == "__main__":
    main()