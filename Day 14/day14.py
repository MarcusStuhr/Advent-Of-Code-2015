import sys
from collections import defaultdict
import re

PUZZLE_DATA_FILENAME = "day14_input.txt"


def get_file_input(filename):
    try:
        with open(filename) as f:
            data = f.read()
        return data
    except IOError:
       print "Unable to open/read input file {}".format(filename)
       sys.exit(1)


class Reindeer():
    def __init__(self, name, fly_speed, fly_duration, rest_duration):
        self.name = name
        self.fly_speed = fly_speed
        self.fly_duration = fly_duration
        self.rest_duration = rest_duration


def get_distance(reindeer, at_time):
    cycle_time = reindeer.fly_duration + reindeer.rest_duration
    num_cycles_completed = at_time / cycle_time
    dist_traveled_full_cycles = num_cycles_completed * reindeer.fly_speed * reindeer.fly_duration
    remaining_time = at_time - num_cycles_completed * cycle_time
    additional_dist = min(remaining_time, reindeer.fly_duration) * reindeer.fly_speed
    dist_traveled_total = dist_traveled_full_cycles + additional_dist
    return dist_traveled_total


def dist_winning_reindeer_part_1(reindeer_dict, at_time):
    best_dist = 0
    
    for reindeer in reindeer_dict.values():
        dist_traveled_total = get_distance(reindeer, at_time)
        best_dist = max(best_dist, dist_traveled_total)
        
    return best_dist


def points_winning_reindeer_part_2(reindeer_dict, time_limit):
    best_pts = 0
    n = len(reindeer_dict.keys())
    points = defaultdict(int)
    
    for at_time in xrange(1,time_limit+1):
        dist_data = [(get_distance(reindeer, at_time), reindeer.name) for reindeer in reindeer_dict.values()]
        best_dist = max(d[0] for d in dist_data)
        for dist, name in dist_data:
            if dist == best_dist:
                points[name]+=1
                
    return max(points.values())


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