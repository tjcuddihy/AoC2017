from collections import defaultdict


def process_line(line):
    pre, post = line.split('<->')
    programs[pre.strip()] = [_.strip() for _ in post.split(',')]


programs = defaultdict(list)
input = []
with open('12-input.txt') as f:
    for line in f.readlines():
        process_line(line.strip())


groups = []
def scan(program):
    neighbours = programs[program]
    for group in groups:
        if program in group:
            for n in neighbours:
                group.add(n)
            return
        for n in neighbours:
            if n in group:
                for neighbour in neighbours:
                    group.add(neighbour)
                group.add(program)
                return
    # Neither program nor neighbours present
    new = set()
    for neighbour in neighbours:
        new.add(neighbour)
    new.add(program)
    groups.append(new)    
    return
        
for program in programs:
    scan(program)


reduction = True
while reduction:
    reduction = False
    for g in range(len(groups)):
        if groups[g] == False:
            continue
        for other in range(len(groups)):
            if g == other:
                continue
            if groups[other] == False:
                continue
            if len(groups[g].intersection(groups[other])) > 0:
                # print(g, other)
                reduction = True
                groups[g] = groups[g].union(groups[other])
                groups[other] = False

counter = 0
for g in groups:
    if g:
        counter += 1
print(counter)
print(len(programs))
print(len(groups))
