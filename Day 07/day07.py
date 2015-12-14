import sys
import re


PUZZLE_DATA_FILENAME = "day07_input.txt"

OPERATIONS = {"AND": lambda a,b: a&b,
              "OR": lambda a,b: a|b,
              "NOT": lambda a: 65535-a,
              "RSHIFT": lambda a,b: a>>b,
              "LSHIFT": lambda a,b: a<<b,
              "SELF": lambda a: a}


def get_wire_value(input, wire_signals):
    if input in wire_signals:
        return wire_signals[input]
    elif input.isdigit():
        return int(input)
    else:
        return None


def parse_line(line):
    lefthand_side, receiving_wire = line.strip().split(" -> ")

    op_findall = re.findall(r"[A-Z]+", lefthand_side)
    operator = op_findall[0] if op_findall else "SELF"
    input_wires = re.findall(r"[a-z0-9]+", lefthand_side)
    
    return input_wires, operator, receiving_wire


def run_circuit(instructions, overrides = {}):
    wire_signals = {}
    instructions_copy = instructions[:]
    
    while len(instructions_copy) > 0:
        index = 0
        
        while index < len(instructions_copy):
            input_wires, operator, receiving_wire = instructions_copy[index]
            
            input_vals = [get_wire_value(input, wire_signals) for input in input_wires]
            
            if receiving_wire in wire_signals or None in input_vals:
                index+=1
            else:
                if receiving_wire in overrides:
                    wire_signals[receiving_wire] = overrides[receiving_wire]
                else:
                    wire_signals[receiving_wire] = OPERATIONS[operator](*input_vals)
                instructions_copy.pop(index)
            
    return wire_signals


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
    instructions = [parse_line(line) for line in file_contents_string.split('\n')]

    ans_part_1 = run_circuit(instructions)['a']
    ans_part_2 = run_circuit(instructions, {'b':ans_part_1})['a']
    
    print "Answer to part 1: {}".format(ans_part_1)
    print "Answer to part 2: {}".format(ans_part_2)

 
if __name__ == "__main__":
    main()