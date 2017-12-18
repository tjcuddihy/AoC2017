import sys
from collections import defaultdict

last_frequency = 0

def operate(instr, registers):
    global last_frequency
    if len(instr) > 2:
        val = registers[instr[2]] if isinstance(instr[2], str) else instr[2]
    if instr[0] == 'snd':
        last_frequency = registers[instr[1]]
    elif instr[0] == 'set':
        registers[instr[1]] = val
    elif instr[0] == 'add':
        registers[instr[1]] += val
    elif instr[0] == 'mul':
        registers[instr[1]] *= val
    elif instr[0] == 'mod':
        registers[instr[1]] = registers[instr[1]] % val
    elif instr[0] == 'rcv':
        if registers[instr[1]] > 0:
            print('RCV: ', last_frequency)
            sys.exit()
    else: # instr[0] == 'jgz':
        if registers[instr[1]] > 0:
            return val
    return 1

def play(instructions, registers):
    i = 0
    while True:
        incr = operate(instructions[i], registers)
        i += incr

if __name__ == '__main__':
    instructions = []
    registers={}
    with open('18-input.txt') as f:
        for line in f.readlines():
            cmd = line.strip().split()
            if cmd[1].isalpha():
                registers[cmd[1]] = 0
            else:
                cmd[1] = int(cmd[1])
            if len(cmd) > 2:
                if cmd[2].isalpha():
                    registers[cmd[2]] = 0
                else:
                    cmd[2] = int(cmd[2])
            instructions.append(cmd)
    print(len(instructions))
    print(registers)
    play(instructions, registers)
