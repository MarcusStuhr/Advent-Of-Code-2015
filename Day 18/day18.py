PUZZLE_DATA_FILENAME = "day18_input.txt"


def count_lights_on(grid, num_rows, num_cols):
    return sum(bin(num)[2:].count("1") for num in grid)

def get_bit(num, bit_index):
    return (num & (1 << bit_index)) != 0

def set_bit(num, bit_index):
    return num | (1 << bit_index)

def clear_bit(num, bit_index):
    return num & ~(1 << bit_index)


def evolve(grid, num_rows, num_cols, n, corners_fixed = False):
    
    if corners_fixed:
        grid[0] = set_bit(grid[0], 0)
        grid[0] = set_bit(grid[0], num_cols-1)
        grid[num_rows-1] = set_bit(grid[num_rows-1], 0)
        grid[num_rows-1] = set_bit(grid[num_rows-1], num_cols-1)
        
    if n==0:
        return count_lights_on(grid,num_rows,num_cols)

    newgrid = grid[:]
    
    for r in xrange(num_rows):
        for c in xrange(num_cols):
            if corners_fixed and (r,c) in [(0,0),(0,num_cols-1),(num_rows-1,0),(num_rows-1,num_cols-1)]:
                continue
            
            neighbors = 0
            
            for offsetr in [-1,0,1]:
                for offsetc in [-1,0,1]:
                    if offsetr==offsetc==0:
                        continue
                    neighbors += (0<=r+offsetr<num_rows and 0<=c+offsetc<num_cols and get_bit(grid[r+offsetr],c+offsetc)==1)

            if get_bit(grid[r],c) == 1:
                if neighbors==2 or neighbors==3:
                    newgrid[r] = set_bit(newgrid[r],c)
                else:
                    newgrid[r] = clear_bit(newgrid[r],c)
            else:
                if neighbors == 3:
                    newgrid[r] = set_bit(newgrid[r],c)
                else:
                    newgrid[r] = clear_bit(newgrid[r],c)
                    
    return evolve(newgrid,num_rows,num_cols,n-1,corners_fixed)


def main():
    lines = [line.replace("#","1").replace(".","0") for line in open(PUZZLE_DATA_FILENAME).read().split("\n")]
    num_rows, num_cols = len(lines), len(lines[0])
    grid = [int(line,2) for line in lines]
    print "Answer to part 1: {}".format(evolve(grid, num_rows, num_cols, 100))
    print "Answer to part 2: {}".format(evolve(grid, num_rows, num_cols, 100, True))


if __name__ == "__main__":
    main()