import re

PUZZLE_DATA_FILENAME = "day23_input.txt"

def get_b(instructions, init_a, init_b):
    a = init_a
    b = init_b
    pointer = 0

    while pointer < len(instructions):
        match1 = re.match(r"([\w]+) ([\w]+), ([+-]?[\d]+)", instructions[pointer])
        match2 = re.match(r"([\w]+) ([\w]+)", instructions[pointer])
        match3 = re.match(r"([\w]+) ([+-]?[\d]+)", instructions[pointer])
        
        if match1:
            m = match1.groups()
            opcode, register, number = m[0], m[1], int(m[2])
            if opcode=="jie" and register=="a" and a%2==0:
                pointer+=number
                continue
            elif opcode=="jie" and register=="b" and b%2==0:
                pointer+=number
                continue
            elif opcode=="jio" and register=="a" and a==1:
                pointer+=number
                continue
            elif opcode=="jio" and register=="b" and b==1:
                pointer+=number
                continue
            
        elif match2:
            m = match2.groups()
            opcode, register = m[0], m[1]
            if opcode=="hlf" and register=="a":
                a/=2
            elif opcode=="hlf" and register=="b":
                b/=2
            elif opcode=="tpl" and register=="a":
                a*=3
            elif opcode=="tpl" and register=="b":
                b*=3
            elif opcode=="inc" and register=="a":
                a+=1
            elif opcode=="inc" and register=="b":
                b+=1
                
        elif match3:
            m = match3.groups()
            opcode, num = m[0], int(m[1])
            if opcode=="jmp":
                pointer+=num
                continue

        pointer+=1

    return b

def main():
    instructions = open(PUZZLE_DATA_FILENAME).read().split("\n")
    print "Answer to part 1: {}".format(get_b(instructions,0,0))
    print "Answer to part 2: {}".format(get_b(instructions,1,0))

if __name__ == "__main__":
    main()