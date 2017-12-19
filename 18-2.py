import sys
from collections import deque
import copy

def operate(instr, own_register, own_queue, other_queue):
    if len(instr) > 2:
        val = own_register[instr[2]] if isinstance(instr[2], str) else instr[2]
    # Parse command
    if instr[0] == 'snd':
        val = own_register[instr[1]] if isinstance(instr[1], str) else instr[1]
        other_queue.append(val)
        # print('snd')
        return 'snd'
    elif instr[0] == 'set':
        own_register[instr[1]] = val
    elif instr[0] == 'add':
        own_register[instr[1]] += val
    elif instr[0] == 'mul':
        own_register[instr[1]] *= val
    elif instr[0] == 'mod':
        own_register[instr[1]] = own_register[instr[1]] % val
    elif instr[0] == 'rcv':
        try:
            val = own_queue.popleft()
            own_register[instr[1]] = val
        except IndexError:
            return 'lock'
    else: # instr[0] == 'jgz':
        if isinstance(instr[1], int):
            return val
        elif own_register[instr[1]] > 0:
            return val
    return 1

def play(instructions, registers):
    registers0 = copy.deepcopy(registers)
    registers1 = copy.deepcopy(registers)
    registers1['p'] = 1
    queue0 = deque()
    queue1 = deque()

    index0 = 0
    index1 = 0
    send_count1 = 0
    locked0 = False
    locked1 = False

    while True:
        locked0 = False
        incr0 = operate(instructions[index0], registers0, queue0, queue1)
        if isinstance(incr0, int):
            index0 += incr0
        else:
            if incr0 == 'lock':
                if locked1:
                    print('DEADLOCK: ', send_count1)
                    print(registers0)
                    print(registers1)
                    sys.exit()
                locked0 = True
            elif incr0 == 'snd':
                index0 += 1

        
        locked1 = False
        incr1 = operate(instructions[index1], registers1, queue1, queue0)
        if isinstance(incr1, int):
            index1 += incr1
        else:
            if incr1 == 'lock':
                if locked0:
                    print('DEADLOCK: ', send_count1)
                    print(registers0)
                    print(registers1)
                    sys.exit()
                locked1 = True
            elif incr1 == 'snd':
                send_count1 += 1
                index1 += 1


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
    play(instructions, registers)
