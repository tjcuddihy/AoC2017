from collections import defaultdict
input = []



def process_line(line):
    pre, post = line.split('<->')
    programs[pre.strip()] = [_.strip() for _ in post.split(',')]

programs = defaultdict(list)

with open('12-input.txt') as f:
    for line in f.readlines():
        process_line(line.strip())


zero_neighbours = set()
def scan(program):
    zero_neighbours.add(program)
    for neighbour in programs[program]:
        if neighbour not in zero_neighbours:
            scan(neighbour)
    return True

scan('0')

print(len(zero_neighbours))