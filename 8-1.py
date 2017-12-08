

def parse_line(line):
    """
    """
    action_map = {'inc': '+=',
                  'dec': '-='}
    data = line.strip().split(' ')
    return {'target': data[0].strip(),
            'action': '{} {}'.format(action_map[data[1]], data[2]),
            'condition': {'target': data[4],
                          'eval': data[5] + ' ' + data[6]}}


def action_instruction(instruction):
    if eval("registers['{}'] {}".format(instruction['condition']['target'],
                          instruction['condition']['eval'])):
        exec("registers['{}'] {}".format(instruction['target'],
                           instruction['action']))


actions_to_be_done = []
registers = {}

with open('8-input.txt', 'r') as f:
    for line in f:
        instruction = parse_line(line)
        if instruction['target'] not in registers:
            registers[instruction['target']] = 0            
        actions_to_be_done.append(instruction)


for instruction in actions_to_be_done:
    action_instruction(instruction)

print(max(registers.values()))