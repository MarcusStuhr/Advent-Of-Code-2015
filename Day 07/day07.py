import re


PUZZLE_DATA_FILENAME = "day07_input.txt"

OPERATIONS = {"AND": lambda a,b: a&b,
              "OR": lambda a,b: a|b,
              "NOT": lambda a: 65535-a,
              "RSHIFT": lambda a,b: a>>b,
              "LSHIFT": lambda a,b: a<<b,
              "SELF": lambda a: a}


def get_wire_value(incoming, wire_signals):
    """
    Inputs:
    incoming: A string, either in the form of a number, e.g. "15265", or a letter, e.g. "x"
    wire_signals: A dict that maps wire labels to their wire values, e.g. wire_signals["x"] -> 4
    
    Outputs:
    An integer representing the value represented by incoming. 
    Returns None if incoming is not a number or a letter found in wire_signals
    """
    if incoming in wire_signals:
        return wire_signals[incoming]
    elif incoming.isdigit():
        return int(incoming)
    else:
        return None


def parse_line(line):
    """
    Inputs:
    line: A string representing wire inputs to a wire output, e.g. "x AND 252 -> a"
    
    Outputs:
    A three-element tuple containing the inputs, the relevant operator, and the output wire.
    e.g. (['x', '252'], 'AND', 'a').
    
    The relevant operations can be found in OPERATIONS
    """
    lefthand_side, receiving_wire = line.strip().split(" -> ")

    op_findall = re.findall(r"[A-Z]+", lefthand_side)
    operator = op_findall[0] if op_findall else "SELF"
    input_wires = re.findall(r"[a-z0-9]+", lefthand_side)
    
    return input_wires, operator, receiving_wire


def run_circuit(instructions, overrides = {}):
    """
    Inputs:
    instructions: A list of tuples -- lines that have been parsed with parse_line()
    overrides: A dict of wire-mapping overrides, if desired. e.g. {"b": 25626}. Any mappings here will
    override any mappings in the instructions list.
    
    Outputs:
    A dict wire_signals representing the mappings of wire labels to wire outputs
    """
    wire_signals = {}
    instructions_copy = instructions[:]
    
    while len(instructions_copy) > 0:
        index = 0
        
        while index < len(instructions_copy):
            input_wires, operator, receiving_wire = instructions_copy[index]
            
            input_vals = [get_wire_value(incoming, wire_signals) for incoming in input_wires]
            
            if receiving_wire in wire_signals or None in input_vals:
                index+=1
            else:
                if receiving_wire in overrides:
                    wire_signals[receiving_wire] = overrides[receiving_wire]
                else:
                    wire_signals[receiving_wire] = OPERATIONS[operator](*input_vals)
                instructions_copy.pop(index)
            
    return wire_signals
    

def main():
    file_contents_string = open(PUZZLE_DATA_FILENAME).read()
    instructions = [parse_line(line) for line in file_contents_string.split('\n')]

    ans_part_1 = run_circuit(instructions)['a']
    ans_part_2 = run_circuit(instructions, {'b':ans_part_1})['a']
    
    print "Answer to part 1: {}".format(ans_part_1)
    print "Answer to part 2: {}".format(ans_part_2)

 
if __name__ == "__main__":
    main()