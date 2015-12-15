import sys
from collections import defaultdict
import re


PUZZLE_DATA_FILENAME = "day14_input.txt"


class Reindeer():

    def __init__(self, name, fly_speed, fly_duration, rest_duration):
        self.name = name
        self.fly_speed = fly_speed
        self.fly_duration = fly_duration
        self.rest_duration = rest_duration

    def get_distance(self, t):
        """
        returns the distance traveled by the reindeer at time t
        Time Complexity: O(1)
        """
        cycle_time = self.fly_duration + self.rest_duration
        num_cycles_completed = t / cycle_time
        remaining_time = t % cycle_time
        dist_traveled_full_cycles = num_cycles_completed * self.fly_speed * self.fly_duration
        additional_dist = min(remaining_time, self.fly_duration) * self.fly_speed
        dist_traveled_total = dist_traveled_full_cycles + additional_dist
        return dist_traveled_total



def dist_winning_reindeer_part_1(reindeer_dict, at_time):
    """
    Inputs:
    reindeer_dict: A dictionary mapping reindeer names to corresponding Reindeer objects
    at_time: The time (in seconds) for which we want the distance of the reindeer in 1st place

    Outputs:
    The distance traveled by the reindeer in first place as of at_time

    Time Complexity:
    O(n) where n is the number of reindeer
    """
    return max(reindeer.get_distance(at_time) for reindeer in reindeer_dict.values())



def points_winning_reindeer_part_2(reindeer_dict, at_time):
    """
    Inputs:
    reindeer_dict: A dictionary mapping reindeer names to corresponding Reindeer objects
    at_time: The time (in seconds) for which we want the max points achieved by any reindeer

    Outputs:
    The max points achieved by any reindeer as of at_time

    Time Complexity:
    O(nt) where n is the number of reindeer and t is the value of at_time
    """
    n = len(reindeer_dict.keys())
    points = defaultdict(int)

    for t in xrange(1, at_time+1):
        dist_data = [(reindeer.get_distance(t), reindeer.name) for reindeer in reindeer_dict.values()]
        best_dist = max(d[0] for d in dist_data)
        for dist, name in dist_data:
            if dist == best_dist:
                points[name]+=1

    return max(points.values())



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

    reindeer_dict = defaultdict(Reindeer)

    for line in lines:
        match = re.match(r"([\w]+) can fly ([\d]+) km/s for ([\d]+) seconds, but then must rest for ([\d]+) seconds.",line)
        if match:
            params = match.groups()
            name = params[0]
            fly_speed, fly_duration, rest_duration = map(int, params[1:])
            reindeer_dict[name] = Reindeer(name, fly_speed, fly_duration, rest_duration)

    ans_part_1 = dist_winning_reindeer_part_1(reindeer_dict, 2503)
    ans_part_2 = points_winning_reindeer_part_2(reindeer_dict, 2503)

    print "Answer to part 1: {}".format(ans_part_1)
    print "Answer to part 2: {}".format(ans_part_2)


if __name__ == "__main__":
    main()
