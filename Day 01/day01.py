import sys

def part1():
    with open(sys.argv[1]) as f:
        instructions = f.read()
    print instructions

def main():
    print part1()

if __name__ == "__main__":
    main()